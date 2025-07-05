import streamlit as st

import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from session_state.session_manager import to_home_page,handel_new_user,user_exist,save_user_state,save_user_orders_state,save_user_cart_item_state
from services.data_validation.json_validator import validate_email
from services.auth_service import if_user_exsits,verify_user
from services.cart_service import read_user_cart
from services.ordering_service import read_user_order
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
center_the_elements = """
    <style>
        h2#login{
            text-align: center;
            font-size: 2em;           
            font-weight: bold;        
            margin-top: 0.67em;       
            margin-bottom: 0.67em;    
            line-height: 1.2;         
            letter-spacing: normal;   
            color: inherit;            
            font-family: inherit; 
        }
        .stButton.st-emotion-cache-8atqhb.e1mlolmg0{
            display: flex;
            justify-content: center;
            align-items: center;
        }

    </style>
"""

heading = "<h2 id = 'login' style = font-size:2em;>Login</h2>"

fade_in_login_form = """
    <style>
        h2#login,
        .stElementContainer.st-key-login_user_email,
        .stElementContainer.st-key-login_user_password,
        .stElementContainer.st-key-login_button,
        .stElementContainer.st-key-new_user_button{
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

def login_form():

    st.markdown(remove_header_footer,unsafe_allow_html=True)
    st.markdown(fade_in_login_form,unsafe_allow_html=True)
    st.markdown(center_the_elements,unsafe_allow_html=True)
    st.markdown(heading,unsafe_allow_html=True)

    useremail = st.text_input("Email",placeholder="Your Email",key = "login_user_email")
    email_flag = validate_email(useremail)
    userpassword = st.text_input("Password",placeholder="Your Password",type="password",key = "login_user_password")
    empty_col,login_btn_col,new_user_btn = st.columns([1,3,1])
    with empty_col:
        st.empty()
    with login_btn_col:
        login_btn = st.button("Login",type="secondary",key = "login_button")
    with new_user_btn:
        st.button("New User?",type="tertiary",key = "new_user_button",on_click=handel_new_user)
    if(login_btn):
        if(email_flag and useremail and if_user_exsits(useremail)):
            if(userpassword):
                if(verify_user(useremail,userpassword)):
                    save_user_state(useremail)
                    save_user_cart_item_state(read_user_cart(st.session_state["user_id"])["cart_items"])
                    save_user_orders_state(read_user_order(st.session_state["user_id"])["orders"])
                    user_exist()
                    to_home_page()
                    st.rerun()
                else:
                    st.error("Invalid Username or Password")
            else:
                st.error("Invalid Entries")
        else:
            st.error("User doesn't Exist")
