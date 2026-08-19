import streamlit as st
from pipeline.model_prediction import ModelsPredictions
import pandas as pd
import pickle

def start_the_program(text):
    try:
        mp = ModelsPredictions()

        intent = mp.model_intent_prediction(text)
        department = mp.model_department_prediction(text)
        severity = mp.model_severity_prediction(text)
        urgency = mp.model_urgency_prediction(text)
        category = mp.model_category_prediction(text)

        return intent, department, severity, urgency, category

    except Exception as e:
        return f"error {e}"

    

def data_packer(name, street, phone_no, text, result):

    with open(r"X:\PROGRAMS\NLP PROJECT\datasets\reportsdata\database.pkl","rb") as f:
        data_ = pickle.load(f)

    intent, department, severity, urgency, category = result

    data = {
        "name": [name],
        "street": [street],
        "phone Num": [phone_no],
        "raw_report" : [text],
        "intent": [intent[0]],
        "department": [department[0]],
        "severity": [severity[0]],
        "urgency": [urgency[0]],
        "category": [category[0]]
    }

    data = pd.DataFrame(data)
    data_ = pd.concat([data_, data], ignore_index=True)

    with open(
        r"X:\PROGRAMS\NLP PROJECT\datasets\reportsdata\database.pkl",
        "wb"
    ) as f:
        pickle.dump(data_, f)

    return pd.DataFrame(data_)    




st.title("Public Complaint System")


name = st.text_input("Enter your name")
street = st.text_input("enter you street")
phone_no = st.text_input("enter you mobile Number")
text = st.text_input("Register your problem")




if st.button("Submit", key="submit_button") and text:

    result = start_the_program(text)

    if isinstance(result, str):
        st.error(result)
    else:
        data = data_packer(name, street, phone_no, text, result)
        st.session_state["result"] = data
        st.success("Thank you! We'll try to solve your problem as soon as possible.")

