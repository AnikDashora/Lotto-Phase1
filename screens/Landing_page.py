import streamlit as st
import time

def landing_page():
    st.markdown(
        """
        <style>
        /* Hide Streamlit header, main menu, and footer */
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

        /* Center content using flexbox */
        section[data-testid="stMain"] {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            min-height: 80vh;
        }

        /* Typing animation for tagline, repeats infinitely */
        #ab-nahi-loge-tho-kab {
            display: inline-block;
            white-space: nowrap;
            overflow: hidden;
            border-right: 2px solid black;
            color: black;
            font-size: 1.5rem;
            width: 0;
            animation: typing 3s steps(25, end) 0.75s forwards, blink 100s step-end infinite;
            animation-iteration-count: infinite;
        }

        @keyframes typing {
            0% { width: 0% }
            80% { width: 10.5em }
            100% { width: 10.5em }
        }
        @keyframes blink {
            50% { border-color: transparent }
        }
        </style>
        
        """,
        unsafe_allow_html=True,
    )

    st.header("Welcome to LOTTO")
    tag_line = "Ab nahi loge tho kab....."
    st.subheader(tag_line)
    start_button_flag = st.button("Let's start")
    if(start_button_flag):
        st.session_state["page"] = "auth_page"
        st.rerun()