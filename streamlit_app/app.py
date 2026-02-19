import sys
import os
import streamlit as st
import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


st.title("Customer Segmentation App")
st.write("Enter customer RFM values:")

recency = st.number_input("Recency", min_value=1, step=1)
frequency = st.number_input("Frequency", min_value=1, step=1)
monetary = st.number_input("Monetary", min_value=0.0,step=1.0)

if st.button("Predict Segment"):
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={
            "Recency": recency,
            "Frequency": frequency,
            "Monetary": monetary
        }
    )

    result = response.json()

    st.success(f"Predicted Segment: {result['segment']}")








