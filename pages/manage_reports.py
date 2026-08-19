import streamlit as st
import pickle 

# Retrieve and load existing complaint reports from the serialized pickle database.
with open("datasets/reportsdata/database.pkl","rb") as f:
    data_ = pickle.load(f)

# Display the complaint reports in an interactive Streamlit data frame.
st.title("reports:")
st.dataframe(data_)
