import streamlit as st
import requests
from api_client import predict_api

st.title("💳 Credit Card Fraud Detection")

st.write("Enter transaction details:")

inputs = {}
for feature in ['Time','Amount'] + [f"V{i}" for i in range(1,29)]:
    inputs[feature] = st.number_input(feature, value=0.0)

if st.button("Predict"):
    result = predict_api(inputs)
    st.write("### Result")
    st.json(result)
