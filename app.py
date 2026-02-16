import streamlit as st
import random

st.set_page_config(page_title="Urban Safety Dashboard", layout="wide")

st.title("🛰 Urban Safety & Surveillance Analytics System")
st.subheader("Live CCTV Monitoring")

# Simulated risk score
risk_score = random.randint(0, 100)

col1, col2 = st.columns(2)

with col1:
    st.image("https://images.unsplash.com/photo-1504384308090-c894fdcc538d",
             caption="Live CCTV Feed (Demo)",
             use_column_width=True)

with col2:
    st.metric("Current Risk Score", risk_score)

    if risk_score > 70:
        st.error("🚨 HIGH RISK DETECTED! Police Notified!")
        st.audio("https://www.soundjay.com/buttons/sounds/beep-07.mp3")
    elif risk_score > 40:
        st.warning("⚠ Moderate Risk - Monitoring")
    else:
        st.success("✅ Low Risk - Area Safe")

st.divider()

st.subheader("📊 Alert History")
st.write("All detected incidents will be stored here.")

st.subheader("🚔 Police Notification Panel")
st.write("High-risk alerts are automatically sent to the control room.")
