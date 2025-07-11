import streamlit as st
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from session_state.session_manager import check_user_exist,give_user_name,go_to_last_page,to_signup_page
from services.cart_service import find_product_quantity_in_user_cart,find_the_quantity_of_product_in_cart,add_to_cart,increase_quantity_in_cart,decrease_quantity_in_cart
from services.product_service import extract_product_by_id

def check_add_to_cart(product_id):
    if(check_user_exist() == True):
        add_to_cart(
            st.session_state["user_id"],
            product_id,
            st.session_state["user_cart_item"]
        )
    else:
        st.session_state["pending_cart_item"] = product_id
        to_signup_page()

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
            padding:10px;
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
        
        .stHorizontalBlock.st-emotion-cache-ajtf3x.eertqu03 {
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
        .stElementContainer.element-container.st-key-back_to_home.st-emotion-cache-r6om3p.eertqu00{
            display: flex;
            align-content: center;
            margin:18px;
        }
    </style>
"""

button_styles = """
    <style>
        .st-emotion-cache-r6om3p{
            width:100%;
        }
        .stVerticalBlock.st-key-button_section.st-emotion-cache-gsx7k2.eertqu03{
            display: flex;
            align-items: center;
            justify-content: space-between;
            height:100px;
            width:100%;
        }
        button.st-emotion-cache-1rwb540.e1e4lema2{
            margin:5px;
            padding:0.8rem;
            border: 1px solid #23278D;
            border-radius:40px;
            width:70%;
            background-image: linear-gradient(to bottom, #4a50c7, #23278D); /* lighter blue */
            color: #fff; /* white text */
            font-weight: bold;
            transition: background-image 0.3s cubic-bezier(0.4,0,0.2,1), border 0.3s cubic-bezier(0.4,0,0.2,1), color 0.3s cubic-bezier(0.4,0,0.2,1);
        }
        .stButton.st-emotion-cache-8atqhb.e1mlolmg0{
            display: flex;
            align-items: center;
            justify-content: center;
        }
        button.st-emotion-cache-1rwb540.e1e4lema2:hover{
            background-image: linear-gradient(to bottom, #181b5e, #121C7B); /* darker blue */
            color: #fff; /* keep white text */
            border:1px solid #3137c5;
        }
        button.st-emotion-cache-1rwb540.e1e4lema2:active{
            background-image: linear-gradient(to bottom, #181b5e, #121C7B);
            color: #fff;
            border:1px solid #3137c5;
        }
        button.st-emotion-cache-1rwb540.e1e4lema2:focus:not(:active){
            border:1px solid #3137c5;
            color:#fff;
        }
        button.st-emotion-cache-1rwb540.e1e4lema2:focus-visible{
            box-shadow:#3137c5 0px 0px 0px 0.16rem;
        }
        p{
            overflow:hidden;
            position:relative;
        }
    </style>
"""

product_style = """
    <style>
        .stVerticalBlock.st-key-product_content.st-emotion-cache-gsx7k2.eertqu03{
            display: flex;
            justify-content: space-between;
            height: 350px;
            flex-direction: column;
        }
    </style>
"""

product_description_style = """
    <style>
        .st-emotion-cache-1nwdr1w.e1g8wfdw0{
            display:flex;
            align-item: center;
            justify-content:center;
        }
        h1{
            text-align:center;
        }
        h5{
            text-align:center;
        }
        p#product_price{
            text-align:center;
            font-size:2rem;
        }
        span.st-emotion-cache-gi0tri.e1g8wfdw3{
            display:none;
        }
    </style>
"""

product_image_style = """
    <style>
        img#product_image{
            width: 450px;
            height: auto;
            object-fit: cover;
            border-radius: 30px;
            box-shadow: rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.04) 0px 10px 10px -5px;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
    </style>
"""

add_to_cart_sub_button_styles = """
    <style>
        .stVerticalBlock.st-key-add_to_cart_qty.st-emotion-cache-gsx7k2.eertqu03{
            width: 70%;
            display: flex;
            justify-self: anchor-center;
            border: 1px solid black;
            border-radius: 40px;
            align-content: stretch;
        }
        .stElementContainer.element-container.st-key-inc_cart.st-emotion-cache-r6om3p.eertqu00{
            background-image: linear-gradient(to bottom, #4a50c7, #23278D);
            border-radius: 0px 40px 40px 0px;
            background-size: inherit;
            padding: 0.2rem;
            color:white;
        }
        .stElementContainer.element-container.st-key-dec_cart.st-emotion-cache-r6om3p.eertqu00{
            background-image: linear-gradient(to bottom, #4a50c7, #23278D);
            border-radius: 40px 0px 0px 40px;
            background-size: inherit;
            padding: 0.2rem;
            color:white;
        }
    </style>
"""

page_animation = """
    <style>
        h1,h5,p#product_price{
            animation:text_animation 1s ease-in-out forwards;
        }
        img#product_image{
            animation:image_animation 1s ease-in-out forwards;
        }
        button.st-emotion-cache-1rwb540.e1e4lema2,.stVerticalBlock.st-key-add_to_cart_qty.st-emotion-cache-gsx7k2.eertqu03{
            animation:button_animation 1s ease-in-out forwards; 
        }


        @keyframes image_animation{
            from{
                opacity:0;
                transform:translateY(40px) scale(0.90);
            }
            to{
                opacity:1;
                transform:translateY(0) scale(1);
            }
        }
        @keyframes text_animation {
            from{
                opacity:0;
                transform:translateY(40px);
            }
            to{
                opacity:1;
                transform:translateY(0);
            }
        }
        @keyframes button_animation{
            from{
                opacity:0;
                width:15%;
            }
            to{
                opacity:1;
                width:70%;
            }
        }
    </style>
"""


def product_page():
    product_id = st.session_state["view_product_id"]
    product_info = extract_product_by_id(product_id,st.session_state["all_products"])
    user_product_quantity_index = find_product_quantity_in_user_cart(
                            product_id,
                            st.session_state["user_cart_item"]
                        )
    st.markdown(remove_header_footer,unsafe_allow_html=True)
    st.markdown(navigation_bar_styles,unsafe_allow_html=True)
    st.markdown(back_button_styles,unsafe_allow_html=True)
    st.markdown(product_style,unsafe_allow_html=True)
    st.markdown(product_description_style,unsafe_allow_html=True)
    st.markdown(product_image_style,unsafe_allow_html=True)
    st.markdown(button_styles,unsafe_allow_html=True)
    st.markdown(add_to_cart_sub_button_styles,unsafe_allow_html=True)
    st.markdown(page_animation,unsafe_allow_html=True)
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
                user_label = give_user_name() if check_user_exist() else "SignUp/Login"
                user_help = f"**{give_user_name()}**" if check_user_exist() else "**SignUp/Login**"
                st.button(
                    label=user_label,
                    help = user_help,
                    type="tertiary",
                    key = "user_button",
                    on_click=to_signup_page
                )

    product_image = f"""
    <img id = 'product_image' src = '{product_info["product_image"]}' alt = '{product_info["product_name"]}'>
    """
    with st.container(key = "product_section"):
        back_btn_col,product_col = st.columns([1,10])
        with st.container(key = "back_button_section"):
            with back_btn_col:
                st.button(label="",icon = ":material/arrow_back:",type="tertiary",key = "back_to_home",on_click=go_to_last_page)
            with product_col:
                # st.markdown("<br><br><br>",unsafe_allow_html=True)
                pass
        with st.container(key = "product_description_section"):
            product_image_col,product_description_col = st.columns(2)
            with product_image_col:
                st.markdown(product_image,unsafe_allow_html=True)
            with product_description_col:
                with st.container(key = "product_content"):
                    with st.container(key = "product_detail"):
                        st.markdown(f"<h1 id = 'product_name'>{product_info["product_name"]}</h1>",unsafe_allow_html=True)
                        st.markdown(f"<h5 id = 'product_description'>{product_info["product_description"]}</h3>",unsafe_allow_html=True)
                        st.markdown(f"<p id = 'product_price'>₹ {product_info["product_price"]}</p>",unsafe_allow_html=True)
                    with st.container(key = "buttons_section"):
                        if(user_product_quantity_index is None):
                            st.button(
                                label = "Add To Cart",
                                key=f"add_to_cart",
                                type="secondary",
                                on_click=check_add_to_cart,
                                args=(product_id,)
                            )
                        else:
                            with st.container(key=f"add_to_cart_qty"):
                                dec_col, qty_col, inc_col = st.columns([0.5, 1, 0.5])
                                with dec_col:
                                    st.button(
                                        type="tertiary",
                                        label="",
                                        icon=":material/remove:",
                                        key=f"dec_cart",
                                        on_click=decrease_quantity_in_cart,
                                        args=(st.session_state["user_id"],product_id,st.session_state['user_cart_item'],)
                                    )
                                with qty_col:
                                    st.markdown(
                                        f"""<p id='quantity'>{
                                            find_the_quantity_of_product_in_cart(
                                                    user_product_quantity_index,
                                                    st.session_state['user_cart_item']
                                                )
                                        }</p>""",
                                        unsafe_allow_html=True
                                    )
                                with inc_col:
                                    st.button(
                                        type="tertiary",
                                        label="",
                                        icon=":material/add:",
                                        key=f"inc_cart",
                                        on_click=increase_quantity_in_cart,
                                        args=(st.session_state["user_id"],product_id,st.session_state['user_cart_item'],)      
                                    )
                        st.button(
                            label = "Buy Now",
                            key=f"buy_now_button",
                            type="secondary"
                        )
                
