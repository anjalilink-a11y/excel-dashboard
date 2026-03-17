import streamlit as st
import pandas as pd

st.title("Excel Dashboard")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.subheader("Data Preview")
    st.write(df)

    st.subheader("Summary")
    st.write(df.describe())

    numeric_cols = df.select_dtypes(include='number').columns

    if len(numeric_cols) > 0:
        selected_col = st.selectbox("Select column", numeric_cols)
        st.line_chart(df[selected_col])
