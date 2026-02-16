# Import libraries
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Title
st.title("Electric Motor Temperature Prediction")

# Description
st.write("""
This app predicts the **temperature of an electric motor** based on input parameters.
""")

# Sidebar inputs
st.sidebar.header("Input Parameters")
voltage = st.sidebar.number_input("Voltage (V)", min_value=0.0, max_value=500.0, value=230.0)
current = st.sidebar.number_input("Current (A)", min_value=0.0, max_value=100.0, value=10.0)
speed = st.sidebar.number_input("Speed (RPM)", min_value=0.0, max_value=5000.0, value=1500.0)
torque = st.sidebar.number_input("Torque (Nm)", min_value=0.0, max_value=100.0, value=20.0)
ambient_temp = st.sidebar.number_input("Ambient Temperature (°C)", min_value=-20.0, max_value=60.0, value=25.0)

# Load model
# with open("motor_model.pkl", "rb") as f:
#     model = pickle.load(f)

# Prepare input data
input_data = pd.DataFrame({
    "Voltage": [voltage],
    "Current": [current],
    "Speed": [speed],
    "Torque": [torque],
    "AmbientTemperature": [ambient_temp]
})

# Predict button
if st.button("Predict Temperature"):
    # prediction = model.predict(input_data)
    
    # Temporary placeholder if model not saved
    prediction = np.random.uniform(30, 100, size=1)
    
    st.success(f"Predicted Motor Temperature: {prediction[0]:.2f} °C")
