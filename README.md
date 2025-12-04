# Fake-User-Detection-Using-Flask
🕵️‍♂️ Fake Social Media Profile Detection

A Machine Learning-powered Flask web application that predicts whether a social media profile is Real or Fake based on user-provided input features.

🚀 Overview

This project aims to detect fake user accounts commonly found on online social platforms. Using machine learning techniques and a simple web interface, the system classifies user profiles into:

Real User

Fake User

It uses a Random Forest Classifier trained on a custom dataset (modified_data.csv) and provides prediction results along with key model evaluation metrics.

✨ Features

🔍 Detects Fake vs. Real user profiles

🧠 Built using Machine Learning (Random Forest Classifier)

📊 Shows model accuracy, confusion matrix & classification report

🌐 Simple and intuitive Flask-based web interface

📝 Dynamically loads input fields based on dataset columns

📂 Project Structure
project/
│── app.py                # Main Flask application
│── modified_data.csv     # Dataset used for training
│── templates/
│     └── index.html      # Frontend UI
│── static/               # (Optional) CSS/JS files
│── README.md             # Documentation

🧠 Machine Learning Pipeline

Data Loading

Reads modified_data.csv

Splits into features (X) and label (Y)

Train-Test Split

80% training, 20% testing

Stratified to maintain class balance

Model Training

Uses Random Forest Classifier (100 trees)

Tuned for reliable binary classification

Model Evaluation

Accuracy score

Confusion matrix

Classification report (precision, recall, F1-score)

Prediction Flow

User enters input values

Model predicts → Real User or Fake User

Results displayed instantly on UI

🖥️ Running the Application
1️⃣ Install Dependencies
pip install flask pandas scikit-learn


Or use your requirements.txt when uploaded.

2️⃣ Start the Flask Application
python app.py

3️⃣ Open Browser

Visit:

http://127.0.0.1:5000/
