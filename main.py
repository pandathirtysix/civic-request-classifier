import streamlit as st
from pipeline.model_prediction import ModelsPredictions



st.header("HOME",text_alignment="center")

st.divider()

col_1,col_2,col_3= st.columns(3)
with col_2:
    st.page_link("pages/user_report.py",label="Report",icon="🌐")
    st.page_link("pages/manage_reports.py",label="View Reports",icon="📊")

# Entry point for the Streamlit application.
# Renders the homepage with navigation links to lodge a report or view reports.