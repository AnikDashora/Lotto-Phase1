import sys
import os
import streamlit as st

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from services.product_service import categories_for_home_page,product_id_for_home,product_deserialization,extract_product_by_id
from session_state.session_manager import save_categories,save_products,save_all_products

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

def home_page():
    st.markdown(remove_header_footer,unsafe_allow_html=True)
    with st.container(key = "navigation_bar_section"):
        logo_col,search_bar_col,other_col = st.columns([1,4,3])
        with logo_col:
            st.image("https://placehold.co/80x30?text=LOOTO", width=100)
        with search_bar_col:
            search_bar = st.text_input(
                label="Search",
                label_visibility="collapsed",
                placeholder="Search",
                key = "navigation_search_bar"
            )
        with other_col:
            cart_col,orders_col,user_col = st.columns(3)
            with cart_col:
                st.button(
                    label="My Cart",
                    type="tertiary",
                    help = "**Go To Cart**",
                    key = "cart_button"
                )
            with orders_col:
                st.button(
                    label="My Orders",
                    type="tertiary",
                    help = "**Go To Orders**",
                    key = "orders_button"
                )
            with user_col:
                user_label = "SignUp/Login"
                user_help = "**SignUp/Login**"
                st.button(
                    label=user_label,
                    help = user_help,
                    type="tertiary",
                    key = "user_button"
                )

    save_categories(categories_for_home_page())
    save_products(product_id_for_home())
    save_all_products(product_deserialization())

    with st.container(key = "category_bar_section"):
        category_bar_col = st.columns(10)
        for category in range(10):
            with category_bar_col[category]:
                st.button(
                    label=st.session_state["categories"][category],
                    type="tertiary",
                    help = f"**{st.session_state["categories"][category]}**",
                    key = f"{st.session_state["categories"][category]}_button"
                )
    
    st.markdown("<br><br>",unsafe_allow_html=True)


    
        