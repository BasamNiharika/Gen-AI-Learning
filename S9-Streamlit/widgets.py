import streamlit as st
import pandas as pd

st.title("Streamlit Widgets")

# Text input box
name = st.text_input("Enter your name:")

if name: 
    st.write(f"Hello, {name}")

# Slider
age = st.slider("Select your age:",0,100,25)

st.write(f"your age is {age}")

# select Box
options = ["Java","C++","Python","Javascript"]
choice = st.selectbox("Choose your favorite language",options)
st.write(f"You selected {choice}")

# displaying data in tabular format using dataframe
data = {
    "Name":["Jane","John", "Jake","Jill"],
    "Age":[28,24,35,40],
    "City":["New york","Los Angels","Chicago","Houston"]
}

df = pd.DataFrame(data)
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file",type ="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)


# for exploring more about streamlit explore streamlit.io
