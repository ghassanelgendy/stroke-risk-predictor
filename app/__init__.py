from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
import os  # Add the 'os' module for path manipulation

app = Flask(__name__)

# Get the absolute path to the directory containing this script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Adjust the path to the pre-trained model based on the current directory
model_path = os.path.join(current_directory, "model", "logistic_model.pkl")

# Load the pre-trained model
model = joblib.load(model_path)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Retrieve user input data from the form and convert to integers
        smoking = int(request.form["smoking"])
        age = float(request.form["age"])
        bmi = float(request.form["bmi"])
        glucose = float(request.form["glucose"])
        marry = int(request.form["marry"])
        hyper_tention = int(request.form["hyper_tention"])
        heart_disease = int(request.form["heart_disease"])
        work_state = int(request.form["work_state"])

        # Perform any necessary data preprocessing here

        # Create a feature vector from the user input
        features = [
            age,
            hyper_tention,
            heart_disease,
            marry,
            work_state,
            glucose,
            bmi,
            smoking,
        ]

        # Make a prediction using your model
        prediction = model.predict(np.array(features).reshape(1, -1))

        if prediction[0] == 1:
            result = "really really dead"
        else:
            result = "thank god he is alive"

        # Return the prediction result as JSON
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
