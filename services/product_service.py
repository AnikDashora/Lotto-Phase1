import json 
import os
import sys
import random
BASE_DIR = os.path.dirname(__file__)
PRODUCT_DATA_FILE = os.path.join(BASE_DIR,"..","data","products.json")
CATEGORIES_DATA_FILE = os.path.join(BASE_DIR,"..","data","categories.json")
PRODUCT_DATA_FILE = os.path.abspath(PRODUCT_DATA_FILE)
CATEGORIES_DATA_FILE = os.path.abspath(CATEGORIES_DATA_FILE)
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

def extract_product_ids():# return all the product ids in data file
    return [product["product_id"] for product in product_deserialization()]

def product_id_for_home():#return the product ids to display at home page
    product_ids = extract_product_ids()
    random.shuffle(product_ids)
    return product_ids[:20]
    
def extract_product_by_id(product_id,products):#return product info in dict by pids
    product_idx = int(product_id[1:])-1
    return products[product_idx]

def categories_deserialization():#return the dict of the categories
    if(not(check_file_exist())):
        raise FileNotFoundError(f"Product data file '{CATEGORIES_DATA_FILE}' does not exist.")
    
    try:
        with open(CATEGORIES_DATA_FILE,"r") as file:
            categories = json.load(file)
    except (json.JSONDecodeError,FileNotFoundError) as e:
        categories = []
    return categories

def categories_for_home_page():#return the categories(name) in string for home page display 
    categories = list(categories_deserialization().keys())
    return categories[0:10]

def extract_product_id_by_categories(categories):#return the list of products ids under the categories
    return categories_deserialization()[categories]  

def extract_product_price(product_id):
    products = product_deserialization()
    product_idx = int(product_id[1:])-1
    return products[product_idx]["product_price"]


