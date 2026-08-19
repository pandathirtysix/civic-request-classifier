import streamlit as st
import pickle 
# from .user_report import data_

#getting the necessary data 
# if "result" in st.session_state:
#     data_ = st.session_state["result"]
with open(r"datasets\reportsdata\database.pkl","rb") as f:
    data_ = pickle.load(f)

st.title("reports:")
st.dataframe(data_)
