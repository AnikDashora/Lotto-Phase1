import streamlit as st
from screens.Landing_page import landing_page
from auth.signup import sign_up_page
if("page" not in st.session_state):
    st.session_state["page"] = "landing_page"

if(st.session_state["page"] == "landing_page"):
    landing_page()
elif(st.session_state["page"] == "auth_page"):
    sign_up_page()

if(__name__ == "__main__"):
    pass