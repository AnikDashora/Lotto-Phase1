import streamlit as st
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from services.data_validation.json_validator import *
from services.auth_service import user_serialization,if_user_exsits
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
                .stButton.st-emotion-cache-8atqhb.e1mlolmg0{
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }
                h1#create-an-account{
                    text-align: center;
                }
                h1#login {
                    display:none;
                    text-align: center;
                }
                
            </style>
        """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    st.title("Create An Account")
    st.title("Login")
    
    username = st.text_input("Name",placeholder="eg: Jho Doe")
    name_flag = validate_name(username)
    useremail = st.text_input("Email",placeholder="eg: Jho.doe@gmail.com")
    email_flag = validate_email(useremail)
    userpassword = st.text_input("Password",placeholder="eg: Qu@314Pra#th",type="password")
    password_flag = validate_password(userpassword)
    st.button("SIGN UP",on_click=lambda:user_serialization(user_data))

    # Dynamically toggle between "Create An Account" and "Login" titles based on user existence
    if useremail and if_user_exsits(useremail):
        # User exists, show Login title and hide Create An Account
        st.markdown("""
            <style>
                h1#create-an-account { display: none; }
                h1#login {
                    display: block;
                    animation: fade-in 0.5s ease;
                }
                @keyframes fade-in {
                    from { opacity: 0; transform: translateY(15px);}
                    to { opacity: 1; transform: translateY(0);}
                }
            </style>
        """, unsafe_allow_html=True)
    else:
        # User does not exist, show Create An Account and hide Login
        st.markdown("""
            <style>
                h1#login { display: none; }
                h1#create-an-account {
                    display: block;
                    animation: fade-in 0.5s ease;
                }
                @keyframes fade-in {
                    from { opacity: 0; transform: translateY(20px);}
                    to { opacity: 1; transform: translateY(0);}
                }
            </style>
        """, unsafe_allow_html=True)
    #new user
    if(name_flag and email_flag and password_flag):
        st.markdown("""
            <style>
                button.st-emotion-cache-1rwb540.e1e4lema2 {
                    pointer-events: auto;
                    transition: opacity 1s;
                    opacity: 1;
                }
            </style>
        """,unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
                button.st-emotion-cache-1rwb540.e1e4lema2 {
                    pointer-events: none;
                    transition: opacity 1s;
                    opacity: 0;
                }
            </style>
        """,unsafe_allow_html=True)

    
    user_data = {
        "username":username,
        "useremail":useremail,
        "userpassword":userpassword,
    }
    

sign_up_page()