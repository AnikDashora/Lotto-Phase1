import streamlit as st

def initialize_session_states():
    if("page" not in st.session_state):
        st.session_state["page"] = "looto/screens/landing_page"
    
    if("user_exist" not in st.session_state):
        st.session_state["user_exist"] = False
    
    if("user_email" not in st.session_state):
        st.session_state["user_email"] = None
    
    if("user_id" not in st.session_state):
        st.session_state["user_id"] = None
    
    if("product_id" not in st.session_state):
        st.session_state["product_id"] =None

    #this is for testing
    if("cart_qty" not in st.session_state):
        st.session_state["cart_qty"] = 0

def handel_already_user():
    st.session_state["page"] = "looto/auth/login_page"
    st.session_state["user_exist"] = True

def handel_new_user():
    st.session_state["page"] = "looto/auth/signup_page"
    st.session_state["user_exist"] = False

def to_home_page():
    st.session_state["page"] = "looto/screens/home_page"

def to_signup_page():
    st.session_state["page"] = "looto/auth/signup_page"

def to_login_page():
    st.session_state["page"] = "looto/auth/login_page"

def to_product_page():
    st.session_state["page"] = "looto/screens/product_page"

def make_user_exist_true():
    st.session_state["user_exist"] = True

def make_user_exist_False():
    st.session_state["user_exist"] = False

#this is for testing

def add_to_cart():
    st.session_state["cart_qty"] += 1

def remove_from_cart():
    st.session_state["cart_qty"] -= 1