# Setup
import json
import sqlite3
import hashlib
import requests
import streamlit as st
from pathlib import Path
from streamlit_lottie import st_lottie
from streamlit_extras.switch_page_button import switch_page
from streamlit.source_util import _on_pages_changed, get_pages


DEFAULT_PAGE = "1_🔐_Login.py"
SECOND_PAGE_NAME = "Home"

# all pages request
def get_all_pages():
    default_pages = get_pages(DEFAULT_PAGE)

    pages_path = Path("pages.json")

    if pages_path.exists():
        saved_default_pages = json.loads(pages_path.read_text())
    else:
        saved_default_pages = default_pages.copy()
        pages_path.write_text(json.dumps(default_pages, indent=4))

    return saved_default_pages

# clear all page but not login page
def clear_all_but_first_page():
    current_pages = get_pages(DEFAULT_PAGE)

    if len(current_pages.keys()) == 1:
        return

    get_all_pages()

    # Remove all but the first page
    key, val = list(current_pages.items())[0]
    current_pages.clear()
    current_pages[key] = val

    _on_pages_changed.send()

# show all pages
def show_all_pages():
    current_pages = get_pages(DEFAULT_PAGE)

    saved_pages = get_all_pages()

    # Replace all the missing pages
    for key in saved_pages:
        if key not in current_pages:
            current_pages[key] = saved_pages[key]

    _on_pages_changed.send()

# Hide default page
def hide_page(name: str):
    current_pages = get_pages(DEFAULT_PAGE)

    for key, val in current_pages.items():
        if val["page_name"] == name:
            del current_pages[key]
            _on_pages_changed.send()
            break

# calling only default(login) page  
clear_all_but_first_page()


# Convert Pass into hash format
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


# Check password matches during login
def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

# DB Management
conn = sqlite3.connect("user_data.db")
c = conn.cursor()

# DB Functions for create table
def create_usertable():
    c.execute(
        "CREATE TABLE IF NOT EXISTS userstable(username TEXT,email TEXT, password TEXT)"
    )

# Insert the data into table
def add_userdata(username, email, password):
    c.execute(
        "INSERT INTO userstable(username,email,password) VALUES (?,?,?)",
        (username, email, password),
    )
    conn.commit()

# Password and email fetch
def login_user(email, password):
    c.execute(
        "SELECT * FROM userstable WHERE email =? AND password = ?", (email, password)
    )
    data = c.fetchall()
    return data

# View all user data
def view_all_users():
    c.execute("SELECT * FROM userstable")
    data = c.fetchall()
    return data

# session state 
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    

# lottie animation 
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# url of littie
lotti_ur = load_lottieurl('https://assets1.lottiefiles.com/packages/lf20_M9p23l.json')

left,col1, col2 = st.columns([0.1,1,1])
with col2:
    st_lottie(lotti_ur,
          speed = 1,
          key=None,
          height=300,
          width=300,
          quality='high',
          reverse=False
          )
with col1:
    st.markdown("<h2 style='text-align: center; color: #C059C0;'> Welcome!</h2>", unsafe_allow_html=True)
    st.write('-----')
    
    st.caption('''<h6 style='text-align: left; color: #fffff;opecity: 50%'>This is a secured Movies 
               Recommendation Web Application. Based on your past choices and behavior it will be suggest five 
               movies. And also you can check out top TV Shows. To use it Login with your email and 
               password. If you don't have an Account just create an Account by selecting Signup option 
               from the dropdown box!</h6>''',unsafe_allow_html=True)
   
st.write('-----')

# Main function
def main():
    # """Login page"""
    menu = ["Login", "SignUp"]
    choice = st.selectbox(
        "Select one option ▾",
        menu,
    )
    # Default choice
    if choice == "":
        st.subheader("Login")
    # if chice login
    elif choice == "Login":
        st.write("-------")
        # st.subheader("Log in")
        with st.form('Login'):
            email = st.text_input("Email Id", placeholder="email")
            password = st.text_input("Password", type="password")
            login_button = st.form_submit_button('Login')
            
            if login_button:
                # if password == '12345':
                # Hash password creation and store in a table
                create_usertable()
                hashed_pswd = make_hashes(password)
                result = login_user(email, check_hashes(password, hashed_pswd))
                
                if result:
                    st.session_state["logged_in"] = True
                    st.success("Logged In Sucessfully")
                else:
                    st.warning("Incorrect Email Id/Password")
    
    elif choice == "SignUp":
        st.write("-----")
        st.subheader("Create New Account")
        with st.form('Create New Account'):
            new_user = st.text_input("Username", placeholder="name")
            new_user_email = st.text_input("Email id", placeholder="email")
            new_password = st.text_input("Password", type="password")
            signup_button = st.form_submit_button('SignUp')
            
            if signup_button:
                
                if new_user == "":  # if user name empty then show the warnings
                    st.warning("Inavlid user name")
                elif new_user_email == "":  # if email empty then show the warnings
                    st.warning("Invalid email id")
                elif new_password == "":  # if password empty then show the warnings
                    st.warning("Invalid password")
                else:
                    create_usertable()
                    add_userdata(new_user, new_user_email, make_hashes(new_password))
                    st.success("You have successfully created a valid Account!")
                    st.info("Go up and Login to you account.")
    # session state checking
    if st.session_state["logged_in"]:
        show_all_pages()  # call all page
        hide_page(DEFAULT_PAGE.replace(".py", ""))  # hide first page
        switch_page(SECOND_PAGE_NAME)   # switch to second page
    else:
        clear_all_but_first_page()  # clear all page but show first page


if __name__ == "__main__":
    main()

