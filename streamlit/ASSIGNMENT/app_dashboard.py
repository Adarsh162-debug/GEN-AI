from optparse import Values
from unicodedata import category

import streamlit as st

st.title("dashboard")
st.write("simple sales dashboard")
month=st.selectbox("months name is",["jan","feb","march","april"])
sales={"jan":1200,
       "feb":1500,"march":900,"april":2000
       }
st.write(f"your sale is:{sales[month]}")
st.bar_chart(sales)
