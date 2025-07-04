import json 
import os
import sys
import random

PRODUCT_DATA_FILE = "D:\\Lotto-Phase1\\data\\products.json"
CATEGORIES_DATA_FILE = "D:\\Lotto-Phase1\\data\\categories.json"

def check_file_exist():
    return os.path.isfile(PRODUCT_DATA_FILE)

def create_ids(pid):
    if(isinstance(pid,str)):
        raise ValueError
    id_len = 4
    if(len(str(pid)) <= 4):
        prefix_len = id_len - len(str(pid))
        return "p"+"0"*prefix_len+str(pid)
    else:
        return "p"+str(pid)

def generate_product_id():
    if(not(check_file_exist())):
        raise FileExistsError
    pid = 0
    try:
        with open(PRODUCT_DATA_FILE,"r") as file:
            products = json.load(file)
    except json.JSONDecodeError as e:
        products = []
    
    if(len(products) == 0):
        pid = 1
    else:
        pid = len(products)+1

    return create_ids(pid)

def product_serialization(product_data):
    product = {
        "product_id":generate_product_id(),
        "product_name":product_data["name"],
        "product_price":product_data["price"],
        "product_image":product_data["image"],
        "product_description":product_data["description"],
        "product_category":product_data["product_category"]
    }
    if not check_file_exist():
        raise FileNotFoundError(f"Product data file '{PRODUCT_DATA_FILE}' does not exist.")

    try:
        with open(PRODUCT_DATA_FILE, "r") as file:
            products = json.load(file)
            if not isinstance(products, list):
                products = []
    except (json.JSONDecodeError, FileNotFoundError):
        products = []

    products.append(product)

    with open(PRODUCT_DATA_FILE, "w") as file:
        json.dump(products, file, indent=4)

def product_deserialization():
    if(not(check_file_exist())):
        raise FileNotFoundError(f"Product data file '{PRODUCT_DATA_FILE}' does not exist.")
    
    try:
        with open(PRODUCT_DATA_FILE,"r") as file:
            products = json.load(file)
    except (json.JSONDecodeError,FileNotFoundError) as e:
        products = []
    return products

def extract_product_ids():
    return [product["product_id"] for product in product_deserialization()]








    