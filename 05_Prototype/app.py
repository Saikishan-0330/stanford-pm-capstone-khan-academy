import streamlit as st
import pandas as pd
import random

# ==========================================
# 🎓 Smart Revisit Algorithm Prototype
# ==========================================

st.set_page_config(page_title="Khan Academy: Smart Revisit Prototype", page_icon="🎓")

st.title("🎓 Smart Revisit Logic Simulator")
st.markdown("""
**Context:** This prototype demonstrates the **logic engine** behind the Smart Revisit feature.
As a Product Manager, I designed this to validate the personalization rules before handing off to Engineering.
""")

# --- 1. SIDEBAR: Simulate User Data ---
st.sidebar.header("🎛️ User Simulator")
st.sidebar.write("Tweak these values to simulate different students:")

student_name = st.sidebar.text_input("Student Name", "Ravi")
last_session_days = st.sidebar.slider("Days Since Last Visit", 0, 30, 2)
accuracy_rate = st.sidebar.slider("Last Session Accuracy (%)", 0, 100, 45)
attempts_on_problem = st.sidebar.slider("Attempts on Stuck Problem", 1, 10, 4)

# --- 2. THE ALGORITHM (From PRD) ---
def get_smart_recommendation(accuracy, attempts, days_away):
    """
    Determines the best entry point for a returning learner.
    Logic defined in PRD Section 3.1.
    """
    # Logic Branch A: Struggling User
    if accuracy < 50 and attempts > 2:
        return {
            "type": "Review Key Concepts",
            "color": "orange",
            "icon": "⏮️",
            "message": "It looks like you hit a snag last time. Let's refresh the basics to build momentum!"
        }
    
    # Logic Branch B: High Performer
    elif accuracy > 80:
        return {
            "type": "Next Logical Step",
            "color": "green",
            "icon": "🚀",
            "message": "You crushed it last time! You're ready to advance to the next unit."
        }
    
    # Logic Branch C: Long Absence (Context Loss)
    elif days_away > 7:
        return {
            "type": "Quick Recap",
            "color": "blue",
            "icon": "🧠",
            "message": "Welcome back! It's been a week. Here is a 2-minute summary to get you back in flow."
        }
    
    # Default: Resume
    else:
        return {
            "type": "Resume",
            "color": "gray",
            "icon": "▶️",
            "message": "Picking up exactly where you left off."
        }

recommendation = get_smart_recommendation(accuracy_rate, attempts_on_problem, last_session_days)

# --- 3. THE UI OUTPUT ---
st.divider()

st.subheader(f"👋 Welcome back, {student_name}!")
st.write(f"*Last seen: {last_session_days} days ago | Accuracy: {accuracy_rate}%*")

# Display the "Smart Chip"
st.info(f"**Algorithm Decision:** {recommendation['type']}")

# Visual Card
card_html = f"""
<div style="
    padding: 20px;
    border-radius: 10px;
    background-color: #f0f2f6;
    border-left: 5px solid {recommendation['color']};
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
">
    <h3 style="margin:0;">{recommendation['icon']} {recommendation['type']}</h3>
    <p style="margin-top:10px; font-size:18px;">{recommendation['message']}</p>
    <button style="
        background-color: {recommendation['color']};
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        margin-top: 15px;
        cursor: pointer;
    ">Start Learning</button>
</div>
"""

st.markdown(card_html, unsafe_allow_html=True)

# --- 4. DEBUG VIEW (For Engineers) ---
st.divider()
with st.expander("🤓 View Logic / Debug Info"):
    st.json({
        "input_accuracy": accuracy_rate,
        "input_attempts": attempts_on_problem,
        "days_absent": last_session_days,
        "output_decision": recommendation['type']
    })
