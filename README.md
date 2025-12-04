# Fake-User-Detection-Using-Flask
1. Fake Social Media Profile Detection

A Machine Learning-powered Flask web application that predicts whether a social media profile is Real or Fake based on user-provided input features.

2. Overview

This project aims to detect fake user accounts commonly found on online social platforms. Using machine learning techniques and a simple web interface, the system classifies user profiles into:

Real User

Fake User

It uses a Random Forest Classifier trained on a custom dataset (modified_data.csv) and provides prediction results along with key model evaluation metrics.

3. Features

🔍 Detects Fake vs. Real user profiles

🧠 Built using Machine Learning (Random Forest Classifier)

📊 Shows model accuracy, confusion matrix & classification report

🌐 Simple and intuitive Flask-based web interface

📝 Dynamically loads input fields based on dataset columns

4. 📂 Project Structure

```plaintext
fake-profile-detection/
├── app.py                   # Main Flask application
├── modified_data.csv        # Dataset used for training the model
├── templates/
│   └── index.html           # Frontend UI for prediction
├── static/                  # Optional CSS/JS assets
│   └── (your styles/scripts)
├── requirements.txt         # Dependencies (if included)
└── README.md                # Documentation file
```


5. How It Works
1️⃣ Data Preparation

Dataset loaded from modified_data.csv

Features extracted as input (X)

Labels (Y) define Real vs Fake profile

2️⃣ Model Training

Train-test split (80% training, 20% testing)

Random Forest Classifier with 100 trees

Evaluates performance using:

Accuracy

Confusion Matrix

Classification Report

3️⃣ Prediction Flow

User enters feature values into the web form

Application creates a DataFrame from input

ML model predicts:

Real User

Fake User

Result displayed instantly in the UI

6. Technologies Used

Python 3

Flask

Pandas

Scikit-Learn

HTML / CSS / Bootstrap
