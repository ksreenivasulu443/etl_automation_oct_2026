import streamlit as st
import pandas as pd

# Set page title
st.set_page_config(page_title="ETL Automation Labs")

# Display application title
st.title("ETL Automation Labs")

st.subheader("CSV File Reader")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# Check whether a file is uploaded
if uploaded_file is not None:

    # Read CSV file using Pandas
    df = pd.read_csv(uploaded_file)

    # Display CSV content
    st.dataframe(df)