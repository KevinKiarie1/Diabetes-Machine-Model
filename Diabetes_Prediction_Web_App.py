# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 11:35:39 2022

@author: kevin
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/kevin/trained_model.sav', 'rb'))

def diabetes_prediction(input_data):
    
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0] == 0):
        return 'the person is not diabetic'
    else:
        return'the person is diabetic'
        
def main():        
    
    st.title('diabetes_prediction')
    Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    
    Pregnancies = st.text_input('Number of pregnancies')
    glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood Pressue level')
    SkinThickness = st.text_input('Skin thickness')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI level')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function level')
    Age = st.text_input('Age')
    
    diagnosis = ''
    
    if st.button('Test Results'):
       diabetes = diabetes_prediction([Pregnancies, glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    
    st.success(diagnosis)
    
if __name__== '_main_':    
    main()
    
    
    
    
    
    
    