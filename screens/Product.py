import streamlit as st
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from session_state.session_manager import to_home_page,add_to_cart,remove_from_cart

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

styles = """
    <style>
        .stMainBlockContainer.block-container.st-emotion-cache-1w723zb.e1cbzgzq4{
            max-width:100%;
        }
        .stVerticalBlock.st-emotion-cache-gsx7k2.eertqu03{
            gap:0px;
        }
        img{
            height:500px;
            animation:fade_in_img 0.5s ease-in-out;
        }
        .stColumn.st-emotion-cache-ss04kk.eertqu01{
            display: flex;
            justify-content: space-between;
            align-items: center;
            align-content: space-between;
            flex-direction: row;
            flex-wrap: wrap;
        }
        h1{
            text-align:center;
            animation:fade_in_product_text 0.5s ease-in-out forwards;
        }
        .stButton.st-emotion-cache-8atqhb.e1mlolmg0{
            display: flex;
            justify-content: center;
            align-items: center;
            
        }
        button.st-emotion-cache-1rwb540.e1e4lema2{
            border-radius:50px;
            margin:15px 0px 5px 0px;
            background-image:linear-gradient(to bottom, #565bd5cc, #565bd5);;
            color:white;
            border:1px solid #3137c5;
            animation:bring_in_button 1s ease-in-out forwards;
        }
        h3#product-description{
            text-align:center;
            margin: 70px;
            margin-top: 30px;
            margin-left: 0px;
            margin-right: 0px;
            margin-bottom:0px;
            animation:fade_in_product_text 0.5s ease-in-out forwards;
        }
        p#quantity{
            margin-top: 7px;
            margin-bottom: 0px;
            text-align: center;
            padding: 0px;
        }
        .st-emotion-cache-13o7eu2.eertqu02:has(> .stVerticalBlock.st-key-add_to_cart_qty.st-emotion-cache-gsx7k2.eertqu03) {
            display: flex;
            width: 80%;
            justify-content: center;
            /* align-items: center; */
            align-self: anchor-center;
        }
        .stVerticalBlock.st-key-add_to_cart_qty.st-emotion-cache-gsx7k2.eertqu03 {
            border: 1px solid black;
            border-radius: 50px;
            width: 80%;
        }
        p#product_price {
            text-align: center;
            font-size: 35px;
            margin-top:30px;
            margin-bottom:50px;
            animation:fade_in_product_text 0.5s ease-in-out forwards;
        }
        span.st-emotion-cache-gi0tri.e1g8wfdw3 {
            display: none;
        }
        .stHorizontalBlock.st-emotion-cache-ajtf3x.eertqu03{
            flex-wrap:wrap;
        }

        @keyframes fade_in_img{
            from{
                opacity:0;
                pointer-events:none;
                transform:translateY(40px) scale(0.90);
            }
            to{
                opacity:1;
                pointer-events:auto;
                transform:translateY(0px) scale(1);
            }
        }
        @keyframes fade_in_product_text{
            from{
                opacity:0;
                pointer-events:none;
                transform:translateY(40px);
            }
            to{
                opacity:1;
                pointer-events:auto;
                transform:translateY(0px);
            }
        }
        @keyframes bring_in_button{
            0%{
                content-visibility:hidden;
                opacity:0;
                pointer-events:none;
                width:0%;
            }
            100%{
                content-visibility:auto;
                opacity:1;
                pointer-events:auto;
                width:80%;
            }

        }
        
    </style>
"""

def product_page():
    st.markdown(remove_header_footer,unsafe_allow_html=True)
    st.markdown(styles,unsafe_allow_html=True)
    back_btn_col,product_col = st.columns([1,10])
    with st.container(key = "back_button_area"):
        with back_btn_col:
            st.button(label="",icon = ":material/arrow_back:",type="tertiary",key = "back_to_home",on_click=to_home_page)
        with product_col:
            st.markdown("<br><br><br>",unsafe_allow_html=True)
    with st.container(key = "product_area"):
        with back_btn_col:
            pass
        with product_col:
            product_img_col,product_description_col = st.columns(2)
            with product_img_col:
                st.image("https://placehold.co/100x100?text=Product", use_container_width=True)
            with product_description_col:
                st.markdown("<h1 id = 'product_name'>Product Name</h1>",unsafe_allow_html=True)
                st.markdown("<h3 id = 'product_description'>Product Description</h3>",unsafe_allow_html=True)
                st.markdown("<p id = 'product_price'>₹0.00</p>",unsafe_allow_html=True)
                if(st.session_state["cart_qty"] == 0):
                    st.button("Add to Cart",type="secondary",key = "add_to_cart",on_click=add_to_cart)
                else:
                    with st.container(key = "add_to_cart_qty"):
                        dec_col,qty_col,inc_col = st.columns([0.5,1,0.5])
                        with dec_col:
                            st.button(type="tertiary",label="",icon=":material/remove:",on_click=remove_from_cart)
                        with qty_col:
                            st.markdown(f"<p id = 'quantity'>{st.session_state["cart_qty"]}</p>",unsafe_allow_html=True)
                        with inc_col:
                            st.button(type="tertiary",label="",icon=":material/add:",on_click=add_to_cart)
                st.button("Buy Now",type="secondary",key = "buy_now_button")
                    
                