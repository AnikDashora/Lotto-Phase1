import streamlit as st
from screens.Landing_page import landing_page
from auth.signup import sign_up_form
from auth.login import login_form
from screens.Home import home_page
from session_state.session_manager import initialize_session_states

initialize_session_states()

if(st.session_state["page"] == "looto/screens/landing_page"):
    landing_page()
elif(st.session_state["page"] == "looto/screens/home_page"):
    home_page()
elif(st.session_state["page"] == "looto/auth/signup_page"):
    sign_up_form()
elif(st.session_state["page"] == "looto/auth/login_page"):
    login_form()

if(__name__ == "__main__"):
    pass