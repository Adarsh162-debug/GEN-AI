import streamlit as st

product_name=st.sidebar.text_input("enetr your product name")


category=st.sidebar.selectbox("select category",["mobile","laptop","car","watch"])

price=st.sidebar.number_input("select the price")

btn=st.sidebar.button('add product')
st.success("The product details are:")
st.write(f"Product Name: {product_name}")
st.write(f"Category: {category}")
st.write(f"Price: ₹{price}")

