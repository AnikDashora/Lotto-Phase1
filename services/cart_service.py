import json
import os
import sys
import random

from auth_service import extract_user_ids
from product_service import extract_product_ids
CART_DATA_FILE = "D:\\Lotto-Phase1\\data\\cart.json"


def check_file_exist():
    return os.path.isfile(CART_DATA_FILE)







    
