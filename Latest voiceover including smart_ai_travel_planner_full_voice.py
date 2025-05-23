
import streamlit as st
from datetime import datetime, timedelta

st.title("Smart AI Travel Planner – Voice + Full Feature Version")

# Trip type toggle
trip_type = st.radio("Trip Type", options=["One-Way", "Round-Trip"])

# Simulated voice input (placeholder for future integration)
st.text("🎤 Say your cities or type them below...")

col1, col2 = st.columns(2)
with col1:
    from_city = st.text_input("From (city)", "Madrid")
    if from_city:
        st.caption("Suggestions:")
        if from_city.lower().startswith("mad"):
            st.write(["Madrid (MAD)", "Madeira (FNC)", "Madurai (IXM)"])
with col2:
    to_city = st.text_input("To (city)", "Tokyo")
    if to_city:
        st.caption("Suggestions:")
        if to_city.lower().startswith("tok"):
            st.write(["Tokyo (NRT)", "Tokushima (TKS)", "Toledo (TOL)"])

# Date pickers
departure_date = st.date_input("Departure Date", datetime.today())
return_date = None
if trip_type == "Round-Trip":
    return_date = st.date_input("Return Date", datetime.today() + timedelta(days=7))

# Voice feedback (placeholder)
st.text("🗣️ I found flights for your route...")

# Search button
if st.button("Search"):
    st.success(f"Searching flights from {from_city} to {to_city}")
    st.info(f"Departure: {departure_date.strftime('%Y-%m-%d')}")
    if return_date:
        st.info(f"Return: {return_date.strftime('%Y-%m-%d')}")
