import json
import os
import sys
import random

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
    carts = read_user_cart()
    carts.append(user_cart)
    writing_cart_file(carts)

def read_user_cart(user_id):#this will return a dictnaory of user_id and cart_items
    carts = reading_cart_file()
    user_index = int(user_id[1:])-1
    return carts(user_index) 








    
