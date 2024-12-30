import pickle
import os
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from bs4 import BeautifulSoup
import requests
import pandas as pd 
import numpy as np
import random
import joblib
import warnings
# Suppress warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))


#loading the saved models
try:
    # Kidney model
    kidney_model_path = os.path.join(working_dir, "kidney_model.sav")
    if not os.path.exists(kidney_model_path):
        st.error("Kidney model file not found! Ensure 'kidney_model.sav' is in the correct directory.")
        kidney_model = None
    else:
        kidney_model = pickle.load(open(kidney_model_path, "rb"))
        st.success("Kidney model loaded successfully.")
    
    # Heart model
    heart_model_path = os.path.join(working_dir, "heart_model.sav")
    if not os.path.exists(heart_model_path):
        st.error("Heart model file not found! Ensure 'heart_model.sav' is in the correct directory.")
        heart_model = None
    else:
        heart_model = pickle.load(open(heart_model_path, "rb"))
        st.success("Heart model loaded successfully.")
except Exception as e:
    st.error(f"An error occurred while loading models: {e}")

#SIDEBAR FOR NAVIGATION
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Chronic Kidney Prediction',
                            'Cancer Prediction',
                            'Heart Prediction ',
                            'Diabetes Prediction'],

                            icons=['pulse','activity','heart','person'],
                            default_index=0)

st.write(f"Selected Page: {selected}")
st.write(f"Model Loaded: {heart_model is not None}")

#CHRONIC KIDNEY PREDICTION PAGE 
if (selected == 'Chronic Kidney Prediction'): 

    #Page Title
    image=Image.open('ki.jpg')
    st.image(image)
    st.title('Chronic Kidney Disease Prediction Using Machine Learning Algorithm')   
    st.markdown('The kidneys are two bean-shaped organs, each about the size of a fist.They are located just below the rib cage, one on each side of your spine.') 
    st.markdown('They work hard to remove wastes, toxins, and excess fluid. They also help control blood pressure, stimulate production of red blood cells, keep your bones healthy, and regulate blood chemicals that are essential to life.Kidneys that function properly are critical for maintaining good health, however, more than one in seven Kenyan adults are estimated to have chronic kidney disease (CKD).')
    st.markdown('In this webapp ,the project ideally is to predict if one has a Chronic Kidney Disease based on these important health factors and parameters:  ')

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.number_input('Age', max_value=90)

    with col2:
        BloodPressure =  st.number_input('BloodPressure', max_value=180)

    with col3:
        SpecificGravity = st.number_input('SpecificGravity', max_value=1.025)

    with col1:
        Albumin = st.number_input('Albumin', max_value=5.00)

    with col2:
        Sugar = st.number_input('Sugar', max_value=5.00) 

    with col3:
        BloodGlucoseRandom = st.number_input('BloodGlucoseRandom', max_value=490)

    with col1:
        BloodUrea= st.number_input('BloodUrea', max_value=400)   

    with col2:
        Potassium = st.number_input('Potassium: ', max_value=47) 

    with col3:
        Haemoglobin = st.number_input('Haemoglobin:', max_value=18)    
            
    with col1:
        Sodium = st.number_input('Sodium: ', max_value=163)
        
    with col2:
        RedBloddCellCount = st.number_input('RedBloodCellCount', max_value=100)

    with col3:
        WhiteBloodCellCount = st.number_input('WhiteBloodCellCount', max_value=100) 

    with col1:
        SerumCreatinine = st.number_input('SerumCreatinine: ', max_value=76)      

    # code for Prediction
    Kidneydisease = ''

    if st.button("Kidney Test Result"):
        kidney_prediction = kidney_model.predict(
            [[Age, BloodPressure, SpecificGravity, Albumin, Sugar, BloodGlucoseRandom, BloodUrea, SerumCreatinine, Sodium, Potassium, Haemoglobin]]
        )                             

        if(kidney_prediction[0] == 1):
            Kidneydisease = 'Congratulations! Predictions show you do not have a Kidney Disease.Keep on Maintaining Healthy Kidneys!'
            st.success(Kidneydisease)
            image=Image.open('nockd.png')
            st.image(image)

        else:
            Kidneydisease = 'The Predictions show there is chances of A Chronic Kidney Disease'
            st.error(Kidneydisease)
            st.markdown("Now that you are aware of the likelihood of a chronic kidney disease,No need to worry. Here is a list of the Renal Facilities In Kenya That Offer Kidney Check Up Services: ")
            image=Image.open('poster.jpeg')
            st.image(image)
            
            #Loading the Hospitals  
            #Applying the data
           
            


# Heart Disease Prediction Page
if selected == 'Heart Prediction':

    # Page title
    st.title('Heart Disease Prediction using ML')

    # Input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age (e.g., 25)', value="25")

    with col2:
        sex = st.text_input('Sex (0 = Female, 1 = Male)', value="1")

    with col3:
        cp = st.text_input('Chest Pain Type (0-3)', value="0")

    with col1:
        trestbps = st.text_input('Resting Blood Pressure (e.g., 120)', value="120")

    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl (e.g., 200)', value="200")

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (0 or 1)', value="0")

    with col1:
        restecg = st.text_input('Resting ECG Results (0-2)', value="0")

    with col2:
        thalach = st.text_input('Max Heart Rate Achieved (e.g., 150)', value="150")

    with col3:
        exang = st.text_input('Exercise Induced Angina (0 or 1)', value="0")

    with col1:
        oldpeak = st.text_input('ST Depression Induced by Exercise (e.g., 1.0)', value="1.0")

    with col2:
        slope = st.text_input('Slope of the Peak Exercise ST Segment (0-2)', value="0")

    with col3:
        ca = st.text_input('Major Vessels Colored by Fluoroscopy (0-3)', value="0")

    with col1:
        thal = st.text_input('Thal (0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect)', value="0")

    # Prediction
    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        try:
            # Convert inputs to floats
            user_input = [float(age), float(sex), float(cp), float(trestbps), float(chol), 
                          float(fbs), float(restecg), float(thalach), float(exang), 
                          float(oldpeak), float(slope), float(ca), float(thal)]
            
            # Make prediction
            heart_prediction = heart_model.predict([user_input])

            # Display result
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'

            st.success(heart_diagnosis)
        
        except ValueError:
            st.error("Please enter valid numeric values for all inputs.")

            