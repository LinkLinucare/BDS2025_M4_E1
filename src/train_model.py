import sqlite3
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# Loading dataset from SQLite
conn = sqlite3.connect('data/penguins.db')
df = pd.read_sql("SELECT * FROM PENGUINS", conn)
conn.close()

# Feature selection (These features are chosen, since those are the ones given from APi, where a new penguin spotted in the streets of NY every day)
X = df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]
y = df['species']

# Scaling the chosen features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Encoding species label
le = LabelEncoder()
y = le.fit_transform(y)

# Creating a train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# Training the XGBoost classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Saving trained model and label encoder
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("models/le.pkl", "wb") as f:
    pickle.dump(le, f)
with open("models/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Model, scaler, and label encoder trained and saved successfully!")
