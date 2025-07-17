import json 
import os
import sys
import random
from datetime import datetime, timedelta
from product_service import extract_product_price,extract_product_ids
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

def writing_orders_file(orders):#orders are all the orders in the databases not only single user cart
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
    writing_orders_file(orders)

def read_user_order(user_id):#this will return a list of all the orders user made
    orders = reading_orders_file()
    user_index = int(user_id[1:])-1
    if(len(orders) == 0):
        return None
    return orders[user_index]["orders"]

def extract_all_orders():
    user_orders = reading_orders_file()
    orders = [user["orders"] for user in user_orders]
    return orders

def create_ids(oid):
    if(isinstance(oid,str)):
        raise ValueError
    id_len = 4
    if(len(str(oid)) <= 4):
        prefix_len = id_len - len(str(oid))
        return "o"+"0"*prefix_len+str(oid)
    else:
        return "o"+str(oid)

def count_orders(user_orders):
    return len(user_orders)

def generate_order_id():
    users_orders = reading_orders_file()
    totalnumber_orders = 0
    oid = 0
    for users in users_orders:
        totalnumber_orders += count_orders(users["orders"])
    if(totalnumber_orders <= 0):
        oid = 1
    else:
        oid = totalnumber_orders + 1
    return create_ids(oid)

def random_timestamp(start, end):
    """Generate a random datetime between `start` and `end`."""
    # convert to unix timestamp (seconds since epoch)
    start_ts = int(start.timestamp())
    end_ts = int(end.timestamp())
    # get a random timestamp between start and end
    rand_ts = random.randint(start_ts, end_ts)
    # convert back to datetime
    rand_dt = datetime.fromtimestamp(rand_ts)
    # format as YYYY-MM-DD HH:MM
    return rand_dt.strftime('%Y-%m-%d %H:%M')

def add_user_order(user_id,order_data):
    user_order = {
        "order_id":generate_order_id(),
        "items":order_data["items"],
        "timestamp":order_data["timestamp"],
        "current_status": order_data["status"]
    }
    all_orders = reading_orders_file()
    user_idx = int(user_id[1:])-1
    all_orders[user_idx]["orders"].append(user_order)
    writing_orders_file(all_orders)

    


