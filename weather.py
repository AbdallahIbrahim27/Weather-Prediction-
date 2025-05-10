import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('model.pkl')

st.title("🌦️ Rain Prediction")

st.write("Enter today's weather details:")

# Input fields — now includes 6 features
min_temp = st.number_input("Min Temperature (°C)", value=10.0)
max_temp = st.number_input("Max Temperature (°C)", value=25.0)
humidity_3pm = st.number_input("Humidity at 3pm (%)", value=60)
rainfall = st.number_input("Rainfall (mm)", value=0.0)
wind_speed_9am = st.number_input("Wind Speed at 9am (km/h)", value=15.0)
pressure_9am = st.number_input("Pressure at 9am (hPa)", value=1012.0)

# Predict
if st.button("Predict Rain Tomorrow"):
    features = np.array([[min_temp, max_temp, humidity_3pm, rainfall, wind_speed_9am, pressure_9am]])
    prediction = model.predict(features)[0]
    result = "🌧️ Yes, it will rain tomorrow." if prediction == 1 else "☀️ No, it won't rain tomorrow."
    st.subheader("Prediction:")
    st.success(result)
