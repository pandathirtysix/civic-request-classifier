import streamlit as st
from pipeline.model_prediction import ModelsPredictions



st.header("HOME",text_alignment="center")

st.divider()

col_1,col_2,col_3= st.columns(3)
with col_2:
    st.page_link(r"pages\user_report.py",label="Report",icon="🌐")
    st.page_link(r"pages\manage_reports.py",label="View Reports",icon="📊")

# pages  = {
#     "MENU" : [
#         st.Page("main.py",title = "HOME"),
#         st.Page(r"pages\user_report.py",title = "Report"),
#         st.Page(r"pages\manage_report.py",title = "View Reports")
#     ]
# }

# nav = st.navigation(pages)

# nav.run()