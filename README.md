🐧 Penguin AI Prediction Project

This project predicts the species of a penguin based on its physical characteristics. A trained machine learning model is used to generate daily predictions, which are stored in a JSON file and displayed on a simple frontend.

🚀 Project Overview

Utilizes a Random Forest model to classify penguin species.

GitHub Actions automation updates predictions daily at 7:30 AM.

SQLite database stores penguin data.

Frontend: A static HTML page fetches and displays daily predictions.

Optional Streamlit App: Allows users to input penguin features for real-time classification.

📂 Project Structure

BDS_2025_M4_Exercise_1/
│── .github/workflows/        # GitHub Actions workflows
│   ├── fetch_and_predict.yml  # Automates daily data fetching and predictions
│
│── data/                     # Data storage
│   ├── penguins.db            # SQLite database containing penguin data
│   ├── penguin_prediction.json # Daily updated JSON with the latest prediction
│
│── models/                   # Trained model and preprocessing tools
│   ├── model.pkl              # Random Forest model
│   ├── le.pkl                 # Label encoder
│   ├── scaler.pkl             # Scaler for feature normalization
│
│── src/                      # Python scripts for data processing and modeling
│   ├── data_to_db.py          # Converts raw data into SQLite database
│   ├── train_model.py         # Trains the ML model
│   ├── predict_penguin.py     # Generates daily predictions
│
│── index.html                 # Frontend webpage displaying predictions
│── README.md                   # Project documentation
│── requirements.txt            # Dependencies

⚙️ How It Works

1️⃣ Data Processing

data_to_db.py processes the raw penguin dataset and stores it in penguins.db.

2️⃣ Model Training

train_model.py trains a Random Forest classifier to predict penguin species.

The trained model is stored in models/model.pkl.

3️⃣ Daily Predictions (Automated via GitHub Actions)

fetch_and_predict.yml runs every morning to:

Fetch the latest penguin data.

Use predict_penguin.py to generate a new prediction.

Save the prediction to data/penguin_prediction.json.

4️⃣ Frontend Display

The index.html file fetches penguin_prediction.json and displays the latest prediction using JavaScript.

📦 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/your-username/BDS_2025_M4_Exercise_1.git
cd BDS_2025_M4_Exercise_1

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Prepare the Database

python src/data_to_db.py

4️⃣ Train the Model (Only Needed for Retraining)

python src/train_model.py

5️⃣ Generate a Prediction

python src/predict_penguin.py

🌐 Hosting the Frontend with GitHub Pages

To host index.html using GitHub Pages:

Move index.html to the docs/ directory

In GitHub:

Go to Settings > Pages.

Set the source branch to main and folder to /docs.

Click "Save" to deploy.

Your project will be available at:

https://your-username.github.io/BDS_2025_M4_Exercise_1/

📌 Notes

penguin_prediction.json is updated automatically every day, so avoid manual modifications.

The frontend fetches the JSON file from /data/penguin_prediction.json, so ensure it exists.

🛠 Future Improvements

Improve model accuracy with additional training data.

Add a Streamlit backend for real-time input predictions.

Enhance the UI for a better user experience.

🚀 Happy Coding! 🐧