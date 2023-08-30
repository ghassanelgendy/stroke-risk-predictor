from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import joblib
import os
#app = Flask(__name__)
#model_file_path = os.path.join('flask app', 'logistic_regression_model.pkl')

# Load the trained model
loaded_model = joblib.load("C:\\Users\\wahda\\OneDrive\\Desktop\\stroke\\stroke-risk-predictor\\flask app\\logistic_regression_model.pkl")
# Load the trained model when the application starts
#loaded_model = joblib.load('logistic_regression_model.pkl')


input_data = [[1,67, 0, 1, 1, 1, 228.69, 36.6, 1]]

# Make predictions
predictions = loaded_model.predict(input_data)

# Display predictions
print("Predictions:", predictions)


#@app.route('/')
#def index():
 #   return render_template('index.html')

#@app.route('/predict', methods=['POST'])
#def predict():
 #   try:
  #      # Get user input from the form
   #     features = [float(x) for x in request.form.values()]
#
 #       # Make a prediction using the loaded model
  #      prediction = loaded_model.predict([features])
#
 #       # Return the prediction to the user
  #      return render_template('result.html', prediction=prediction[0])
#
 #   except Exception as e:
  #      return str(e)
#
#if __name__ == '__main__':
 #   app.run(debug=True)
