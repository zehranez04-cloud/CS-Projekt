import streamlit as st

st.write ("Hello!")
st.title("My First Streamlit App")
st.subheader("This is a subheader")

st.text("This is a simple text")

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
tab1.write("This is content for Tab 1")
tab2.write("This is content for Tab 2")

