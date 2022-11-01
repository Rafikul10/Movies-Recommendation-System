import streamlit as st
import pandas as pd
import sqlite3
import streamlit as st
from streamlit_option_menu import option_menu


# 1 slider menu
selected = option_menu(menu_title =None,
                           options=['Feedback','Troubleshooting','Users Database'],
                           icons = ['','exclamation-triangle','file-lock'],
                           orientation='horizontal',
                           styles={ 
                            "container": {"padding": "0!important", "background-color": "#000000"},
                            "icon": {"color": "white", "font-size": "15px"}, 
                            "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#4a4a4a"},
                            "nav-link-selected": {"background-color": '#9277E8'},
                                }
                    )
# for feed back page
if selected == 'Feedback':
    st.subheader('Feedback Form')
    st.caption('''Thank you! for visiting the Application. I would love to hear about your experience,
               simply fill out this form and hit submit.
               ''')  
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    def create_table(): 
        c.execute('CREATE TABLE IF NOT EXISTS feedback( Q1 TEXT, Q2 TEXT, date_submitted DATE, Q3 TEXT)')

    def add_feedback(Q1, Q2, date_submitted, Q3 ):  
        c.execute('INSERT INTO feedback (Q1, Q2, date_submitted, Q3) VALUES (?,?,?,?)',(Q1, Q2, date_submitted, Q3))
        conn.commit()

    def main(): 
    # Title of the form
    # First question to ask 
        question_1 = st.text_input('Username',placeholder='name')
    # Display the answer of first question
   
        question_2 = st.text_input('Email Id',placeholder='email')
    # Dispaly the answer of second question
    #st.write('You Email id:', question_2)
    # Thircd question to be ask
        d = st.date_input("Today's date",None, None, None, None)
        question_3 = st.text_area('What could have been better?',placeholder='text..')
        if st.button('Submt feedback'):
            
            create_table()
            add_feedback(question_1,question_2,d,question_3)
            st.success('Feedback submitted')

        # lines I added to display your table
            query = pd.read_sql_query('''
            select * from feedback''', conn)

            data = pd.DataFrame(query)
            #st.write(data)
    if __name__ == '__main__':
        main()    
        
           
# for troubleshooting page                       
if selected == 'Troubleshooting':
    st.subheader('Troubleshooting Form')
    
    st.caption('''Troubleshooting is a form of problem solving, if you have an any issue to use this Application simply fill out this form and hit submit
               . I will look into it as soon as possible.
               ''') 
    st.caption('''**INFO :** If you got some error message like this **' list index out of range'** then it's the problem 
                   of the website **TMDB** from where i collected the data beacuse i checked that there some data
                   is missing beacuse of the missing data it's showing an error. I can't fixed this issue.
                   Hope you understand...Thank You!''')                         
                       
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()

    def create_table(): 
        c.execute('CREATE TABLE IF NOT EXISTS feedback( Q1 TEXT, Q2 TEXT, date_submitted DATE, Q3 TEXT)')

    def add_feedback(Q1, Q2, date_submitted, Q3 ):  
        c.execute('INSERT INTO feedback (Q1, Q2, date_submitted, Q3) VALUES (?,?,?,?)',(Q1, Q2, date_submitted, Q3))
        conn.commit()

    def main(): 
    # Title of the form
    # First question to ask 
        question_1 = st.text_input('Username',placeholder='name')
    # Display the answer of first question
   
        question_2 = st.text_input('Email Id',placeholder='email')
        d = st.date_input("Today's date",None, None, None, None)
        question_3 = st.text_area('''Write your problems in detail - ''')
        if st.button('Submt report'):
            
            create_table()
            add_feedback(question_1,question_2,d,question_3)
            st.success('Report submitted')
        
        
        # lines I added to display your table
            query = pd.read_sql_query('''
            select * from feedback''', conn)

            data = pd.DataFrame(query)
            #st.write(data)
    if __name__ == '__main__':
        main()
        
#user data fetch         
connection = sqlite3.connect("user_data.db")  
crsr = connection.cursor()
conn = sqlite3.connect('feedback.db')
_conect_queries = sqlite3.connect('queries.db')

# for user data base page

if selected == 'Users Database':
    
    st.subheader('Datbase Of Users')
    st.caption('''''')
    st.write('''Database is **encrypted**, Only admin can access the database.''')
    st.caption('''_Formally, a "database" refers to a set of related data and the way 
               it is organized.  Access to this data is usually provided by a "database
               management system" (DBMS) consisting of an integrated set of computer 
               software that allows users to interact with one or more databases and 
               provides access to all of the data contained in the database (although 
               restrictions may exist that limit access to particular data). 
               The DBMS provides various functions that allow entry, storage and 
               retrieval of large quantities of information and provides ways to 
               manage how that information is organized.If you have an admin access
               then access database with the secure key to see the data._''')
    admin_key = st.text_input('Secure Key', placeholder='key...', type='password')
    Password = 'admin$8910'
    if st.button('Access'):
        
        if admin_key == Password:
            st.markdown('''<h8 style = 'text-align:left; color: green; opacity: 70%'> _🔓Access Granted_</h8>''',unsafe_allow_html=True)
            st.write('----')
            
            query = pd.read_sql_query('''select * from feedback''', conn)
            query2 = pd.read_sql_query('''select * from queries''', _conect_queries)
            query3 = pd.read_sql_query('''select * from userstable''', connection)
            
            data1 = pd.DataFrame(query)
            data2 = pd.DataFrame(query2)
            data3 = pd.DataFrame(query3)
            
            st.subheader('🗒️Database of Feedbacks and Reports -')
            # check = st.checkbox('Explore the data by clicking on checkbox')
            st.dataframe(data1)
            st.write('---')
            
            st.subheader('❓ Queries table -')
            st.dataframe(data2)
            st.write('---')
            
            st.subheader('🛢 Database of all Users -')
            st.dataframe(data3)
            st.write('---')
            
        else:
            st.markdown('''<h8 style = 'text-align:left; color: red; opacity: 70%'>_Wrong **key!** access request declined ,Contact with the admin for key_</h8>''',
                        unsafe_allow_html=True)
            st.write('------')
            st.subheader('📬 Contact Details')
            st.caption('_Contact with the admin for secure key!!_')
            st.write(f'📧 ' ,' rafikul.official10@gmail.com',type='mail')
            st.write("👾  [GitHub](https://github.com/Rafikul10?tab=repositories)")
                