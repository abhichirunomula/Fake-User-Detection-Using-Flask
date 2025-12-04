# Fake-User-Detection-Using-Flask
1. Overview

This project is a Fake Social Media Profile Detection System built using Flask and a Random Forest Classifier.
It predicts whether a social media profile is Real or Fake based on user-input features.

2. Project Structure
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
5. How the System Works

Load Dataset

Split Features (X) and Labels (Y)

Train/Test Split (80/20)

Train Random Forest Classifier

Evaluate using:

Accuracy

Confusion Matrix

Classification Report

Predict Real/Fake Profile using the trained model    
