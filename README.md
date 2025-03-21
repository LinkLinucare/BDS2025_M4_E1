<h2>🚀 Project Overview</h2>
<ul>
    <li>Utilizes a <strong>Random Forest model</strong> to classify penguin species.</li>
    <li><strong>GitHub Actions automation</strong> updates predictions daily at 7:30 AM.</li>
    <li><strong>SQLite database</strong> stores penguin data.</li>
    <li><strong>Frontend:</strong> A static HTML page fetches and displays daily predictions.</li>
    <li><strong>Optional Streamlit App:</strong> Allows users to input penguin features for real-time classification.</li>
</ul>

<h2>📂 Project Structure</h2>
<pre>
<code>
BDS_2025_M4_Exercise_1/
├── .github/workflows/        # GitHub Actions workflows
│   ├── fetch_and_predict.yml  # Automates daily data fetching and predictions
│
├── data/                     # Data storage
│   ├── penguins.db            # SQLite database containing penguin data
│   ├── penguin_prediction.json # Daily updated JSON with the latest prediction
│
├── models/                   # Trained model and preprocessing tools
│   ├── model.pkl              # Random Forest model
│   ├── le.pkl                 # Label encoder
│   ├── scaler.pkl             # Scaler for feature normalization
│
├── src/                      # Python scripts for data processing and modeling
│   ├── data_to_db.py          # Converts raw data into SQLite database
│   ├── train_model.py         # Trains the ML model
│   ├── predict_penguin.py     # Generates daily predictions
│
├── index.html                 # Frontend webpage displaying predictions
├── README.md                   # Project documentation
├── requirements.txt            # Dependencies
</code>
</pre>

<h2>⚙️ How It Works</h2>
<ol>
    <li><strong>Data Processing:</strong> `data_to_db.py` processes the raw penguin dataset and stores it in `penguins.db`.</li>
    <li><strong>Model Training:</strong> `train_model.py` trains a <strong>Random Forest classifier</strong> to predict penguin species.</li>
    <li><strong>Daily Predictions:</strong> `fetch_and_predict.yml` fetches the latest data and updates `penguin_prediction.json` daily.</li>
    <li><strong>Frontend Display:</strong> `index.html` fetches `penguin_prediction.json` and displays the latest prediction using JavaScript.</li>
</ol>

<h2>📦 Installation & Setup</h2>
<pre>
<code>
# Clone the Repository
git clone https://github.com/LinkLinucare/BDS2025_M4_E1.git
cd BDS2025_M4_E1

# Install Dependencies
pip install -r requirements.txt

# Prepare the Database
python src/data_to_db.py

# Train the Model (Only Needed for Retraining)
python src/train_model.py

# Generate a Prediction
python src/predict_penguin.py
</code>
</pre>

<h2>🌐 Hosting the Frontend with GitHub Pages</h2>
<p>To host `index.html` using <strong>GitHub Pages</strong>:</p>
<ol>
    <li><strong>Move `index.html` to the `docs/` directory.</strong></li>
    <li>In GitHub:
        <ul>
            <li>Go to <strong>Settings > Pages</strong>.</li>
            <li>Set the source branch to <strong>main</strong> and folder to <strong>/docs</strong>.</li>
            <li>Click "Save" to deploy.</li>
        </ul>
    </li>
</ol>
<p>Your project will be available at:</p>
<pre><code>https://LinkLinucare.github.io/BDS2025_M4_E1/</code></pre>

<h2>📌 Notes</h2>
<ul>
    <li>`penguin_prediction.json` is updated <strong>automatically every day</strong>, so avoid manual modifications.</li>
    <li>The frontend fetches the JSON file from `/penguin_prediction.json`, so ensure it exists.</li>
</ul>

<h2>🛠 Future Improvements</h2>
<ul>
    <li>Improve model accuracy with additional training data.</li>
    <li>Add a Streamlit backend for real-time input predictions.</li>
    <li>Enhance the UI for a better user experience.</li>
</ul>