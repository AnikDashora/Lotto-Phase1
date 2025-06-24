import streamlit as st
from screens.Landing_page import landing_page
if("page" not in st.session_state):
    st.session_state["page"] = "landing_page"

if(st.session_state["page"] == "landing_page"):
    landing_page()

if(__name__ == "__main__"):
    pass