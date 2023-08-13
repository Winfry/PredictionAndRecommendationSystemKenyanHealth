import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

kidney_model = pickle.load(open('kidney_model.sav', 'rb'))

#SIDEBAR FOR NAVIGATION
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Chronic Kidney Prediction',
                            'Cancer Prediction',
                            'Heart Prediction ',
                            'Diabetes Prediction'],

                            icons=['activity','heart','person'],
                            default_index=0)


#CHRONIC KIDNEY PREDICTION PAGE 
if (selected == 'Chronic Kidney Prediction'): 

    #Page Title
    st.title('Chronic Kidney Disease Prediction Using Machine Learning')             