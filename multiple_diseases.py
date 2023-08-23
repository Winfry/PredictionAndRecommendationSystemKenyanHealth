import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from bs4 import BeautifulSoup
import requests
import pandas as pd 
import numpy as np
import random

#loading the saved models

kidney_model = pickle.load(open('kidney_model.sav', 'rb'))

#SIDEBAR FOR NAVIGATION
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Chronic Kidney Prediction',
                            'Cancer Prediction',
                            'Heart Prediction ',
                            'Diabetes Prediction'],

                            icons=['kidney','activity','heart','person'],
                            default_index=0)


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
           
            

            