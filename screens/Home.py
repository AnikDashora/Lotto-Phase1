import sys
import os
import streamlit as st

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from services.product_service import categories_for_home_page,product_id_for_home,product_deserialization,extract_product_by_id
from session_state.session_manager import save_categories,save_products,save_all_products,to_signup_page
from services.cart_service import find_product_quantity_in_user_cart,find_the_quantity_of_product_in_cart,add_to_cart

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
            padding:10px 10px 5px 10px;
            display: flex;
            justify-content: space-evenly;
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
            
        }
        .stColumn.st-emotion-cache-3u1gzc.eertqu01:hover{
            background-color:white;
            color:black;
            border:1px solid white;
            border-radius: 50px;
            box-shadow: 0 2px 12px rgba(35,39,141,0.15);
        }
        
    </style>
"""

category_bar_styles = """
    <style>
        .stVerticalBlock.st-key-category_bar_section.st-emotion-cache-gsx7k2.eertqu03{
            padding:5px 10px 5px 10px;
            display: inline-flex;
            justify-content: space-around;
            flex-wrap: wrap;
            background-image: linear-gradient(to bottom, #121C7B, #0A185F);
            color:white;
        }
        .stVerticalBlock.st-emotion-cache-gsx7k2.eertqu03{
            width:100%;
            max-width:100%;
        }
        .stHorizontalBlock.st-emotion-cache-ajtf3x.eertqu03{
            display: flex;
            justify-content: space-around;
            align-items: center;
            flex-wrap: wrap;
        }
        
        .stColumn.st-emotion-cache-81xr8g.eertqu01{
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .stColumn.st-emotion-cache-81xr8g.eertqu01:hover{
            background-color:white;
            color:black;
           border:1px solid white;
           border-radius: 50px;
           box-shadow: 0 2px 12px rgba(18,28,123,0.15);
        }
        .stColumn.st-emotion-cache-1spjr6t.eertqu01{
            width:100%;
            transition: width 1s cubic-bezier(0.4,0,0.2,1);
        }
    </style>
"""

product_section_styles = """
    <style>
        .stVerticalBlock.st-key-product_section.st-emotion-cache-gsx7k2.eertqu03{
            padding:1rem;
        }
        button.st-emotion-cache-1rwb540.e1e4lema2{
            width:100%;
            border-radius:50px;
        }
        button.st-emotion-cache-1rwb540.e1e4lema2:hover{
            background-image:linear-gradient(to bottom, #565bd5cc, #565bd5);;
            color:white;
            border:1px solid #3137c5;
        }
        button.st-emotion-cache-1rwb540.e1e4lema2:active{
            background-image:linear-gradient(to bottom, #565bd5cc, #565bd5);;
            color:white;
            border:1px solid #3137c5;
        }
        button.st-emotion-cache-1rwb540.e1e4lema2:focus:not(:active){
            border:1px solid #3137c5;
            color:#3137c5;
        }
        button.st-emotion-cache-1rwb540.e1e4lema2:focus-visible{
            box-shadow:#3137c5 0px 0px 0px 0.2rem;
        }
    </style>
"""

fade_in_animation = """
    <style>
        
    </style>
"""

def home_page():
    st.markdown(remove_header_footer,unsafe_allow_html=True)
    st.markdown(navigation_bar_styles,unsafe_allow_html=True)
    st.markdown(category_bar_styles,unsafe_allow_html=True)
    st.markdown(product_section_styles,unsafe_allow_html=True)
    st.markdown(fade_in_animation,unsafe_allow_html=True)
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
                    key = "user_button",
                    on_click=to_signup_page
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

    with st.container(key = "product_section"):
        num_columns = 5
        products = len(st.session_state["products_ids"])
        item_cols = st.columns(num_columns)
        for item in range(products):
            col = item_cols[item % num_columns]
            with col:
                with st.container(key = f"item_box_{item}"):
                    product_id = st.session_state["products_ids"][item]
                    user_product_quantity_index = find_product_quantity_in_user_cart(
                        product_id,
                        st.session_state["user_cart_item"]
                    )
                    product_info = extract_product_by_id(
                        product_id,
                        st.session_state["all_products"]
                    )
                    st.image(product_info["product_image"],use_container_width=True)
                    st.markdown("<br>",unsafe_allow_html=True)
                    st.markdown(f"**{product_info["product_name"]}**")
                    st.markdown("<br>",unsafe_allow_html=True)
                    st.markdown(f"**₹{product_info["product_price"]}**")
                    st.markdown("<br>",unsafe_allow_html=True)
                    st.button(label="View Product", key=f"view_product_{product_id}", type="secondary")
                    st.markdown("<br>",unsafe_allow_html=True)
                    add_to_cart_col, buy_now_col = st.columns(2)

                    with add_to_cart_col:
                        if(user_product_quantity_index is None):
                            st.button(label="Add to Cart",
                                        key=f"add_to_cart_{product_id}",
                                        type="secondary",
                                        on_click=add_to_cart,
                                        args=(product_id,st.session_state["user_cart_item"],)
                            )  
                        else:
                            with st.container(key = f"add_to_cart_qty_{product_id}"):
                                dec_col,qty_col,inc_col = st.columns([0.5,1,0.5])
                                with dec_col:

                                    st.button(
                                        type="tertiary",
                                        label="",
                                        icon=":material/remove:",
                                        key = f"dec_cart_{product_id}"
                                    )
                                with qty_col:
                                    st.markdown(f"<p id = 'quantity'>{find_the_quantity_of_product_in_cart(user_product_quantity_index,st.session_state["user_cart_item"])}</p>",unsafe_allow_html=True)
                                with inc_col:

                                    st.button(
                                        type="tertiary",
                                        label="",icon=":material/add:",
                                        key = f"inc_cart_{product_id}"
                                    )

                        st.markdown("<br>",unsafe_allow_html=True)
                    with buy_now_col:
                        st.button(label="Buy Now", key=f"buy_now_button_{product_id}", type="secondary")
                        st.markdown("<br>",unsafe_allow_html=True)
    
        