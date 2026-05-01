import streamlit as st
import numpy as np
import joblib
import os

# Specify the custom save path for models and scalers
path = '../Models/naive_bayes.pkl'
feature_scaler_filename = "../Models/feature_scaler.pkl"

# Load the scaler
feature_scaler = joblib.load(feature_scaler_filename)

# Load all the models
model = joblib.load(path)
model_feature_scaler = joblib.load(feature_scaler_filename)

# Define the input fields for the features
st.title('Crop Recommendation System')

st.write("Please input the following features:")

# Input fields for the selected features
n = st.number_input('Nitrogen (N)', value=0.0)
p = st.number_input('Phosphorus (P)', value=0.0)
k = st.number_input('Potassium (K)', value=0.0)
temperature = st.number_input('Temperature (°C)', value=0.0)
humidity = st.number_input('Humidity (%)', value=0.0)
ph = st.number_input('PH', value=0.0)
rainfall = st.number_input('Rainfall (mm)', value=0.0)

# Create a feature vector from the input
features = np.array([[n, p, k, temperature, humidity, ph, rainfall]])

# Scale the input features using the loaded feature scaler
features_scaled = model_feature_scaler.transform(features)

# Predict the crop type using all models
if st.button('Predict Crop Type'):
    st.write('Predictions:')
    prediction = model.predict(features_scaled)[
        0]  # Get the predicted class

    # Display the predicted class
    st.write(f'La prediction du model est: {prediction}')
