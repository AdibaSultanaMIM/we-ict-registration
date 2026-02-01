import streamlit as st
import uuid
from datetime import datetime

# 1. Page Configuration (University Standard)
st.set_page_config(page_title="Register | Women in ICT", page_icon="📝", layout="centered")

# 2. Custom Styling (White, Red, Purple)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button { 
        background-color: #C8102E; 
        color: white; 
        border-radius: 8px; 
        width: 100%;
        font-weight: bold;
    }
    .header-text { color: #6A1B9A; font-weight: 800; font-size: 2.5rem; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="header-text">Join the Community</p>', unsafe_allow_html=True)
st.write("Register to join our network of women in technology. You will receive a confirmation email upon successful registration.")

# 3. The Registration Form
with st.form("registration_form"):
    full_name = st.text_input("Full Name *")
    email = st.text_input("Email Address * (Any Gmail or institutional email)")
    phone = st.text_input("Phone Number *")
    institution = st.text_input("Institution / Organization *")
    
    role = st.selectbox("Your Role *", options=["Student", "Faculty", "Industry Professional", "Other"])
    poster = st.radio("Are you interested in presenting a Poster?", options=["Yes", "No"], index=1)
    
    notes = st.text_area("Any specific interests or questions? (Optional)")
    
    consent = st.checkbox("I consent to the collection of my data for event purposes. *")
    
    submitted = st.form_submit_button("Submit Registration")

# 4. Logic after Submission (This is where MySQL & Email will go)
if submitted:
    if not full_name or not email or not phone or not consent:
        st.error("Please fill in all required fields (*) and provide consent.")
    else:
        # Generate a unique ID for this person
        reg_id = str(uuid.uuid4())[:8].upper()
        
        # DISPLAY SUCCESS (We will add the DB/Email code in the next step)
        st.success(f"Success! Thank you, {full_name}.")
        st.info(f"Your Registration ID is: {reg_id}. A confirmation email will be sent shortly.")
