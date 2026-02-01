import streamlit as st
import uuid

# 1. Setup Database Connection
# This uses Streamlit's official MySQL connector
conn = st.connection('mysql', type='sql')

st.set_page_config(page_title="Register | Women in ICT", page_icon="📝")

st.markdown("""
    <style>
    .stButton>button { background-color: #C8102E; color: white; border-radius: 8px; font-weight: bold; }
    .header-text { color: #6A1B9A; font-weight: 800; font-size: 2rem; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="header-text">Join the Community</p>', unsafe_allow_html=True)

with st.form("registration_form"):
    full_name = st.text_input("Full Name *")
    email = st.text_input("Email Address *")
    phone = st.text_input("Phone Number *")
    institution = st.text_input("Institution *")
    role = st.selectbox("Role *", ["Student", "Faculty", "Industry", "Other"])
    poster = st.radio("Poster Presenter?", ["Yes", "No"], index=1)
    consent = st.checkbox("I consent to data collection *")
    submitted = st.form_submit_button("Submit Registration")

if submitted:
    if not full_name or not email or not consent:
        st.error("Please fill required fields.")
    else:
        reg_id = str(uuid.uuid4())[:8].upper()
        
        # SAVE TO MYSQL
        try:
            with conn.session as s:
                s.execute(
                    "INSERT INTO registrations (id, name, email, phone, institution, role, poster) VALUES (:id, :n, :e, :p, :i, :r, :pt)",
                    params={"id": reg_id, "n": full_name, "e": email, "p": phone, "i": institution, "r": role, "pt": poster}
                )
                s.commit()
            
            st.success(f"Successfully Registered! ID: {reg_id}")
            st.balloons()
            # Note: We will add the "Confirmation Email" logic in the next turn!
        except Exception as e:
            st.error("Database error. Please contact admin.")
            st.write(e)
