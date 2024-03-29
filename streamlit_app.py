import streamlit as st
import jaydebeapi

def login_page():
    # Set page config to wide layout and set the page background color
    st.set_page_config(layout="wide", page_title="Login Page", page_icon="🔒", 
                       initial_sidebar_state="collapsed")
    # Set the background color
    st.markdown(
        """
        <style>
        body {
            background-color: #7FFFD4; /* Aquamarine color */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Title
    st.title("Welcome to our App")
    
    # Login Section
    st.write("Please login to continue:")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "user" and password == "password":
            st.success("Logged In as {}".format(username))
            return True
        else:
            st.error("Invalid Username or Password")
    return False

def data_operations():
    # Set page config to wide layout and set the page background color

    # Set the background color
    st.markdown(
        """
        <style>
        body {
            background-color: #7FFFD4; /* Aquamarine color */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Title
    st.title("Data Operations")
    
    # Data Input Section
    st.write("Please enter the values of A and B:")
    A = st.number_input("Value of A", value=0)
    B = st.number_input("Value of B", value=0)
    
    if st.button("Execute"):
        result = A + B
        st.success(f"The result of {A} + {B} is {result}")

def main():
    if login_page():
        data_operations()

if __name__ == "__main__":
    main()

