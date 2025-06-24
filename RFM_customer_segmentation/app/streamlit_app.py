import streamlit as st
import pandas as pd

df = pd.read_csv("data/rfm_with_segments.csv")

st.title("Customer Segmentation Viewer")

customer_id = st.text_input("Enter Customer ID:")

if customer_id:
    customer_data = df[df['CustomerID'].astype(str) == customer_id]
    if not customer_data.empty:
        st.write("### Customer RFM Details and Segment:")
        st.write(customer_data[['CustomerID', 'Recency', 'Frequency', 'Monetary', 'R_score', 'F_score', 'M_score', 'RFM_Score', 'Segment']])
    else:
        st.warning("Customer ID not found.")
