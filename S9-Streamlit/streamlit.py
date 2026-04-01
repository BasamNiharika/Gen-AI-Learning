# What is streamlit ?
# Streamlit is an open source framework for ML and DS projects. It allows you to create beautiful web application for your machine learning
# and data science projects with simple python scripts.

import streamlit as st
import pandas as pd
import numpy as np

# Creating title for an application using streamlit
st.title("Hello Streamlit")

# Display a simple text
st.write("This is a simple text")

# create a simple dataframe
df = pd.DataFrame({
    'first column':[1, 2, 3, 4],
    'second column':[10, 20, 30, 40]
})

# Displaying dataframe
st.write("Here is the data frame")
st.write(df)

# create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns = ['a','b','c']
)

st.line_chart(chart_data)