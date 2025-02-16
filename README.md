# Weather-Based Recommendation System

This project predicts recommendations based on weather conditions using Machine Learning and Flask API.

Title of the Project:

Weather Based Recommendation System

Overview:

This project is a Machine Learning-based recommendation system that suggests clothing, activities, travel plans, and food based on weather conditions.
It uses a Random Forest Classifier to provide predictions and is deployed as a Flask API, allowing users to input weather parameters and receive personalized recommendations.

Features:

Predicts Clothing, Activity, Travel, and Food Recommendations
Trained using Real-World Weather Data
Flask API for Easy Integration (Tested with Postman)
Preprocessed Data for Improved Model Accuracy
Deployable in Production Environments


Technologies Used:
Machine Learning: Scikit-Learn
Backend API: Flask
Data Processing: Pandas, NumPy
Version Control: Git, GitHub
Testing Tool: Postman


How to run the project?
Clone the rpository or copy the code
Install dependecies
Train the model and save it
Start the Flask API
Finally, test with Postman
Please check these parameters before execute in the Postman

  Endpoint: Will be given once when the program is executed, add it in the URL
  Method: Change the method from Get to POST
  Body: (JSON Example)

    {
    "MEAN ANNUAL AIR TEMP": 15.0,
    "MEAN MONTHLY MAX TEMP": 18.0,
    "MEAN MONTHLY MIN TEMP": 10.0,
    "MEAN ANNUAL WIND SPEED": 3.0,
    "MEAN CLOUD COVER": 60.0,
    "MEAN ANNUAL SUNSHINE": 1200.0,
    "MEAN ANNUAL RAINFALL": 500.0,
    "MAX MONTHLY WIND SPEED": 2.0,
    "MAX AIR TEMP": 30.0,
    "MAX WIND SPEED": 15.0,
    "MAX RAINFALL": 50.0,
    "MIN AIR TEMP": -5.0,
    "EXTRA_FEATURE_1": 7.0,
    "EXTRA_FEATURE_2": 3.5,
    "EXTRA_FEATURE_3": 68.0
    }

Author: Abhiram Ramakrishnan

Email ID: abhiramramakrishnan10@gmail.com

LinkedIn: https://www.linkedin.com/in/abhiram-ramakrishnan-5179b9201/