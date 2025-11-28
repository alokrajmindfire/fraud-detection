import streamlit as st
from api_client import predict_api  # your function to call FastAPI

st.set_page_config(page_title="Credit Card Fraud Detection", page_icon="💳")

st.title("💳 Credit Card Fraud Detection")
st.write("Provide transaction details below:")

# Only the features expected by the backend
features = ['Amount', 'Time', 'V1', 'V2', 'V3', 'V4', 'V5']

inputs = {}

st.subheader("Transaction Inputs")

cols = st.columns(3)  # layout: 3 inputs per row
for i, feature in enumerate(features):
    col = cols[i % 3]
    inputs[feature] = col.number_input(feature, value=0.0, format="%.6f")

st.markdown("---")

if st.button("🔍 Predict Fraud"):
    with st.spinner("Analyzing transaction..."):
        # Send only the 7 features to the API
        result = predict_api(inputs)

    st.subheader("🔎 Prediction Result")
    st.write(f"**Fraudulent:** `{result['fraud']}`")
    st.write(f"**Probability:** `{result['probability']:.4f}`")

    if result["fraud"]:
        st.error("⚠️ Warning: Transaction seems fraudulent!")
    else:
        st.success("✅ Transaction looks legitimate.")
