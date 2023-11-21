import plotly.express as px
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# Dummy Data
team_data = {
    'TeamMember': ['Employee A', 'Employee B', 'Employee C'],
    'AllocatedResources': [120, 90, 110],
}

df_team_allocation = pd.DataFrame(team_data)

def display_team_resource_allocation_chart():
    st.subheader("Team Resource Allocation Overview")
    st.write("This horizontal bar chart shows the allocation of resources across team members.")

    fig = px.bar(df_team_allocation, x='AllocatedResources', y='TeamMember', orientation='h',
                 title='Team Resource Allocation Overview')
    st.plotly_chart(fig)

#display_team_resource_allocation_chart()


# Dummy Data
project_progress_data = {
    'Project': ['Project X', 'Project Y', 'Project Z'],
    'Progress': [75, 60, 90],
}




# Dummy Data
expenditure_data = {
    'Category': ['Servers', 'Hardware', 'Software'],
    'Allotted': [200000, 50000, 100000],
    'Used': [150000, 30000, 80000],
}

df_expenditure = pd.DataFrame(expenditure_data)

def display_expenditure_status():
    st.subheader("Project Expenditure Status")
    st.write("This visualization shows the allotted expenditure and how much of it is used for a project.")

    fig_expenditure = px.bar(df_expenditure, x='Category', y=['Allotted', 'Used'],
                             title='Expenditure Overview',
                             labels={'value': 'Amount (in USD)'},
                             color_discrete_map={'Allotted': 'blue', 'Used': 'orange'})

    st.plotly_chart(fig_expenditure)

#display_expenditure_status()




# Dummy Data
tasks_data = {
    'Task': ['Task A', 'Task B', 'Task C'],
    'Start Date': ['2023-07-01', '2023-07-05', '2023-07-10'],
    'End Date': ['2023-07-07', '2023-07-12', '2023-07-15'],
    'Status': ['Completed', 'In Progress', 'Not Started'],
}

df_tasks = pd.DataFrame(tasks_data)

def display_tasks_timeline():
    st.subheader("Project Tasks Timeline")
    st.write("This Gantt chart shows the timeline of tasks for a project.")

    df_tasks['Start Date'] = pd.to_datetime(df_tasks['Start Date'])
    df_tasks['End Date'] = pd.to_datetime(df_tasks['End Date'])

    color_mapping = {'Completed': 'green', 'In Progress': 'orange', 'Not Started': 'red'}

    fig_tasks_timeline = px.timeline(df_tasks, x_start='Start Date', x_end='End Date', y='Task',
                                     color='Status',
                                     color_discrete_map=color_mapping,
                                     labels={'Task': 'Project Tasks'},
                                     title='Tasks Timeline Overview')

    st.plotly_chart(fig_tasks_timeline)

#display_tasks_timeline()

def manager_request():
    st.write("This is a demo of how the dashboard would look like for a manager")
    radio1= st.sidebar.radio("",("Approve Request","Launch Request"))  
    if radio1 == "Launch Request":    
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
    if radio1 == "Approve Request":
        st.write("All requests:")
        st.write("Request 1")
        st.write("Request 2")
        st.write("Request 3")
        st.write("Request 4")
        dropdown = st.selectbox("Select request:",("Request 1","Request 2","Request 3","Request 4"))
        if st.button("Approve"):
            st.write("Request approved!")