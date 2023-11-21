import streamlit as st
from admin import admin_request
from employee import employee_request
from ceo import ceo_request
from manager import manager_request
st.title("Your Request Page")
st.write("Welcome to the dashboard, user!")
if st.session_state.usertype == "admin":
    admin_request()
if st.session_state.usertype == "user":
    employee_request()
if st.session_state.usertype == "manager":
    manager_request()
if st.session_state.usertype == "ceo":
    ceo_request()    