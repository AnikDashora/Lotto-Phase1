import streamlit as st
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from services.auth_service import extract_user_id_using_email,extract_user_name_by_uid
from services.product_service import categories_deserialization

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
    
    if("all_products" not in st.session_state):#this is for fast reterivatl of data
        st.session_state["all_products"] = None

    if("products_ids" not in st.session_state):#stores product ids for home page
        st.session_state["products_ids"] = None
    
    if("view_product_id" not in st.session_state):#stores the pid the product for the view in the product page
        st.session_state["view_product_id"] = None

    if("categories" not in st.session_state):#store name of the "categories" for home page
        st.session_state["categories"] = None

    if("user_cart_item" not in st.session_state):#stoes the list of dict that has pid and qty of the user cart
        st.session_state["user_cart_item"] =None
    
    if("pending_cart_item" is not st.session_state):#stores the item(product_id) if user clicks on add to cart and have not signed in
        st.session_state["pending_cart_item"] = None

    if("user_order" not in st.session_state):#stores the list of the orders user has made
        st.session_state["user_order"] = None
    
    if("pending_order_item" is not st.session_state):#stores the item if user clicks on Buy now and have not signed in
        st.session_state["pending_order_item"] = None
    

def to_home_page():
    if((st.session_state["pages"][st.session_state["page_index"]] == 6)
        or (st.session_state["pages"][st.session_state["page_index"]] == 7)):
        st.session_state["pages"].pop()
        st.session_state["page_index"] -= 1
    else:
        st.session_state["pages"].append(1)
        st.session_state["page_index"] += 1

def go_to_last_page():
    if(not(st.session_state["pages"][st.session_state["page_index"]] == 0)
        or
        (st.session_state["pages"][st.session_state["page_index"]] == 1)):
        st.session_state["pages"].pop()
        st.session_state["page_index"] -= 1


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

def save_user_cart_item_state(user_cart_items):#saves the list of the carts user has have the pids and qtys of products
    st.session_state["user_cart_item"] = user_cart_items

def save_user_orders_state(user_orders):#saves the list orders of the user has made with there price and status
    st.session_state["user_order"] = user_orders

def save_view_product_id(product_id):#saves the pid of the product after clicking on the view product
    st.session_state["view_product_id"] = product_id

def save_categories(categories):#saves the name of the categories args_type -> list of str (categories names)
    st.session_state["categories"] = categories

def save_categories_navigation(categories):#saves the categories in the product ids for home and change the home page accordingly args-> string (categoirs name)
    st.session_state["products_ids"] = categories_deserialization()[categories]

def save_products(products):#saves the ids of the products args_type -> list of str (products ids)
    st.session_state["products_ids"] = products

def save_all_products(products):
    st.session_state["all_products"] = products

def user_exist():
    st.session_state["user_exist"] = True

def user_doesnt_exist():
    st.session_state["user_exist"] = False

def check_user_exist():
    return st.session_state["user_exist"]

def give_user_name():
    return  st.session_state["user_name"]