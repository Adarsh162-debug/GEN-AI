import streamlit as st

price=st.number_input("enter thr input price")
level=st.slider(" enter your discount percent level",0,50)
st.write(f"your discount percetage is {level}")

btn=st.button('click for discount')
if btn:
 discount=price*level/100
 final_price=price-discount
 st.success(f"your price after discount is{final_price}")
