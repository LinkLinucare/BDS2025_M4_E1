import pandas as pd
import seaborn as sns
import sqlite3

# Load the Penguins dataset & remove missing values
penguins = sns.load_dataset("penguins").dropna()

# Prepare DataFrames for Tables
islands_df = pd.DataFrame({
    'island_id': range(1, penguins['island'].nunique() + 1),
    'name': penguins['island'].unique()
})

# Assign each penguin an animal_id
penguins['animal_id'] = range(1, len(penguins) + 1)

# Merge penguins dataset with island_id mapping
penguins_df = penguins.merge(islands_df, left_on='island', right_on='name', how='left')[[
    'species', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 
    'body_mass_g', 'sex', 'island_id', 'animal_id'
]]

# Create SQLite Database
db_path = 'data/penguins.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Enable foreign key support
cursor.execute("PRAGMA foreign_keys = ON;")

# Create ISLANDS table (prevents duplicate islands)
cursor.execute('''
CREATE TABLE IF NOT EXISTS ISLANDS (
    island_id INTEGER PRIMARY KEY,
    name TEXT UNIQUE
);
''')

# Create PENGUINS table with a primary key
cursor.execute('''
CREATE TABLE IF NOT EXISTS PENGUINS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    species TEXT,
    bill_length_mm REAL,
    bill_depth_mm REAL,
    flipper_length_mm REAL,
    body_mass_g REAL,
    sex TEXT,
    island_id INTEGER,
    animal_id INTEGER UNIQUE,
    FOREIGN KEY (island_id) REFERENCES ISLANDS(island_id)
);
''')

# Insert Data into ISLANDS Table (Avoid Duplicates)
islands_data = islands_df.to_records(index=False)
cursor.executemany("INSERT OR IGNORE INTO ISLANDS (island_id, name) VALUES (?, ?);", islands_data)

# Insert Data into PENGUINS Table (Avoid Duplicates)
penguins_data = penguins_df.to_records(index=False)
cursor.executemany("""
INSERT OR REPLACE INTO PENGUINS (species, bill_length_mm, bill_depth_mm, 
                                 flipper_length_mm, body_mass_g, sex, island_id, animal_id)
VALUES (?, ?, ?, ?, ?, ?, ?, ?);
""", penguins_data)

# Commit and Close
conn.commit()
conn.close()

print(f"✅ Database '{db_path}' updated successfully!")