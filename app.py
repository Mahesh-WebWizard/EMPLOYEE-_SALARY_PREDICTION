import streamlit as st
import pandas as pd
import joblib

# for overwriting jupyterfile to py file
# Load the trained model
model=joblib.load('best_model.pk1')

# layout of the pg
st.set_page_config(page_title='Employee Salary Classification', page_icon='💼', layout='centered')

# short title & description on main web page
st.title('💼 Employee Salary Prediction App')
st.markdown('Predict whether an employee earns >50k or <=50k based on input features:')

# Sidebar inputs (these must match your training feature columns)
st.sidebar.header("Input Employee Details")

# Replace these fields with your dataset's actual input columns
age = st.sidebar.slider("Age", 18, 65, 30)
education = st.sidebar.selectbox("Education Level", [
    "Bachelors", "Masters", "PhD", "HS-grad", "Assoc", "Some-college"
])
occupation = st.sidebar.selectbox("Job Role", [
    "Tech-support", "Craft-repair", "Other-service", "Sales",
    "Exec-managerial", "Prof-specialty", "Handlers-cleaners", "Machine-op-inspct",
    "Adm-clerical", "Farming-fishing", "Transport-moving", "Priv-house-serv",
    "Protective-serv", "Armed-Forces"
])
hours_per_week = st.sidebar.slider("Hours per week", 1, 80, 40)
experience = st.sidebar.slider ("Years of Experience", 0, 40, 5)

# Build input DataFrame (must match preprocessing of your training data)
input_df = pd.DataFrame({
    'age': [age],
    'education': [education],
    'occupation': [occupation],
    'hours-per-week': [hours_per_week],
    'experience': [experience]
})

st.write("### Input Data")
st.write(input_df)

# Predict button
if st.button("Predict Salary Class"):
    prediction = model.predict(input_df)
    st.success(f"Prediction: {prediction[0]}")

# Batch prediction
st.markdown('---')
st.markdown('#### Batch Prediction')
uploaded_file = st.file_uploader("Upload a CSV file for batch prediction", type="csv")
if uploaded_file is not None:
    batch_data = pd.read_csv(uploaded_file)
    st.write("Uploaded data preview:", batch_data.head())
    batch_preds = model.predict(batch_data)
    batch_data['PredictedClass'] = batch_preds
    st.write("Predictions:")
    st.write(batch_data.head())
    csv = batch_data.to_csv(index=False).encode('utf-8')
    st.download_button("Download Predictions CSV", csv, file_name='predicted_classes.csv', mime='text/csv')
