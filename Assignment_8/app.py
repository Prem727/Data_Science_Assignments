import streamlit as st
import pandas as pd
import joblib


# Load the trained model
model = joblib.load("diabetes_logistic_model.pkl")


# Page title
st.title("Diabetes Prediction App")

st.write(
    "Enter the patient's information below "
    "to predict the probability of diabetes."
)


# Patient inputs
pregnancies = st.number_input(
    "Pregnancies",
    min_value=0,
    max_value=20,
    value=1
)

glucose = st.number_input(
    "Glucose",
    min_value=0.0,
    max_value=250.0,
    value=120.0
)

blood_pressure = st.number_input(
    "Blood Pressure",
    min_value=0.0,
    max_value=150.0,
    value=70.0
)

skin_thickness = st.number_input(
    "Skin Thickness",
    min_value=0.0,
    max_value=100.0,
    value=20.0
)

insulin = st.number_input(
    "Insulin",
    min_value=0.0,
    max_value=900.0,
    value=80.0
)

bmi = st.number_input(
    "BMI",
    min_value=0.0,
    max_value=70.0,
    value=30.0
)

diabetes_pedigree = st.number_input(
    "Diabetes Pedigree Function",
    min_value=0.0,
    max_value=3.0,
    value=0.5
)

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=30
)


# Prediction button
if st.button("Predict"):

    input_data = pd.DataFrame({
        "Pregnancies": [pregnancies],
        "Glucose": [glucose],
        "BloodPressure": [blood_pressure],
        "SkinThickness": [skin_thickness],
        "Insulin": [insulin],
        "BMI": [bmi],
        "DiabetesPedigreeFunction": [diabetes_pedigree],
        "Age": [age]
    })


    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]


    if prediction == 1:

        st.error(
            f"Prediction: Diabetes detected\n\n"
            f"Probability: {probability:.2%}"
        )

    else:

        st.success(
            f"Prediction: No diabetes detected\n\n"
            f"Probability of diabetes: {probability:.2%}"
        )
        