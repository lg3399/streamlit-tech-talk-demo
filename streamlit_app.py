import streamlit as st

# page setup
hide_st_style ="""
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)
about_page = st.Page(
    page="pages/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

chatbot_page = st.Page(
    page="pages/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)

dashboard_page = st.Page(
    page="pages/sales_dashboard.py",
    title="Dashboard",
    icon=":material/bar_chart:",
)

# nav
pg = st.navigation(
    {
        "info": [about_page],
        "Projects":[dashboard_page,chatbot_page]
    }
)

# logo
st.logo("assets/trust-the-idea-logo.png")
st.sidebar.text("Built using Streamlit")
# run nav

pg.run()
