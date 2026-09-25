import streamlit as st


st.write("hello world")
st.title("hello streamlit")
st.write("this is my first streamlit app")
st.header("welcome to streamlit")
st.subheader("this is a subheader")
st.text("this is a  plain text")


## Buttons, checkboxes and sliders

if st.button('click me!'):
    st.write("button clicked !")

agree=st.checkbox("i agree")
if agree:
    st.write("you agreed!")    

level=st.slider("select a level :",1,10)
st.write(f"selceted level :{level}")

uploaded_files=st.file_uploader("upload a file",type=['csv','txt'])

if uploaded_files is not None:
    df=pd.read_csv


