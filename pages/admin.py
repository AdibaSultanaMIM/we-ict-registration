import streamlit as st
import pandas as pd

st.set_page_config(page_title="Admin Dashboard | WE-ICT", layout="wide")

# Simple Password Protection (We will store the real password in Secrets later)
st.sidebar.title("Admin Login")
password = st.sidebar.text_input("Enter Admin Password", type="password")

if password == st.secrets.get("admin_password", "buet123"):
    st.title("Registration Dashboard")
    st.write("Below are the names and contacts of all registered participants.")
    
    # FOR NOW: We use a placeholder table until we connect the database
    # In the next step, we will connect MySQL to show REAL data here
    data = {
        "Name": ["Sarah Ahmed", "Lisa Wong"],
        "Email": ["sarah@example.com", "lisa@example.com"],
        "Role": ["Software Engineer", "Cybersecurity Analyst"],
        "Status": ["Registered", "Registered"]
    }
    df = pd.DataFrame(data)
    st.table(df)
    
    # Option to Delete (Requirement)
    st.divider()
    delete_id = st.text_input("Enter ID to Delete Participant")
    if st.button("Delete Entry"):
        st.warning(f"Ready to delete {delete_id} from MySQL database.")

else:
    st.info("Please enter the correct password in the sidebar to view data.")
