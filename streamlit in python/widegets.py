import streamlit as st
import numpy as np
import pandas as pd
st.title("WELCOME")
name=st.text_input("Enter your name: ")
if name:
    f"Hello,{name}"

age=st.slider("Choose your age: ",0,100,25)
options=["c","python","java"]
subject=st.selectbox("choose your subject",options)
st.write(f"you selected{subject}")
data={
    "name":["m","a","n"],
    "age":[10,20,30],
    "subject":["c","p","j"]
}
df=pd.DataFrame(data)
st.write(df)
df.to_csv("sampledata.csv")
upload_file=st.file_uploader("choose csv file",type="csv")
if upload_file is not None:
    df=pd.read_csv(upload_file)
    st.write(df)