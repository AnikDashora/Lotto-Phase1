import sys
import os
import streamlit as st

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)


from session_state.session_manager import to_signup_page
from services.auth_service import extract_user_name_by_uid

def user_check():
    if(not(st.session_state["user_exist"])):
        to_signup_page()
    else:
        pass

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

nav_bar_style = """
    <style>
        section > .stMainBlockContainer.block-container.st-emotion-cache-1w723zb.e1cbzgzq4:first-child {
            padding:0 !important;
            max-width:100%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .st-emotion-cache-8atqhb.e1q5ojhd0{
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .stVerticalBlock.st-emotion-cache-gsx7k2.eertqu03{
            gap:0;
            display: flex;
            justify-content: space-evenly;
        }
        .stVerticalBlock.st-key-navigation_bar.st-emotion-cache-gsx7k2.eertqu03{
            padding:10px 10px 5px 10px;
            display: flex;
            justify-content: space-evenly;
            background-image: linear-gradient(to bottom, #23278D, #121C7B);
            color:white;
        }
        .stVerticalBlock.st-key-categories_bar.st-emotion-cache-gsx7k2.eertqu03{
            padding:5px 10px 10px 10px;
            background-image: linear-gradient(to bottom, #121C7B, #0A185F);
            color:white;
        }
        .stButton.st-emotion-cache-8atqhb.e1mlolmg0{
            display: flex;
            justify-content: center;
            align-items: center;
        }
        /*this is for product name*/
        p{
            text-align:center;
        }
        /*this is for view product button*/
        button.st-emotion-cache-1rwb540.e1e4lema2{
            width:100%;
        }
        /*this is for nav button*/
        .stColumn.st-emotion-cache-3u1gzc.eertqu01{
            display: flex;
            justify-content: center;
            align-items: center;
            
        }
        .stColumn.st-emotion-cache-3u1gzc.eertqu01:hover{
            border:1px solid white;
            border-radius: 50px;
        }
        /*this is for cat button*/
        .stColumn.st-emotion-cache-81xr8g.eertqu01{
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .stColumn.st-emotion-cache-81xr8g.eertqu01:hover{
           border:1px solid white;
            border-radius: 50px;
        }
        .stColumn.st-emotion-cache-1spjr6t.eertqu01{
            width:100%;
        }
        /*this is for product section*/
        .stVerticalBlock.st-key-item_section.st-emotion-cache-gsx7k2.eertqu03{
            padding:10px;
        }
    </style>
"""

home_fade_in = """
    <style>
        .stVerticalBlock.st-key-navigation_bar.st-emotion-cache-gsx7k2.eertqu03,
        .stVerticalBlock.st-key-categories_bar.st-emotion-cache-gsx7k2.eertqu03,
        .stVerticalBlock.st-key-item_section.st-emotion-cache-gsx7k2.eertqu03{
            animation:fade_in 1s ease-in-out forwards;
        }
        @keyframes fade_in{
            from{
                opacity:0;
                pointer-events:none;
                transform:translateY(40px) scale(0.95)
            } 
            to{
                opacity:1;
                pointer-events:auto;
                transform:translateY(0px) scale(1)
            }
        }
    </style>
"""


def home_page():
    st.markdown(remove_header_footer,unsafe_allow_html=True)
    st.markdown(nav_bar_style,unsafe_allow_html=True)
    st.markdown(home_fade_in,unsafe_allow_html=True)
    with st.container(key = "navigation_bar"):
        logo_col,search_col,other_col = st.columns([1,4,3])
        with logo_col:
            st.image("https://placehold.co/80x30?text=LOGO", width=100)
        with search_col:
            search_bar = st.text_input(label="Search",key = "search_bar",placeholder="Search",label_visibility="collapsed")
        with other_col:
            user_col,cart_col,orders_col = st.columns(3)
            with user_col:
                user_label = extract_user_name_by_uid(st.session_state["user_id"]) if st.session_state["user_exist"] else "SignUp/Login"
                st.button(label = user_label,key = "signup\login_button",type="tertiary",on_click=user_check)
            with cart_col:
                st.button(label = "CART",key = "cart_button",type="tertiary")
            with orders_col:
                st.button(label = "ORDERS",key = "orders_button",type="tertiary")
    with st.container(key = "categories_bar"):
        category_col = st.columns(10)
        for i in range(10):
            with category_col[i]:
                st.button(label = f"category {i+1}",key = f"category_ele{i+1}",type="tertiary")
    
    st.markdown("<br><br>",unsafe_allow_html=True)
    with st.container(key="item_section"):
        num_columns = 5
        num_items = 25
        item_cols = st.columns(num_columns)
        for idx in range(num_items):
            col = item_cols[idx % num_columns]
            with col:
                st.image("https://placehold.co/150x130?text=Product", use_container_width=True)
                st.markdown("<br>",unsafe_allow_html=True)
                st.markdown(f"**Product Name {idx+1}**")
                st.markdown("<br>",unsafe_allow_html=True)
                st.button(label="View Product", key=f"product_view_button{idx+1}", type="secondary")
                st.markdown("<br>",unsafe_allow_html=True)
                add_to_cart_col, buy_now_col = st.columns(2)
                with add_to_cart_col:
                    st.button(label="Add to Cart", key=f"add_to_cart_button{idx+1}", type="secondary")
                    st.markdown("<br>",unsafe_allow_html=True)
                with buy_now_col:
                    st.button(label="Buy Now", key=f"buy_now_button{idx+1}", type="secondary")
                    st.markdown("<br>",unsafe_allow_html=True)
            if (idx + 1) % num_columns == 0:
                st.markdown("<br><br>",unsafe_allow_html=True)  # Add a row break for better spacing


    
    
    

