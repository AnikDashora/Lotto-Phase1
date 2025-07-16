import streamlit as st
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from session_state.session_manager import to_home_page,go_to_last_page,give_user_name
from services.product_service import extract_product_by_id
from services.cart_service import increase_quantity_in_cart,decrease_quantity_in_cart,subtotal_price


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

navigation_bar_styles = """
    <style>
    *{
        padding:0px;
        margin:0px;
    }
        section > .stMainBlockContainer.block-container.st-emotion-cache-1w723zb.e1cbzgzq4:first-child{
            padding:0 !important;
            max-width:100%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .stVerticalBlock.st-key-navigation_bar_section.st-emotion-cache-gsx7k2.eertqu03{
            padding:10px 10px 10px 10px;
            margin-bottom:24px;
            display: flex;
            justify-content: space-around;
            background-image: linear-gradient(to bottom, #23278D, #121C7B);
            color:white;
        }
        /*this is img part*/
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
        .stTooltipIcon.st-emotion-cache-oj1fi.e1pw9gww0{
            display: flex;
            -webkit-box-align: center;
            align-items: center;
            margin-top: 0px;
            justify-content: center;
        }
        p{
            text-align:center;
        }
        .st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-ak.st-al.st-am.st-an.st-ao.st-ap.st-aq.st-ar.st-as.st-at.st-au.st-av.st-aw.st-ax.st-ay.st-az.st-b0.st-b1.st-b2.st-b3.st-b4.st-b5.st-b6.st-b7.st-b8.st-b9.st-ba {
            height:40px;
        }
        
        .stVerticalBlock.st-key-navigation_bar_section.st-emotion-cache-gsx7k2.eertqu03
        > .st-emotion-cache-13o7eu2.eertqu02
        > .stHorizontalBlock.st-emotion-cache-ajtf3x.eertqu03 {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
        }
        .stColumn.st-emotion-cache-3u1gzc.eertqu01{
            display: flex;
            justify-content: center;
            align-items: center;
            transition: border 0.5s cubic-bezier(0.4,0,0.2,1),
              border-radius 0.5s cubic-bezier(0.4,0,0.2,1),
              background-color 0.5s cubic-bezier(0.4,0,0.2,1);
            
        }
        .stColumn.st-emotion-cache-3u1gzc.eertqu01:hover{
            background-color:white;
            color:black;
            border:1px solid white;
            border-radius: 50px;
            box-shadow: 0 2px 12px rgba(35,39,141,0.15);
        }
        button.st-emotion-cache-2yl1y1.e1e4lema3:hover{
            color:black;
        }
        button.st-emotion-cache-2yl1y1.e1e4lema3:active{
            color:black;
        }
        button.st-emotion-cache-2yl1y1.e1e4lema3:focus-visible{
            color: black;
            box-shadow: rgba(255, 255, 255, 0.5) 0px 0px 0px 0.2rem;
        }
        
    </style>

"""

back_button_styles = """
    <style>
    .stElementContainer.element-container.st-key-back_to_home.st-emotion-cache-r6om3p.eertqu00
    > .stButton.st-emotion-cache-8atqhb.e1mlolmg0{
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap:wrap;
    }
    .stElementContainer.element-container.st-key-back_to_home.st-emotion-cache-r6om3p.eertqu00
    > .stButton.st-emotion-cache-8atqhb.e1mlolmg0
    > button.st-emotion-cache-2yl1y1.e1e4lema3:hover{
        border:1px solid black;
        width:40px;
        height:40px;
        border-radius:50%;
        transition:  border-radius 0.3s ease;
    }
    </style>
"""

cart_item_styles = """
    <style>
        .stVerticalBlock.st-key-cart_items.st-emotion-cache-gsx7k2.eertqu03{
           padding: 20px;
           background-color: #f8f9fa;
        }
        
        img#cart_item_image{
            width: 100%;
            height: 100%;
            max-width: 180px;
            max-height: 200px;
            object-fit: cover;
            object-position: center;
            border-radius: 8px;
            border: 1px solid #e0e0e0;
            display: block;
            margin: auto;
        }
        
        [class*="st-key-cart_item_"]{
            display: flex;
            justify-content: center;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 20px;
            height: 220px;
            margin: 12px 0px;
            background-color: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        [class*="st-key-cart_item_"]
        > .st-emotion-cache-13o7eu2.eertqu02
        > .stHorizontalBlock.st-emotion-cache-ajtf3x.eertqu03
        > .stColumn.st-emotion-cache-ss04kk.eertqu01{
            width: auto;
            flex: none;
        }

        [class*="st-key-cart_item_"]
        > .st-emotion-cache-13o7eu2.eertqu02
        > .stHorizontalBlock.st-emotion-cache-ajtf3x.eertqu03
        > .stColumn.st-emotion-cache-ss04kk.eertqu01:first-child {
            height: 178px;
            width: 200px;
            border-radius: 8px;
            padding: 10px;
            box-sizing: border-box;
        }

        [class*="st-key-cart_item_"]
        > .st-emotion-cache-13o7eu2.eertqu02
        > .stHorizontalBlock.st-emotion-cache-ajtf3x.eertqu03{
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: nowrap;
            height: 100%;
            gap: 15px;
        }

        /* Content column styling */
        [class*="st-key-cart_item_"]
        > .st-emotion-cache-13o7eu2.eertqu02
        > .stHorizontalBlock.st-emotion-cache-ajtf3x.eertqu03
        > .stColumn.st-emotion-cache-ss04kk.eertqu01:nth-child(2) {
            width:50%;
            padding: 0 10px;
        }

        /* Actions column styling */
        [class*="st-key-cart_item_"]
        > .st-emotion-cache-13o7eu2.eertqu02
        > .stHorizontalBlock.st-emotion-cache-ajtf3x.eertqu03
        > .stColumn.st-emotion-cache-ss04kk.eertqu01:last-child {
            min-width: 120px;
            text-align: center;
        }

        /* Responsive design */
        @media (max-width: 786px) {
            [class*="st-key-cart_item_"]
            > .st-emotion-cache-13o7eu2.eertqu02
            > .stHorizontalBlock.st-emotion-cache-ajtf3x.eertqu03{
                flex-wrap: wrap;
                justify-content: center;
                text-align: center;
            }
            
            [class*="st-key-cart_item_"]
            > .st-emotion-cache-13o7eu2.eertqu02
            > .stHorizontalBlock.st-emotion-cache-ajtf3x.eertqu03
            > .stColumn.st-emotion-cache-ss04kk.eertqu01:first-child {
                margin-right: 0;
                margin-bottom: 15px;
            }
            
            [class*="st-key-cart_item_"]{
                height: auto;
                padding: 15px;
            }
        }
        [class*="st-key-add_to_cart_qty_"]{
            border:1px solid black;
            display:flex;
            flex-wrap:wrap;
            justify-content: center;
            margin-top:18px;
            border-radius:40px;
            width:100%;
        }
        [class*="st-key-add_to_cart_qty_"]
        > .st-emotion-cache-13o7eu2.eertqu02
        > .stHorizontalBlock.st-emotion-cache-ajtf3x.eertqu03{
            display:flex;
            flex-wrap:wrap;
            justify-content: center;
            align-items:center;
        }
        p.cart_item_name {
            font-size: xx-large;
            font-weight: bolder;
            text-align: center;
        }
        p.cart_item_price {
            font-size: x-large;
            font-weight: bold;
            text-align: center;
        }
    </style>
"""

subtotal_section_styles = """
    <style>
        .stVerticalBlock.st-key-subtotal_box.st-emotion-cache-gsx7k2.eertqu03{
            width:100%;
            height:150px;;
            border:2px solid black;
            padding:18px;
            margin-top:32px;
            display:flex;
            align-items: center;
            justify-content: center;
            border-radius:20px;
        }
        .stVerticalBlock.st-key-subtotal_box.st-emotion-cache-gsx7k2.eertqu03
        >.st-emotion-cache-13o7eu2.eertqu02
        >.stHorizontalBlock.st-emotion-cache-ajtf3x.eertqu03{
            display:flex;
            align-items: center;
            justify-content: center;
            gap:2rem;
        }
        p#subtotal_text{
            word-break: auto-phrase;
            width: fit-content;
            font-size: x-large;
            font-weight: bold;
            text-align: center;

        }
        p#subtotal_amount{
            word-break: auto-phrase;
            width: fit-content;
            font-size: x-large;
            font-weight: bold;
            text-align: center;
        }
    </style>
"""
def cart_page():
    st.markdown(remove_header_footer,unsafe_allow_html=True)
    st.markdown(navigation_bar_styles,unsafe_allow_html=True)
    st.markdown(back_button_styles,unsafe_allow_html=True)
    st.markdown(cart_item_styles,unsafe_allow_html=True)
    st.markdown(subtotal_section_styles,unsafe_allow_html=True)
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
            home_col,orders_col,user_col = st.columns(3)
            with home_col:
                st.button(
                    label="Home",
                    type="tertiary",
                    help = "**Go To Home**",
                    key = "home_button",
                    on_click=to_home_page
                )
            with orders_col:
                st.button(
                    label="My Orders",
                    type="tertiary",
                    help = "**Go To Orders**",
                    key = "orders_button"
                )
            with user_col:
                user_label = give_user_name() 
                user_help = f"**{give_user_name()}**" 
                st.button(
                    label=user_label,
                    help = user_help,
                    type="tertiary",
                    key = "user_button",
                )

    with st.container(key = "cart_section"):
        back_button_col,cart_items_col,subtotal_col = st.columns([1,8,3])
        
        with st.container(key = "back_button_section"):
            with back_button_col:
                st.button(
                    label="",
                    icon = ":material/arrow_back:",
                    type="tertiary",
                    key = "back_to_home",
                    on_click=go_to_last_page
                )
        
        with st.container(key = "cart_item_section"):
            with cart_items_col:
                with st.container(key = "cart_items"):
                    for item in st.session_state["user_cart_item"]:
                        cart_item = extract_product_by_id(item['product_id'],st.session_state["all_products"])
                        cart_item_image = cart_item["product_image"]
                        cart_item_name = cart_item["product_name"]
                        with st.container(key = f"cart_item_{item['product_id']}"):
                            item_img_col,item_description_col = st.columns(2)
                            with item_img_col:
                                item_image = f"""
                                    <img id='cart_item_image' src='{cart_item_image}' alt='{cart_item_name}'>
                                """
                                st.markdown(
                                    item_image,
                                    unsafe_allow_html=True
                                )
                            with item_description_col:
                                with st.container(key = f"item_description_{item['product_id']}"):
                                    
                                    with st.container(key = f"item_text_{item['product_id']}"):
                                        item_name = f"<p  class = 'cart_item_name'>{cart_item["product_name"]}</p>"
                                        item_price = f"<p class = 'cart_item_price'>₹ {cart_item["product_price"]}</p>"
                                        st.markdown(
                                            item_name,
                                            unsafe_allow_html=True
                                        )
                                        st.markdown(
                                            item_price,
                                            unsafe_allow_html=True
                                        )

                                    with st.container(key=f"add_to_cart_qty_{item['product_id']}"):
                                        dec_col, qty_col, inc_col = st.columns([0.5, 1, 0.5])
                                        with dec_col:
                                            st.button(
                                                type="tertiary",
                                                label="",
                                                icon=":material/remove:",
                                                key=f"dec_cart{item['product_id']}",
                                                on_click=decrease_quantity_in_cart,
                                                args=(st.session_state["user_id"],item['product_id'],st.session_state['user_cart_item'],)
                                            )
                                        with qty_col:
                                            st.markdown(
                                                f"""<p id='quantity'>{
                                                    item["quantity"]
                                                }</p>""",
                                                unsafe_allow_html=True
                                            )
                                        with inc_col:
                                            st.button(
                                                type="tertiary",
                                                label="",
                                                icon=":material/add:",
                                                key=f"inc_cart{item['product_id']}",
                                                on_click=increase_quantity_in_cart,
                                                args=(st.session_state["user_id"],item['product_id'],st.session_state['user_cart_item'],)   
                                            )
            
        with st.container(key = "subtotal_section"):
            with subtotal_col:
                subtotal_text = "<p id = 'subtotal_text'>Subtotal</p>"
                subtotal_amount = f"<p id = 'subtotal_amount'>₹ {subtotal_price(st.session_state["user_cart_item"],
                                                                                st.session_state["all_products"])}</p>"
                with st.container(key = "subtotal_box"):
                    subtotal_text_col,subtotal_amount_col = st.columns(2)
                    with subtotal_text_col:
                        st.markdown(
                            subtotal_text,
                            unsafe_allow_html=True
                        )
                    with subtotal_amount_col:
                        st.markdown(
                            subtotal_amount,
                            unsafe_allow_html=True
                        )

                    st.button(
                        label = "Buy Now",
                        key=f"buy_now_button",
                        type="secondary"
                    )

                



                    
                    


    



