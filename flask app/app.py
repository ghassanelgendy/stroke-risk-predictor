from flask import Flask, render_template, request,jsonify
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import joblib



app = Flask(__name__)

# Load the pre-trained model
model = joblib.load("C:\\Users\\wahda\\OneDrive\\Desktop\\stroke\\stroke-risk-predictor\\flask app\\logistic_model.pkl")

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Receive data from the POST request
        data = request.json  
        
        if 'age' not in data or 'hyper_tension' not in data or 'heart_disease' not in data or'marry' not in data or'work_type' not in data or'smoking' not in data or'glucose' not in data or'bmi' not in data :
            return jsonify({'error': 'Missing features'}), 400
        
        age = data['age']
        hyper_tension = data['hyper_tension']
        heart_disease = data['heart_disease']
        work_type = data['work_type']
        smoking = data['smoking']
        glucose = data['glucose']
        bmi = data['bmi']
        marry = data['marry']
        # Extract the other features similarly
        
        # Ensure the features are in the correct data type and format
        age = float(age)
        hyper_tension = int(hyper_tension)
        heart_disease = int(heart_disease)
        work_type = int(work_type)
        marry = int(marry)
        bmi = float(bmi)
        smoking = int(smoking)
        glucose = float(glucose)
        # Convert and validate the other features
        
        # Prepare the data for prediction as a 2D array
        input_data = [[age, hyper_tension, heart_disease,marry,work_type,glucose,bmi,smoking]]  # Include all eight features
        
        # Make predictions using the model
        prediction = model.predict(input_data)
        
        # Return the prediction as JSON response
        return jsonify({'prediction': prediction[0]})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
