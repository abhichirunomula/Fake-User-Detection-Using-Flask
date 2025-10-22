from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

app = Flask(__name__)

# --- Loading and Preparing the data ---
df = pd.read_csv('modified_data.csv')
X = df.drop(columns='Label')
Y = df['Label']

# --- Spliting of data for Training and Testing ---
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42,stratify=Y)

# --- Training the Model ---
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, Y_train)

# --- Evaluating the Model ---
y_pred = model.predict(X_test)
report = classification_report(Y_test, y_pred, output_dict=True)
accuracy = accuracy_score(Y_test, y_pred)
conf_matrix = confusion_matrix(Y_test, y_pred)

# --- Define Routes ---
@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_label = None
    input_values = None

    if request.method == 'POST':
        try:
            # Reading the input values in column order
            input_values = [float(request.form.get(col)) for col in X.columns]
            input_df = pd.DataFrame([input_values], columns=X.columns)

            # Predict's the class (0 or 1)
            prediction = model.predict(input_df)[0]
            prediction_label = "Fake User" if prediction == 1 else "Real User"
        except Exception as e:
            prediction_label = f"Error: {e}"

    return render_template('index.html',
                           columns=X.columns,
                           prediction=prediction_label,
                           input_values=input_values,
                           accuracy=round(accuracy * 100, 2),
                           report=report,
                           conf_matrix=conf_matrix.tolist())

if __name__ == '__main__':
    app.run(debug=True)
