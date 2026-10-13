import streamlit as st
from ui import badge, css_laden, diagram_stil

st.title("Going Concern")
st.subheader("Test if your company is a going concern")

st.text("Follow the instructions below to test if your company is a going concern. Please fill in the required information and click the 'Submit' button to see the results.")


tab1, tab2, tab3, tab4, tab5 = st.tabs(["Import Data", "Qualitative Questions", "Merging Data", "Liquidity Planer", "Result"])
tab1.write("Put in your balance sheet, income statement and cash flow statement in the correct format. You can download the template below.")
tab2.write("Answer the qualitative questions about your company with yes or no via button. These questions will help us assess the going concern status of your company.")
tab3.write("The data from the previous tabs will be merged and analyzed to determine the going concern status of your company.")
tab4.write("Use the liquidity planner to assess your company's liquidity position and plan for future cash needs. This tool will help you identify potential liquidity issues and take proactive measures to address them.")
tab5.write("The results of the going concern assessment will be displayed here. You will receive a summary of the analysis, including any potential risks or concerns identified during the assessment process. Based on the results, you can take appropriate actions to address any issues and ensure the long-term viability of your company.")

st.set_page_config(page_title="Going Concern", page_icon=":bar_chart:", layout="wide", initial_sidebar_state="expanded")
badge("Going Concern")



