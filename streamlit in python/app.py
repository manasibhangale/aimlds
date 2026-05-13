import streamlit as st
import pandas as pd
import numpy as np
st.write("welcome to streamlit")
df=pd.DataFrame(
    {
        "first_column":[10,20,30],
        "second_column":[40,50,60]
    }
)
st.write("here is the dataframe")
st.write(df)
chart=pd.DataFrame(
    np.random.randn(20,3),columns=["m","n","o"]
)
st.line_chart(chart)
