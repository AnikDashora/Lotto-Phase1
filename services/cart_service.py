import json
import os
import sys
import random
import streamlit as st
CART_DATA_FILE = "D:\\Lotto-Phase1\\data\\cart.json"

def check_file_exist():
    return os.path.isfile(CART_DATA_FILE)

def reading_cart_file():
    if(not check_file_exist()):
        raise FileNotFoundError(f"Cart file doesnt exist at {CART_DATA_FILE}")
    try:
        with open(CART_DATA_FILE, "r") as file:
            carts = json.load(file)
            if not isinstance(carts, list):
               carts = []
    except (json.JSONDecodeError, FileNotFoundError):
            carts = []
    return carts

def writing_cart_file(carts):#carts are all the carts in the databases not only single user cart
    if(not check_file_exist()):
        raise FileNotFoundError(f"Cart file doesnt exist at {CART_DATA_FILE}")
    with open(CART_DATA_FILE, "w") as file:
        json.dump(carts, file, indent=4)

def create_user_cart(user_id):
    user_cart = {
        "user_id":user_id,
        "cart_items":[]
    }
    carts = reading_cart_file()
    carts.append(user_cart)
    writing_cart_file(carts)

def read_user_cart(user_id):#this will return the list of cart_items according to the user id 
    carts = reading_cart_file()
    if(len(carts) == 0):
        return None
    user_index = int(user_id[1:])-1
    return carts[user_index]["cart_items"] 

def find_product_quantity_in_user_cart(product_id,user_cart_state):#args -> pid,session state of user cart
    """finds the item in cart and return index and
        if the item in not in the then it means the
        product has zero qty and doesnt exist in cart"""
    if(user_cart_state is None):
        return None
    for item in range(len(user_cart_state)):
        if(user_cart_state[item]["product_id"] == product_id):
            return item
    return None

def find_the_quantity_of_product_in_cart(product_index,user_cart_state):
    return user_cart_state[product_index]["quantity"]

def add_to_cart(user_id,product_id,user_cart_state):#this is add to cart button function args -> pid,session state of user cart
    product = {
        "product_id": product_id,
        "quantity": 1
    }
    user_cart_state.append(product)
    save_cart_in_data_file(user_id,user_cart_state)


def increase_quantity_in_cart(user_id,product_id,user_cart_state):#incresr the quantity of the cart item args -> pid,session state of user cart
    product_index = find_product_quantity_in_user_cart(product_id,user_cart_state)
    user_cart_state[product_index]["quantity"] += 1
    save_cart_in_data_file(user_id,user_cart_state)

def decrease_quantity_in_cart(user_id,product_id,user_cart_state):#decrease the quantity of the cart item args -> pid,session state of user cart
    product_index = find_product_quantity_in_user_cart(product_id,user_cart_state)
    if(user_cart_state[product_index]["quantity"] <= 1):
        user_cart_state.pop(product_index)
    else:
        user_cart_state[product_index]["quantity"] -= 1
    save_cart_in_data_file(user_id,user_cart_state)

def remove_from_cart(user_id,product_id,user_cart_state):#remove the item from the cart args -> pid,session state of user cart
    product_index = find_product_quantity_in_user_cart(product_id,user_cart_state)
    user_cart_state.pop(product_index)
    save_cart_in_data_file(user_id,user_cart_state)

def save_cart_in_data_file(user_id,user_cart_state):
    carts = reading_cart_file()
    user_index = int(user_id[1:])-1
    carts[user_index]["cart_items"] = user_cart_state
    writing_cart_file(carts)






    
