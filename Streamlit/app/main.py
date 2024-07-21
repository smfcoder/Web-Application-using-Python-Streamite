import streamlit as st
import sqlite3
import time

# Function to create a table in SQLite database if it doesn't exist
def create_table():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS data
                (name TEXT, email TEXT)''')
    conn.commit()
    conn.close()

# Function to insert data into the database
def insert_data(name, email):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO data (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

# Function to retrieve all data from the database
def get_data():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM data")
    data = c.fetchall()
    conn.close()
    return data

# Main function to run the Streamlit app
def main():
    st.title('Simple Input Form with SQLite Backend')

    # Create table if not exists
    create_table()

    # Input fields for name and email
    name = st.text_input('Enter your name:')
    email = st.text_input('Enter your email:')

    # Button to submit data
    if st.button('Submit'):
        insert_data(name, email)
        success_message = st.success('Data inserted successfully!')

        # Remove success message after 5 seconds
        with st.spinner('Removing message...'):
            time.sleep(2)  # Simulate a delay (you may use st.timeout instead)
            success_message.empty()

    # Display all data in the database
    st.title('Stored Data')
    data = get_data()
    if data:
        st.write(data)
    else:
        st.write('No data found.')

if __name__ == '__main__':
    main()
