import streamlit as st
# Hardcoded credentials (for demo purposes)
correct_username ={"peng_admin":"admin","peng_user":"user","peng_manager":"manager","peng_ceo":"ceo"}
login,options=st.empty(),st.empty()
class SessionState:
    def __init__(self):
        self.conn = None
        self.data_inserted = False
if "auth" not in st.session_state:
    st.session_state.auth = 0
# Get user input
def login1():
    st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
    with login.container():
        st.title("IT Infrastructure Management Software - Login")
        username = st.text_input("Username:", key="user")
        password = st.text_input("Password:", type="password")
        if st.button("Login"):
            if username in correct_username and password == correct_username[username]:
                st.success("Login Successful!")
                st.session_state.auth = 1
                st.session_state.usertype = username.split("_")[1]
                login.empty()
                options.empty()
            else:
                st.error("Invalid Username or Password")
# Display login form
if st.session_state.auth == 0:
    login1()
# Redirect to dashboard if logged in
def show_user():
    if st.session_state.usertype == "admin":
        radio1= st.sidebar.radio("",("View","Add User"))
        if radio1 =="Add User":    
                st.write("Add new user:")
                st.text_input("First Name:")
                st.text_input("Last Name:")
                st.text_input("Username:", key="user_registeration")
                st.text_input("Password:",key="password_registeration")
                st.text_input("Confirm Password:")
                st.selectbox("User Type:", ("User", "Manager", "CEO"))
                button = st.button("Add User")
                if button:
                    st.write("User added!")
        if radio1 =="View":
            st.title("User Dashboard")
            st.write("Welcome to the dashboard, user!")
            st.write("This is a demo of how the dashboard would look like for a user.")
            st.write("You can use the sidebar to navigate to different pages.")
            if st.button("Logout"):
                st.session_state.auth = 0
                st.session_state.usertype = ""
                st.experimental_rerun()
    else :
        st.title("User Dashboard")
        st.write("Welcome to the dashboard, user!")
        st.write("This is a demo of how the dashboard would look like for a user.")
        st.write("You can use the sidebar to navigate to different pages.")
        if st.button("Logout"):
                st.session_state.auth = 0
                st.session_state.usertype = ""
                st.experimental_rerun()
if st.session_state.auth == 1:
    show_user()
    st.markdown("<style> ul {display: block;} </style>", unsafe_allow_html=True)