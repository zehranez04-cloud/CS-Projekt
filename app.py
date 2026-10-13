import streamlit as st
from Feature_01 import return_even

original_list =[i for i in range(10)]
even_list = return_even(original_list)

st.write("Hello")
st.write("Das ist der Test für die Streamlit App")

st.header ("Test für die Streamlit App")
st.subheader ("untertitel")

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
tab1.write("Inhalt von Tab 1")
tab2.write("Inhalt von Tab 2")

st.button("Click!")

st.write(even_list)

# webseite:testingcs.streamlit.app

