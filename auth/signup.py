import streamlit as st
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from session_state.session_manager import handel_already_user,to_home_page,make_user_exist_true
from services.data_validation.json_validator import validate_email,validate_name,validate_password
from services.auth_service import if_user_exsits,user_serialization,extract_user_id_using_email


remove_header_footer = """
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}

        /* Hide the orange loading progress bar */
        div[data-testid="stDecoration"] {
            display: none !important;
        }

        /* Remove top padding to avoid white space */
        .block-container {
            padding-top: 0rem !important;
        }
    </style>
"""

heading = "<h1 id = 'create-a-account'>Create A Account</h1>"
center_the_elements = """
    <style>
        #create-a-account{
            text-align: center;
        }
        .stButton.st-emotion-cache-8atqhb.e1mlolmg0{
            display: flex;
            justify-content: center;
            align-items: center;
        }

    </style>
"""

fade_in_signup_form = """
    <style>
        h1#create-a-account,
        .stElementContainer.st-key-signup_user_name,
        .stElementContainer.st-key-signup_user_email,
        .stElementContainer.st-key-signup_user_password,
        .stElementContainer.st-key-signup_button,
        .stElementContainer.st-key-already_user_button {
            animation: fade_in 1s cubic-bezier(0.4, 0, 0.2, 1) forwards;
        }
        @keyframes fade_in {
            from {
                opacity: 0;
                transform: translateY(100px) scale(0.95);
                pointer-events: none;
            }
            to {
                opacity: 1;
                transform: translateY(0) scale(1);
                pointer-events: auto;
            }
        }
    </style>
"""

def sign_up_form():
    st.markdown(remove_header_footer,unsafe_allow_html=True)
    st.markdown(fade_in_signup_form,unsafe_allow_html=True)
    st.markdown(center_the_elements,unsafe_allow_html=True)
    st.markdown(heading,unsafe_allow_html=True)
    username = st.text_input("Name",placeholder="Jho Doe",key = "signup_user_name")
    name_flag = validate_name(username)
    useremail = st.text_input("Email",placeholder="Jho.Doe@gmail.com",key = "signup_user_email")
    email_flag = validate_email(useremail)
    userpassword = st.text_input("Password",placeholder="!hnfa@2343hgAn",key = "signup_user_password",type="password")
    password_flag = validate_password(userpassword)
   
    empty_col,signup_btn_col,already_user_btn = st.columns([1,3,1])
    with empty_col:
        st.empty()
    with signup_btn_col:
        signup_btn = st.button("Sign Up",key = "signup_button",type="secondary")
    with already_user_btn:
        st.button("Already a user?",key = "already_user_button",type = "tertiary",on_click=handel_already_user)
    if(signup_btn):
        if((validate_email and validate_name and validate_password)and(useremail and username and userpassword)):
            if(not(if_user_exsits(useremail))):
                user_serialization({
                    "username":username,
                    "useremail":useremail,
                    "userpassword":userpassword
                })
                make_user_exist_true()
                st.session_state["user_id"] = extract_user_id_using_email(useremail)
                to_home_page()
                st.rerun()
            else:
                st.error("User already exist")
        else:
            st.error("Invalid Entries")



