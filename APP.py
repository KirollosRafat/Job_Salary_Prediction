import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("salary_model.joblib")

st.title("💼 Salary Prediction App")
st.write("Predict employee salaries based on demographic and job information.")

# Input fields
age = st.number_input("Age", min_value=18, max_value=70, value=18)
experience = st.number_input("Years of Experience", min_value=0, max_value=50, value=5)
gender = st.selectbox("Gender", ["Male", "Female"])
education = st.selectbox("Education Level", ["Bachelor", "Master", "PhD"])
job_title = st.text_input("Job Title", "Data Scientist")

# Create input DataFrame
input_data = pd.DataFrame({
    "Age": [age],
    "Years of Experience": [experience],
    "Gender": [gender],
    "Education Level": [education],
    "Job Title": [job_title]
})

# Predict
if st.button("Predict Salary"):
    prediction = model.predict(input_data)
    st.success(f"💰 Predicted Salary: ${prediction[0]:,.2f}")
