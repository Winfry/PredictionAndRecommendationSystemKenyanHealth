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

heart_model = pickle.load(open("heart_model.sav",'rb'))
