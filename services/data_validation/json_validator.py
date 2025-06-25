import streamlit as st

def validate_name(name):
    if(len(name) == 0):
        return False
    if(len(name) <= 2):
        st.error("Please Enter a Vaild Name")
        return False
    special_chars = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', 
    '{', '}', '[', ']', '|', '\\', ':', ';', "'", '"', '<', '>', ',', '.', '?', '/'
    ]
    for char in name:
        if(char in special_chars or char.isdigit()):
            st.error("Please Enter a Vaild Name")
            return False
    return True

def validate_email(email):
    if(len(email) == 0):
        return False
    
    if(('@' not in email)):
        st.error("Invalid Email")
        return False
    
    if(email.count("@") != 1):
        st.error("Invalid Email")
        return False
    
    if(" " in email):
        st.error("Invalid Email")
        return False
    
    local,domain = email.split("@")

    if(not local or not domain):
        st.error("Invalid Email")
        return False
    
    if("." not in domain):
        st.error("Invalid Email")
        return False

    if(domain.startswith(".") or domain.endswith(".")):
        st.error("Invalid Email")
        return False
    
    return True

def validate_password(password):
    
    if(len(password) == 0):
        return False
    
    special_chars = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', 
    '{', '}', '[', ']', '|', '\\', ':', ';', "'", '"', '<', '>', ',', '.', '?', '/'
    ]
    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_letters = "abcdefghijklmnopqrstuvwxyz"

    special_chars_flag = False
    capital_case_flag = False
    small_case_flag = False
    number_flag = False

    for char in password:
        if(char in special_chars and special_chars_flag == False):
            special_chars_flag = True
        if(char in capital_letters and capital_case_flag == False):
            capital_case_flag = True
        if(char in small_letters and small_case_flag == False):
            small_case_flag = True
        if(char.isdigit() and number_flag == False):
            number_flag = True
    
    if(not(special_chars_flag and small_case_flag and capital_case_flag and number_flag)):
        st.error("Choose a Strong Password")
        return False
    
    return True

