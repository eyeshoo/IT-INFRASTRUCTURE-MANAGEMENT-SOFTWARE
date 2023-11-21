import streamlit as st
import plotly.express as px
import pandas as pd
import streamlit as st
from admin import display_resource_utilization2
from admin import display_admin_dashboard
from admin import display_resource_utilization
from employee import display_employee_dashboard
from manager import display_team_resource_allocation_chart
from manager import display_expenditure_status
from ceo import display_expenditure_overview
from ceo import display_project_progress
from ceo import display_detailed_reports

st.title("Your View Page")
st.write("Welcome to the dashboard, user!")
if st.session_state.usertype == "admin":
    st.write("This is a demo of how the dashboard would look like for an admin")
    st.write("View of all resources being used:")
    display_admin_dashboard()
    display_resource_utilization2()
if st.session_state.usertype == "user":
    st.write("This is a demo of how the dashboard would look like for a user")
    st.write("View of all your resources being used:")
    display_employee_dashboard()
if st.session_state.usertype == "manager":
    st.write("This is a demo of how the dashboard would look like for a manager")
    st.write("View of all your teams resources being used:")
    options = st.selectbox("Navigation", ("Team Resource Allocation", "Expenditure Status"))
    if options == "Team Resource Allocation":
        display_team_resource_allocation_chart()
    if options == "Expenditure Status":
        display_expenditure_status()
if st.session_state.usertype == "ceo":
    st.write("This is a demo of how the dashboard would look like for a CEO")
    st.write("View of all resources in the company being used:")
    options = st.selectbox("Navigation", ("Project Progress", "Expenditure Overview", "Detailed Reports"))
    if options == "Project Progress":
        display_project_progress()
    if options == "Expenditure Overview":
        display_expenditure_overview()
    if options == "Detailed Reports":
        display_detailed_reports()