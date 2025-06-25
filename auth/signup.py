import streamlit as st
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from services.data_validation.json_validator import *
from services.auth_service import user_serialization

def sign_up_page():
    hide_streamlit_style = """
            <style>
                /* Hide Streamlit header, main menu, and footer */
                #MainMenu {visibility: hidden;}
                header {visibility: hidden;}
                footer {visibility: hidden;}

                /* Hide the orange loading progress bar */
                div[data-testid="stDecoration"] {
                    display: none;
                }

                /* Optional: remove top padding to avoid white space */
                div.block-container {
                    padding-top: 0rem;
                }
                .stButton.st-emotion-cache-8atqhb.e1mlolmg0 {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                } 
                h1#create-an-account {
                    text-align: center;
                }
                
            </style>
        """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    st.title("Create An Account")

    username = st.text_input("Name",placeholder="eg: Jho Doe")
    name_flag = validate_name(username)
    useremail = st.text_input("Email",placeholder="eg: Jho.doe@gmail.com")
    email_flag = validate_email(useremail)
    userpassword = st.text_input("Password",placeholder="eg: Qu@314Pra#th",type="password")
    password_flag = validate_password(userpassword)
    st.button("SIGN UP",on_click=lambda:user_serialization(user_data))
    
    user_data = {
        "username":username,
        "useremail":useremail,
        "userpassword":userpassword,
    }
    

sign_up_page()