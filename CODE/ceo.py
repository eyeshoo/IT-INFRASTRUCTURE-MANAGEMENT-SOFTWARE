import streamlit as st
import pandas as pd
import plotly.express as px

# Dummy Data
project_data = {
    'Project': ['Project A', 'Project B', 'Project C'],
    'Progress': [75, 60, 90],
}

df_projects = pd.DataFrame(project_data)

# Dummy Data for Expenditure
expenditure_data = {
    'Category': ['Servers', 'Hardware', 'Software'],
    'Expenditure': [250000, 100000, 50000],
}

df_expenditure = pd.DataFrame(expenditure_data)

def display_project_progress():
    st.subheader("Project Progress Overview")
    st.write("This section shows the progress of ongoing projects.")

    fig = px.bar(df_projects, x='Progress', y='Project', orientation='h', title='Project Progress Overview')
    st.plotly_chart(fig)

def display_expenditure_overview():
    st.subheader("Expenditure Overview")
    st.write("This section provides a high-level overview of the total expenditure.")

    fig = px.pie(df_expenditure, values='Expenditure', names='Category', title='Expenditure Distribution')
    st.plotly_chart(fig)

def display_detailed_reports():
    st.subheader("Detailed Financial Reports")
    st.write("View detailed financial reports for a more granular analysis.")

    fig = px.bar(df_expenditure, x='Category', y='Expenditure', title='Detailed Financial Reports')
    st.plotly_chart(fig)



def ceo_request():
    st.write("This is a demo of how the dashboard would look like for a CEO")