import streamlit as st
import pickle
import numpy as np

# Load the saved Random Forest model
model = pickle.load(open('classifyModel.pkl', 'rb'))

# Streamlit app with custom HTML and CSS
st.markdown("""
    <style>
    body {
        background: linear-gradient(to bottom, #fff700, #ffe066);
        font-family: Arial, sans-serif;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #43a049;
    }
    .header {
        background-color: #005f99;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        color: white;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .header h1 {
        font-size: 2.5rem;
        color:#ffffff;
    }
    .header p {
        font-size: 1rem;
        color: #d0e7f9;
    }
    .output-box {
        background-color: #282c34;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .output-box h3 {
        color: #ffffff;
    }
    .output-box span {
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# Header section
st.markdown("""
    <div class="header">
        <h1>🩺 Blood_Pressure_Abnormality Classifier</h1>
        <p>Analyze Blood_Pressure_Abnormality based on its characteristics</p>
    </div>
""", unsafe_allow_html=True)

# Input fields in rows
st.markdown("### Enter Required Parameters Below")

col1, col2 = st.columns(2)
with col1:
    Patient_Number = st.number_input("Patient_Number", min_value=0.0, value=1574.00, step=0.1)
    Level_of_Hemoglobin = st.number_input("Level_of_Hemoglobin", value=9.74, step=0.1)
    Genetic_Pedigree_Coefficient = st.number_input("Genetic_Pedigree_Coefficient", value=0.96, step=1.0)

with col2:
    Age = st.number_input("Age", value=57.00, step=0.1)
    BMI = st.number_input("BMI", value=41.00, step=0.1)
    Sex  = st.number_input("Sex ", value=0.00, step=0.1)

col3, col4 = st.columns(2)
with col3:
    Smoking = st.number_input("Smoking", value=1.00, step=0.1)
    Physical_activity = st.number_input("Physical_activity", value=30571.00, step=0.1)
    salt_content_in_the_diet = st.number_input("salt_content_in_the_diet", value=39134.00, step=0.1)

with col4:
    alcohol_consumption_per_day = st.number_input("alcohol_consumption_per_day", value=388.00, step=0.1)
    Level_of_Stress = st.number_input("Level_of_Stress", value=1.00, step=0.1)
    

col5, col6 = st.columns(2)
with col5:
    Chronic_kidney_disease = st.number_input("Chronic_kidney_disease", value=1.00, step=0.1)
with col6:
    Adrenal_and_thyroid_disorders = st.number_input("Adrenal_and_thyroid_disorders", value=0.00, step=0.1)

# Combine inputs into a single array
input_data = np.array([Patient_Number, Level_of_Hemoglobin, Genetic_Pedigree_Coefficient, Age, BMI, Sex, 
                       Smoking, Physical_activity, salt_content_in_the_diet,alcohol_consumption_per_day,Level_of_Stress,Chronic_kidney_disease,Adrenal_and_thyroid_disorders  ]).reshape(1, -1)

# Predict button
if st.button("Predict Blood_Pressure_Abnormality"):
    prediction = model.predict(input_data)
    Blood_Pressure = "SAFE" if prediction[0] == 1 else "NOT SAFE"
    
    # Display result in a styled box
    st.markdown(f"""
        <div class="output-box">
            <h3>The Blood_Pressure_Abnormality is: <span>{Blood_Pressure}</span></h3>
        </div>
    """, unsafe_allow_html=True)
