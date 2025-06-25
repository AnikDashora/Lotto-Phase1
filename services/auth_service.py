import json
import os
import uuid

USER_DATA_FILE = "D:\\Lotto-Phase1\\data\\users.json"

def check_file_exist():
    return os.path.isfile(USER_DATA_FILE)

def create_ids(uid):
    if(isinstance(uid,str)):
        raise ValueError
    id_len = 4
    if(len(str(uid)) <= 4):
        prefix_len = id_len - len(str(uid))
        return "u"+"0"*prefix_len+str(uid)
    else:
        return "u"+str(uid)

def generate_user_id():
    if(not(check_file_exist())):
        raise FileExistsError
    uid = 0
    try:
        with open(USER_DATA_FILE,"r") as file:
            users = json.load(file)
    except json.JSONDecodeError as e:
        users = []
    
    if(len(users) == 0):
        uid = 1
    else:
        uid = len(users)+1

    return create_ids(uid)
    
def generate_mac_address():
    return str(uuid.getnode())

def user_serialization(user_data):
    user = {
        "uid":generate_user_id(),
        "username":user_data["username"],
        "email":user_data["useremail"],
        "password" : user_data["userpassword"],
        "device_id":generate_mac_address()
    }
    if not check_file_exist():
        raise FileNotFoundError(f"User data file '{USER_DATA_FILE}' does not exist.")

    try:
        with open(USER_DATA_FILE, "r") as file:
            users = json.load(file)
            if not isinstance(users, list):
                users = []
    except (json.JSONDecodeError, FileNotFoundError):
        users = []

    users.append(user)

    with open(USER_DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)

def user_deserialization():
    if(not(check_file_exist(USER_DATA_FILE))):
        raise FileNotFoundError(f"User data file '{USER_DATA_FILE}' does not exist.")
    
    try:
        with open(USER_DATA_FILE,"r") as file:
            users = json.load(file)
    except (json.JSONDecodeError,FileNotFoundError) as e:
        users = []
    return users
