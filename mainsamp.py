import streamlit as st
from streamlit_navigation_bar import st_navbar
from streamlit_option_menu import option_menu
import account, your, about, sample2

img="logo.png"
st.set_page_config(page_title="MoodMatrix", page_icon=img, initial_sidebar_state="collapsed")

pages = ["Home","About"]
styles = {
	"nav": {
		"background-color": "rgba(0, 0, 0, 0)",
	},
	"div": {
		"max-width": "31.25rem",
	},
	"span": {
		"color": "var(--text-color)",
		"border-radius": "0.5rem",
		"padding": "0.4375rem 0.625rem",
		"margin": "0 0.125rem",
	},
	"active": {
		"background-color": "rgba(55, 73, 79, 1)",
	},
	"hover": {
		"background-color": "rgba(50, 42, 35, 1)",
	},
}

page = st_navbar(pages, styles=styles)
if page=="About":
    about.app()
else:
    pass

    
col1, col2, col3 = st.columns([1, 2, 1])  # Adjust column widths as needed
with col2:
  st.image("logo.png")

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='MoodMatrix ',
                options=['Analyze','Account','Your Posts'],
                icons=['activity','person-circle','trophy-fill'],
                menu_icon='logo.png',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "rgba(50, 42, 35, 1)"},
        "nav-link-selected": {"background-color": "rgba(55, 73, 79, 1)"},}
                
                )

        
        if app == "Analyze":
            sample2.main()
        if app == "Account":
            account.app()       
        if app == 'Your Posts':
            your.app()
             
          
    run()     
    

