import streamlit as st
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

cart_items = [
    {"product_id":"p0001","Quantity":4},
    {"product_id":"p0002","Quantity":2},
    {"product_id":"p0003","Quantity":3},
    {"product_id":"p0004","Quantity":4},
    {"product_id":"p0005","Quantity":5},
    {"product_id":"p0006","Quantity":41},
    {"product_id":"p0007","Quantity":46},
    {"product_id":"p0008","Quantity":7},
    {"product_id":"p0009","Quantity":8},
    {"product_id":"p0011","Quantity":44},
    {"product_id":"p0041","Quantity":43},
]

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


def cart_page():
    st.markdown(remove_header_footer,unsafe_allow_html=True)
    st.markdown(navigation_bar_styles,unsafe_allow_html=True)

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
                )

    with st.container(key = "category_bar_section"):
        category_bar_col = st.columns(10)
        for category in range(10):
            with category_bar_col[category]:
                st.button(
                    label=st.session_state["categories"][category],
                    type="tertiary",
                    help = f"**{st.session_state["categories"][category]}**",
                    key = f"{st.session_state["categories"][category]}_button",
                    args=(st.session_state["categories"][category],)
                )



                    
                    


    


cart_page()
