import streamlit as st
from datetime import datetime, timedelta

# Page setup
st.set_page_config(page_title="Smart AI Travel Planner", layout="wide")

# Inject custom styles for modern UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background-color: #0b0c10;
        color: #f8f9fa;
    }

    .main-title {
        text-align: center;
        font-size: 48px;
        font-weight: 600;
        background: -webkit-linear-gradient(45deg, #00ffe1, #7a00ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 30px;
        margin-bottom: 10px;
    }

    .welcome-box {
        background-color: #161b22;
        border-radius: 12px;
        padding: 20px;
        margin: 20px auto;
        max-width: 700px;
        box-shadow: 0 0 10px rgba(122, 0, 255, 0.25);
    }

    .stTextInput > div > input {
        background-color: #1e1e2e;
        color: #ffffff;
        border-radius: 8px;
        padding: 10px;
    }

    .stDateInput input {
        background-color: #1e1e2e !important;
        color: #ffffff !important;
    }

    .stButton>button {
        background-color: #7a00ff;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        height: 45px;
    }
    </style>
""", unsafe_allow_html=True)

# Glowing Title
st.markdown('<div class="main-title">Smart AI Travel Planner</div>', unsafe_allow_html=True)

# Welcome Box
st.markdown("""
<div class="welcome-box">
    <p><strong>Welcome!</strong> You can speak or type to plan your trip. I’ll guide you step-by-step. Enter any city, travel date, or just talk to me.</p>
</div>
""", unsafe_allow_html=True)

# Form Section
col1, col2 = st.columns(2)
with col1:
    from_city = st.text_input("From", "")
with col2:
    to_city = st.text_input("To", "")

col3, col4 = st.columns(2)
with col3:
    departure_date = st.date_input("Departure Date", datetime.today())
with col4:
    trip_type = st.radio("Trip Type", ["One-Way", "Round-Trip"])
    return_date = None
    if trip_type == "Round-Trip":
        return_date = st.date_input("Return Date", datetime.today() + timedelta(days=5))

if st.button("Find Flights"):
    st.success(f"Searching for trips from {from_city} to {to_city}")
    st.info(f"Departure: {departure_date.strftime('%Y-%m-%d')}")
    if return_date:
        st.info(f"Return: {return_date.strftime('%Y-%m-%d')}")