import streamlit as st
import pandas as pd
import pickle

# Load the trained model and encoders
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('encoders.pkl', 'rb') as f:
    encoders = pickle.load(f)

st.title("Heart Disease Prediction")

# User input form
with st.form("prediction_form"):
    age = st.text_input("Age", placeholder="Enter Age")
    sex = st.selectbox("Sex", options=["Select", 'M', 'F'])
    chest_pain = st.selectbox("Chest Pain Type", options=["Select", 'ASY', 'NAP', 'ATA', 'TA'])
    resting_bp = st.text_input("Resting Blood Pressure", placeholder="Enter RestingBP")
    cholesterol = st.text_input("Cholesterol", placeholder="Enter Cholesterol")
    fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=["Select", 0, 1])
    resting_ecg = st.selectbox("Resting ECG", options=["Select", 'Normal', 'LVH', 'ST'])
    max_hr = st.text_input("Maximum Heart Rate", placeholder="Enter MaxHR")
    exercise_angina = st.selectbox("Exercise Induced Angina", options=["Select", 'Y', 'N'])
    oldpeak = st.text_input("Oldpeak", placeholder="Enter Oldpeak (e.g. 1.5)")
    st_slope = st.selectbox("ST Slope", options=["Select", 'Flat', 'Up', 'Down'])


    submitted = st.form_submit_button("Predict")

    if submitted:
        input_dict = {
            'Age': age,
            'Sex': sex,
            'ChestPainType': chest_pain,
            'RestingBP': resting_bp,
            'Cholesterol': cholesterol,
            'FastingBS': fasting_bs,
            'RestingECG': resting_ecg,
            'MaxHR': max_hr,
            'ExerciseAngina': exercise_angina,
            'Oldpeak': oldpeak,
            'ST_Slope': st_slope
        }

        df_input = pd.DataFrame([input_dict])

        # Apply encoders
        for col in encoders:
            if col in df_input.columns:
                df_input[col] = encoders[col].transform(df_input[col])

        # Make prediction
        prediction = model.predict(df_input)
        result = "Heart Disease Detected" if prediction[0] == 1 else "No Heart Disease"
        st.success(f"Prediction: {result}")
