import streamlit as st
import sqlite3
import bcrypt

# Function to create a SQLite database and users table
def create_db():
    conn = sqlite3.connect('users.db')  # Connect to SQLite database (or create it if it doesn't exist)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY, 
                        password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Function to register a new user
def register_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Check if username already exists
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        return False  # User already exists
    
    # Hash the password before storing it
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    # Insert the new user into the database
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                   (username, hashed_password))
    conn.commit()
    conn.close()
    return True

# Function to authenticate a user during login
def authenticate_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    if st.button("select"):
            apple=cursor.execute("SELECT * FROM users " )
            st.write("apple")
    # Query the database for the given username
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    
    # If user exists and password matches the hash
    if user and bcrypt.checkpw(password.encode('utf-8'), user[1]):
        return True
    return False

# Function to display the login page
def login_page():
    st.title("Login Page")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        if authenticate_user(username, password):
            st.success("Login successful!")
            st.write(f"Welcome, {username}!")
            home_page()  # Redirect to the home page if login is successful
        else:
            st.error("Invalid username or password.")

# Function to display the signup page
def signup_page():
    st.title("Signup Page")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    confirm_password = st.text_input("Confirm Password", type='password')
    
    if st.button("Signup"):
        if password != confirm_password:
            st.error("Passwords do not match!")
        elif register_user(username, password):
            st.success("User registered successfully!")
            st.write("Now, you can log in with your credentials.")
           # login_page()  # Redirect to login page after successful registration
        else:
            st.error("Username already exists. Please choose a different username.")
    

# Function to display the home page after successful login
def home_page():
    st.title("Home Page")
    st.write("Welcome to the home page!")

# Main function to control navigation between pages
def main():
    create_db()  # Ensure the database and table are created at the start
    
    # Display the choice of either login or signup
    page = st.selectbox("Choose an option", ["Login", "Signup"])
    
    if page == "Login":
        login_page()
    elif page == "Signup":
        signup_page()

# Run the app
if __name__ == "__main__":
    main()



