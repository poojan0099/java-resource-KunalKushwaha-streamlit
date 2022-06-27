import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
import show_programs,video_tutorial,landing_page,contribute,about_me,resources

PAGES = {
    "Home": landing_page,
    "Programs": show_programs,
    "Video Tutorials": video_tutorial,
    "Resources": resources,
    "Contribute": contribute,
    "Contact": about_me
}

with st.sidebar:
    choose = option_menu("Navigation", ["Programs", "Video Tutorials", "Resources", "Contribute", "Contact"],
                         icons=['code-slash', 'camera-video', 'file-earmark', 'pen','person lines fill'],
                         #menu_icon="app-indicator", default_index=0,   
                         styles={
        "container": {"padding": "5!important", "background-color": "#0E1117"},
        "icon": {"color": "#C9403A", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "black"},
        "nav-link-selected": {"background-color": "#0E1117"},
    }
    )

page = PAGES[choose]
page.app()