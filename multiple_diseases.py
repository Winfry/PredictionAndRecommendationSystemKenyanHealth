import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

kidney_model = pickle.load(open('kidney_model.sav', 'rb'))

