import streamlit as st
from screens.Landing_page import landing_page
from screens.Home import home_page
from auth.signup import sign_up_form
from auth.login import login_form
from screens.Product import product_page
from session_state.session_manager import initialize_session_states

initialize_session_states()

if(st.session_state["pages"][st.session_state["page_index"]] == 0):
    landing_page()
elif(st.session_state["pages"][st.session_state["page_index"]] == 1):
    home_page()
elif(st.session_state["pages"][st.session_state["page_index"]] == 2):
    product_page()
elif(st.session_state["pages"][st.session_state["page_index"]] == 6):
    sign_up_form()
elif(st.session_state["pages"][st.session_state["page_index"]] == 7):
    login_form()
if(__name__ == "__main__"):
    pass