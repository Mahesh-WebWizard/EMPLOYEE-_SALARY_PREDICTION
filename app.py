# app.py

import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load('model_knn.pkl')
scaler = joblib.load('scaler.pkl')

# Title
st.title("Employee Salary Prediction 💼")

# Input fields
age = st.slider("Age", 18, 70, 30)
gender = st.selectbox("Gender", ["Male", "Female"])
degree = st.selectbox("Education Level", ["Bachelor's", "Master's", "PhD"])
job = st.selectbox("Job Title", ["Software Engineer", "Data Analyst", "Senior Manager", "Sales Associate", "Director"])
experience = st.slider("Years of Experience", 0, 40, 5)

# Encode inputs manually
gender_encode = 1 if gender == 'Male' else 0
degree_encode = {"Bachelor's": 0, "Master's": 1, "PhD": 2}[degree]
job_encode = {
    "Software Engineer": 3,
    "Data Analyst": 0,
    "Senior Manager": 4,
    "Sales Associate": 2,
    "Director": 1
}[job]

# Scale numeric inputs
age_scaled = scaler.transform([[age]])[0][0]
exp_scaled = scaler.transform([[experience]])[0][0]

# Prepare final input
features = np.array([[age_scaled, gender_encode, degree_encode, job_encode, exp_scaled]])

# Predict salary
if st.button("Predict Salary"):
    prediction = model.predict(features)[0]
    st.success(f"Predicted Salary: ₹{prediction:,.2f}")
