import streamlit as st
import pandas as pd

# Create a Streamlit app
st.title("CSV File Uploader")

# Create a file uploader widget
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Check if a file was uploaded
if uploaded_file is not None:
    # Read the uploaded CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the DataFrame
    st.write("Uploaded CSV Data:")
    st.write(df)

