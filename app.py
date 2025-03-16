import streamlit as st

# In-memory data to simulate a database
data = {
    "1": {"name": "John Doe", "age": 30},
    "2": {"name": "Jane Smith", "age": 25}
}

# App title with an emoji
st.title("Simple API with Streamlit 🧑‍💻")

# Sidebar with options
st.sidebar.title("Choose an operation 🛠️")
operation = st.sidebar.selectbox(
    "Select operation", 
    ("View All Users", "View User", "Add User", "Update User", "Delete User")
)

# Function to show all users
def show_users():
    st.subheader("All Users 📜")
    if data:
        for user_id, user_info in data.items():
            st.write(f"**User ID**: {user_id}")
            st.write(f"**Name**: {user_info['name']} 🧑‍💼")
            st.write(f"**Age**: {user_info['age']} years 🎂")
            st.write("---")
    else:
        st.write("No users available ❌")

# Function to show a specific user by ID
def show_user(user_id):
    user = data.get(user_id)
    if user:
        st.subheader(f"User Details 🧑‍💼 (ID: {user_id})")
        st.write(f"**Name**: {user['name']} 🧑‍💼")
        st.write(f"**Age**: {user['age']} years 🎂")
    else:
        st.write(f"**User not found! ❌**")

# Function to add a new user
def add_user():
    st.subheader("Add a New User ✨")
    new_name = st.text_input("Enter name: ")
    new_age = st.number_input("Enter age: ", min_value=1)
    
    if st.button("Add User ✅"):
        if new_name and new_age:
            new_id = str(len(data) + 1)
            data[new_id] = {"name": new_name, "age": new_age}
            st.success(f"User {new_name} added successfully! 🎉")
        else:
            st.error("Please provide both name and age! ❌")

# Function to update an existing user
def update_user():
    st.subheader("Update User ✍️")
    user_id = st.text_input("Enter User ID to update: ")
    
    if user_id in data:
        new_name = st.text_input("New name: ", value=data[user_id]["name"])
        new_age = st.number_input("New age: ", value=data[user_id]["age"])
        
        if st.button(f"Update User {user_id} ✅"):
            data[user_id] = {"name": new_name, "age": new_age}
            st.success(f"User {user_id} updated successfully! ✨")
    else:
        st.write("User ID not found ❌")

# Function to delete a user
def delete_user():
    st.subheader("Delete a User 🗑️")
    user_id = st.text_input("Enter User ID to delete: ")
    
    if user_id in data:
        if st.button(f"Delete User {user_id} ❌"):
            del data[user_id]
            st.success(f"User {user_id} deleted successfully! 🗑️")
    else:
        st.write("User ID not found ❌")

# Display operations based on selected option
if operation == "View All Users":
    show_users()
elif operation == "View User":
    user_id = st.text_input("Enter User ID to view: ")
    if user_id:
        show_user(user_id)
elif operation == "Add User":
    add_user()
elif operation == "Update User":
    update_user()
elif operation == "Delete User":
    delete_user()


