import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image


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
    image=Image.open('kidinfo.png')
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
        RedBloodCells = st.selectbox('RedBloodCells: ', ["normal", "abnormal"] )    

    with col1:
        BloodGlucoseRandom = st.number_input('BloodGlucoseRandom', max_value=490)

    with col2:
        BloodUrea= st.number_input('BloodUrea', max_value=400)   

    with col3:
        Bacteria = st.selectbox('Bacteria: ', ["notpresent", "present"])   

    with col1:
        Appetite = st.selectbox('Appetite: ', ["good", "bad"]) 

    with col2:
        Haemoglobin = st.number_input('Haemoglobin:', max_value=18)    
            
    with col3:
        Diabetes = st.selectbox('Diabetes: ', ["no", "yes"])
        
    with col1:
        RedBloddCellCount = st.number_input('RedBloodCellCount', max_value=100)

    with col2:
        WhiteBloodCellCount = st.number_input('WhiteBloodCellCount', max_value=100)                            