import streamlit as st
import joblib
import re
import numpy as np

#Uploading our models
try:
    classifier = joblib.load('model_classifier.pkl')
    regressor = joblib.load('model_regressor.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
except:
    st.error("Error: Model files not found! Make sure you ran the training code first.")
    st.stop()

#Cleaning the text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text

#Layout
st.title("AutoJudge: AI Problem Evaluator")
st.write("Paste your coding problem below to predict its Difficulty and Score.")

#Input/Output boxes
title = st.text_input("Problem Title", "Example: Sum of Array")
desc = st.text_area("Problem Description", "Given an array of integers, find the sum of its elements.")
inp_desc = st.text_area("Input Description", "The first line contains N.")
out_desc = st.text_area("Output Description", "Print the sum.")

if st.button("Predict Difficulty"):
    #Combining inputs
    full_text = f"{title} {desc} {inp_desc} {out_desc}"
    
    #Cleaning and transforming into numerical
    cleaned = clean_text(full_text)
    vectorized_text = vectorizer.transform([cleaned])
    
    #Prediction
    pred_class = classifier.predict(vectorized_text)[0]
    pred_score = regressor.predict(vectorized_text)[0]
    
    #Result
    st.success("Prediction Complete!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Difficulty Class", pred_class)
    with col2:
        st.metric("Difficulty Score", f"{pred_score:.1f}")

    st.progress(int(min(max(pred_score, 0), 100)))

print("Website code created successfully!")
