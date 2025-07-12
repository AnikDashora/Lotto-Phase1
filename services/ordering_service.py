import json 
import os
import sys
BASE_DIR = os.path.dirname(__file__)
ORDERS_DATA_FILE =os.path.join(BASE_DIR,"..","data","order.json")
ORDERS_DATA_FILE = os.path.abspath(ORDERS_DATA_FILE)


def check_file_exist():
    return os.path.isfile(ORDERS_DATA_FILE)

def reading_orders_file():
    if(not check_file_exist()):
        raise FileNotFoundError(f"Cart file doesnt exist at {ORDERS_DATA_FILE}")
    try:
        with open(ORDERS_DATA_FILE, "r") as file:
            orders = json.load(file)
            if not isinstance(orders, list):
               orders = []
    except (json.JSONDecodeError, FileNotFoundError):
            orders = []
    return orders

def writing_cart_file(orders):#orders are all the orders in the databases not only single user cart
    if(not check_file_exist()):
        raise FileNotFoundError(f"Cart file doesnt exist at {ORDERS_DATA_FILE}")
    with open(ORDERS_DATA_FILE, "w") as file:
        json.dump(orders, file, indent=4)

def create_user_orders(user_id):
    user_order = {
        "user_id":user_id,
        "orders":[]
    }
    orders = reading_orders_file()
    orders.append(user_order)
    writing_cart_file(orders)

def read_user_order(user_id):#this will return a list of all the orders user made
    orders = reading_orders_file()
    user_index = int(user_id[1:])-1
    if(len(orders) == 0):
        return None
    return orders[user_index]["orders"]


