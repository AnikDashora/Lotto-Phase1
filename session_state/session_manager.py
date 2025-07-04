import streamlit as st
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from services.auth_service import extract_user_id_using_email,extract_user_name_by_uid

PAGES = ("looto/screens/landing_page",#0
         "looto/screens/home_page",#1
         "looto/screens/product_page",#2
         "looto/screens/cart_page",#3
         "looto/screens/order_page",#4
         "looto/screens/order_status_page",#5
         "looto/auth/signup_page",#6
         "looto/auth/login_page"#7
        )
def initialize_session_states():
    if("pages" not in st.session_state):
        st.session_state["pages"] = [0]
    
    if("page_index" not in st.session_state):
        st.session_state["page_index"] = 0

    if("user_exist" not in st.session_state):
        st.session_state["user_exist"] = False
    
    if("user_id" not in st.session_state):
        st.session_state["user_id"] = None
    
    if("user_name" not in st.session_state):
        st.session_state["user_name"] = None
    
    if("user_email" not in st.session_state):
        st.session_state["user_email"] = None
    
    if("products" not in st.session_state):
        st.session_state["products"] = None

    if("user_cart_item" not in st.session_state):
        st.session_state["user_cart_item"] =None

    if("user_order" not in st.session_state):
        st.session_state["user_order"] = None
    

def to_home_page():
    if((st.session_state["pages"][st.session_state["page_index"]] == 6)
        or 
        (st.session_state["pages"][st.session_state["page_index"]] == 7)):
        st.session_state["pages"].pop()
        st.session_state["page_index"] -= 1
    else:
        st.session_state["pages"].append(1)
        st.session_state["page_index"] += 1

def to_signup_page():
    st.session_state["pages"].append(6)
    st.session_state["page_index"] += 1

def handel_already_a_user():
    st.session_state["pages"][-1] = 7

def handel_new_user():
    st.session_state["pages"][-1] = 6

def save_user_state(useremail):
    st.session_state["user_id"] = extract_user_id_using_email(useremail)
    st.session_state["user_email"] = useremail
    st.session_state["user_name"] = extract_user_name_by_uid(st.session_state["user_id"])

def save_user_cart_item_state(user_cart_items):
    st.session_state["user_cart_item"] = user_cart_items

def save_user_orders_state(user_orders):
    st.session_state["user_order"] = user_orders

def user_exist():
    st.session_state["user_exist"] = True

def user_doesnt_exist():
    st.session_state["user_exist"] = False