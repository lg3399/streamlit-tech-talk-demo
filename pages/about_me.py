import streamlit as st

st.write("A faster way to build and share data apps")

st.write("Streamlit build upon 3 simple principles")

from forms.contact import contact_form
@st.dialog("Principles")
def show_contact_form():
    contact_form()

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("assets/trust-the-idea-logo.png", width= 200)
with col2:
    st.title("Streamlit App")
    st.write("Turn your data scripts into shareable web apps in minutes, all in pure Python. No front end experience required. Streamlit is an open-source app framework that is a breeze to get started with. Just install it like any other Python library")
    if st.button("Contact Me"):
        show_contact_form()