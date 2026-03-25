import streamlit as st

# 1. Professional Page Setup
st.set_page_config(page_title="Student Success Portal", layout="wide")

# 2. Check Login Status
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# --- LOGIN SCREEN ---
def show_login():
    st.title("🔐 Student Portal Login")
    with st.form("login_form"):
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        
        if submit:
            if user == "Ramya" and pwd == "admin123":
                st.session_state['authenticated'] = True
                st.rerun()
            else:
                st.error("Invalid Username or Password")

# --- DASHBOARD ---
def show_dashboard():
    st.sidebar.title(f"Welcome, Ramya!")
    if st.sidebar.button("Log Out"):
        st.session_state['authenticated'] = False
        st.rerun()

    st.title("📊 Student Performance Dashboard")
    
    # Layout with Columns
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Input Student Data")
        study = st.slider("Study Hours", 0, 15, 7)
        attendance = st.slider("Attendance %", 0, 100, 85)
        # You can add your other sliders here
        
    with col2:
        st.subheader("AI Prediction")
        # Logic for prediction
        marks = (study * 5) + (attendance * 0.2)
        
        st.metric(label="Predicted Marks", value=f"{marks:.2f}/100")
        
        if marks > 75:
            st.success("High Performance Predicted")
        else:
            st.warning("Improvement Needed")

# --- MAIN APP LOGIC ---
if st.session_state['authenticated']:
    show_dashboard()
else:
    show_login()
