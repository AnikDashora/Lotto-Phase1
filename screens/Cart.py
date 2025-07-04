import streamlit as st
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

remove_header_footer = """
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}

        /* Hide the orange loading progress bar */
        div[data-testid="stDecoration"] {
            display: none !important;
        }

        /* Remove top padding to avoid white space */
        .block-container {
            padding-top: 0rem !important;
        }
    </style>
"""



USER_CART = [
    {"product_id": "pid_001", "quantity": 1},
    {"product_id": "pid_002", "quantity": 2},
    {"product_id": "pid_003", "quantity": 1},
    {"product_id": "pid_004", "quantity": 3},
    {"product_id": "pid_005", "quantity": 2},
    {"product_id": "pid_006", "quantity": 1},
    {"product_id": "pid_007", "quantity": 4},
    {"product_id": "pid_008", "quantity": 2},
    {"product_id": "pid_009", "quantity": 2},
    {"product_id": "pid_010", "quantity": 1}
]
PRICE = 0

def cart_page():
    st.markdown(remove_header_footer,unsafe_allow_html=True)
    with st.container(key = "navigation_bar"):
        logo_col,search_col,other_col = st.columns([1,4,3])
        with logo_col:
            st.image("https://placehold.co/80x30?text=LOGO", width=100)
        with search_col:
            search_bar = st.text_input(label="Search",key = "search_bar",placeholder="Search",label_visibility="collapsed")
        with other_col:
            user_col,home_col,orders_col = st.columns(3)
            with user_col:
                user_label = "USER_NAME"
                st.button(label = user_label,key = "user_name_button",type="tertiary")
            with home_col:
                st.button(label = "HOME",key = "home_button",type="tertiary")
            with orders_col:
                st.button(label = "ORDERS",key = "orders_button",type="tertiary")
    
    with st.container(key = "cart_page"):
        cart_col,bill_items_col = st.columns([10,3])
        with cart_col:
            with st.container(key = "cart_col"):
                cart_back_button_col,cart_items_col = st.columns([0.5,9.5])
                with st.container(key = "back_button_section"):
                    with cart_back_button_col:
                        st.button(label="",icon = ":material/arrow_back:",type="tertiary",key = "to_last_page")
                    with cart_items_col:
                        st.markdown("<br><br>",unsafe_allow_html=True)
                with st.container(key = "cart_item_section"):
                    with cart_back_button_col:
                        pass
                    with cart_items_col:
                        for item in USER_CART:
                            with st.container(key = f"item_{item["product_id"]}"):
                                item_image_col,item_description_col = st.columns(2)
                                with item_image_col:
                                    st.image("https://placehold.co/30x30?text=Product", use_container_width=True)
                                with item_description_col:
                                    st.markdown(f"<p id = 'product_id_{item['product_id']}'>{item['product_id']}</p>",unsafe_allow_html=True)
                                    st.markdown(f"<p id = 'product_id_{item['product_id']}'>₹{PRICE}</p>",unsafe_allow_html=True) 
                                    with st.container(key = f"item_quantity_{item['product_id']}"):
                                        dec_col,qty_col,inc_col = st.columns([0.5,1,0.5])
                                        with dec_col:
                                            st.button(type="tertiary",label="",icon=":material/remove:",key = f"remove_item_{item['product_id']}")
                                        with qty_col:
                                            st.markdown(f"<p id = 'quantity'>{item["quantity"]}</p>",unsafe_allow_html=True)
                                        with inc_col:
                                            st.button(type="tertiary",label="",icon=":material/add:",key = f"add_item_{item["product_id"]}")   
        with bill_items_col:
            st.markdown("<br><br>",unsafe_allow_html=True)
            with st.container(key = "product_bill_section"):
                subtotal_col,item_price_col = st.columns([2,1])
                with subtotal_col:
                    st.markdown(f"<p id = 'subtotal_title'>SUBTOTAL</p>",unsafe_allow_html=True)
                with item_price_col:
                    st.markdown(f"<p id = 'subtotal_price'>{PRICE}</p>",unsafe_allow_html=True)
                st.button("Buy Now",type="secondary",key = "buy_now_button")



cart_page()
