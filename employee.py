import plotly.express as px
import pandas as pd
import streamlit as st

# Dummy Data for Employee Resources
resources_data = {
    'Resource': ['Laptop', 'Desktop', 'Tablet'],
    'Status': ['In Use', 'In Use', 'Available'],
}

df_resources = pd.DataFrame(resources_data)

# Dummy Data for Employee Tasks
tasks_data = {
    'Task': ['Task A', 'Task B', 'Task C'],
    'Start Date': ['2023-07-01', '2023-07-05', '2023-07-10'],
    'End Date': ['2023-07-07', '2023-07-12', '2023-07-15'],
    'Status': ['Completed', 'In Progress', 'Not Started'],
}

df_tasks = pd.DataFrame(tasks_data)

def display_employee_dashboard():
    st.title("Employee Dashboard")

    st.subheader("Allocated Resources")
    st.table(df_resources)

    df_tasks['Start Date'] = pd.to_datetime(df_tasks['Start Date'])
    df_tasks['End Date'] = pd.to_datetime(df_tasks['End Date'])

    color_mapping = {'Completed': 'green', 'In Progress': 'orange', 'Not Started': 'red'}

    st.subheader("Tasks Overview")
    fig_tasks_timeline = px.timeline(df_tasks, x_start='Start Date', x_end='End Date', y='Task',
                                     color='Status',
                                     color_discrete_map=color_mapping,
                                     labels={'Task': 'Project Tasks'},
                                     title='Tasks Overview')

    st.plotly_chart(fig_tasks_timeline)


#display_employee_dashboard()

def employee_request():
    st.write("This is a demo of how the dashboard would look like for a user")
    st.write("Request for new resources:")
    option = st.radio("",("Server","Storage","Network"))
    if option == "Server":
        server_memory=st.text_input("Server memory:")
        if st.button("Submit"):
            st.write("Request submitted!")
    if option == "Storage":
        storage_memory=st.text_input("Storage memory:")
        if st.button("Submit"):
            st.write("Request submitted!")
    if option == "Network":
        network_memory=st.text_input("Network memory:")
        if st.button("Submit"):
            st.write("Request submitted!")