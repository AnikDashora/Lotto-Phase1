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

def user_serialization(user_data):
    user = {
        "uid":generate_user_id(),
        "username":user_data["username"],
        "email":user_data["useremail"],
        "password" : encrypt_password(user_data["useremail"],user_data["userpassword"])
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
    if(not(check_file_exist())):
        raise FileNotFoundError(f"User data file '{USER_DATA_FILE}' does not exist.")
    
    try:
        with open(USER_DATA_FILE,"r") as file:
            users = json.load(file)
    except (json.JSONDecodeError,FileNotFoundError) as e:
        users = []
    return users

def extract_user_email():
    users = user_deserialization()
    emails = [user["email"] for user in users]
    return emails

def extract_user_name():
    users = user_deserialization()
    names = [user["username"] for user in users]
    return names

def extract_password():
    users = user_deserialization()
    password = [user["password"] for user in users]
    return password

def if_user_exsits(user_email):
    emails = extract_user_email()
    return (user_email in emails)

def verify_password(email,password):
    emails = extract_user_email()
    passwords = extract_password()
    user_idx = emails.index(email)
    return password == encrypt_password(email,passwords[user_idx])

def encrypt_password(email,password):
    local,domain = email.split("@")
    del domain
    half_local_len = len(local)//2 - 1
    new_password = local[:half_local_len] + password + local[half_local_len:]
    encrypted_password = ""
    for i in new_password:
        encrypted_password += str((ord(i)**2)+(ord(i)*5)+10) #x^2 + 5x + 10
    return encrypted_password

def verify_user(email,password):
    if(not(if_user_exsits(email))):
        return False
    if(verify_password(email,password)):
        return True
    else:
        return False
