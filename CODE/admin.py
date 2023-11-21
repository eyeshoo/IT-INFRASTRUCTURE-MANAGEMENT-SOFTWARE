import plotly.express as px
import pandas as pd
import streamlit as st

# Dummy Data for Resource Utilization
utilization_data = {
    'Resource': ['Server', 'Storage', 'Network'],
    'Date': ['2023-07-01', '2023-07-02', '2023-07-03'],
    'Utilization': [80, 60, 90],
    'Project': ['Project A', 'Project B', 'Project C'],
}

df_utilization = pd.DataFrame(utilization_data)

def display_admin_dashboard():
    st.title("Admin Dashboard")

    # Display Resource Utilization Heatmap
    display_resource_utilization()

    # # Display Total Resources, Resources Used, Resources Remaining
    # st.subheader("Resource Summary")
    # total_resources = df_utilization['Resource'].nunique()
    # resources_used = df_utilization['Resource'].count()
    # resources_remaining = total_resources - resources_used

    # st.write(f"Total Resources: {total_resources}")
    # st.write(f"Resources Used: {resources_used}")
    # st.write(f"Resources Remaining: {resources_remaining}")

    # Display Project for Each Resource
    # st.subheader("Project-wise Resource Utilization")
    # st.table(df_utilization[['Resource', 'Project']].drop_duplicates())

    # Display Resource Availability and Utilization Percentage
    st.subheader("Resource Availability and Utilization Percentage")
    fig_resource_utilization = px.bar(df_utilization.groupby('Resource').agg({'Utilization': 'mean'}).reset_index(),
                                       x='Utilization',
                                       y='Resource',
                                       orientation='h',
                                       title='Resource Availability and Utilization Percentage',
                                       labels={'Utilization': 'Utilization Percentage (%)', 'Resource': 'Resource'})

    st.plotly_chart(fig_resource_utilization)

def display_resource_utilization():
    st.subheader("Resource Utilization Heatmap")
    st.write("This heatmap shows the utilization of resources across the entire organization.")

    df_utilization['Date'] = pd.to_datetime(df_utilization['Date'])

    fig_utilization_heatmap = px.imshow(df_utilization.pivot(index='Resource',columns= 'Date', values='Utilization'),
                                        x=df_utilization['Date'].dt.strftime('%Y-%m-%d'),
                                        y=df_utilization['Resource'],
                                        color_continuous_scale="Viridis",
                                        title='Resource Utilization Heatmap')

    st.plotly_chart(fig_utilization_heatmap)

#display_admin_dashboard()


utilization_data1 = {
    'Resource': ['Server', 'Storage', 'Network'],
    'Project A': [60, 60, 90],
    'Project B': [20, 60, 90],
    'Project C': [20, 60, 90],
}

df_utilization1 = pd.DataFrame(utilization_data1)

def display_resource_utilization2():
    st.title("Resource Utilization by Project")
    st.write("This visualization shows the utilization of resources for each project.")

    df_melted = pd.melt(df_utilization1, id_vars='Resource', var_name='Project', value_name='Utilization')

    fig = px.bar(df_melted, x='Resource', y='Utilization', color='Project',
                 title='Resource Utilization by Project',
                 labels={'Utilization': 'Utilization Percentage (%)', 'Resource': 'Resource'})

    st.plotly_chart(fig)

# Display Resource Utilization
#display_resource_utilization2()

def admin_request():
    st.write("This is a demo of how the dashboard would look like for an admin")
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
        if st.button("Allocate"):
            st.write("Request allocated!")