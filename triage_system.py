import streamlit as st
import datetime
import uuid

# Set up clean corporate branding on the page
st.set_page_config(page_title="Tumaini 365 Dashboard", page_icon="🌱", layout="centered")

st.title("🌱 Tumaini Three Sixty Five Limited")
st.subheader("Viva 365 Insurance Brokers: Preventive Wellness Engine")
st.write("---")

# 1. INPUT INTERFACE (What the board clicks to test the system)
st.sidebar.header("🎯 Boardroom Simulation Controls")
st.sidebar.write("Adjust scores below to test the automated triage logic live:")

department = st.sidebar.selectbox(
    "Select Target Department:",
    ["Direct Sales Force", "Underwriting & Risk", "Claims Adjustment Cadre", "Administration & HR"]
)

st.sidebar.write("---")
st.sidebar.subheader("Clinical Metrics (DSM-5-TR Scale)")
phq9_score = st.sidebar.slider("PHQ-9 Depression/Burnout Score (0 - 27):", 0, 27, 4)
gad7_score = st.sidebar.slider("GAD-7 Anxiety/Stress Score (0 - 21):", 0, 21, 3)

self_harm_triggered = st.sidebar.checkbox("Trigger PHQ-9 Q9 Flag (Self-Harm/Acute Risk Indicators)")

# 2. CORE BACKEND ENGINES
def generate_anonymized_token(dept):
    unique_id = uuid.uuid4().hex[:6].upper()
    return f"T365-{dept[:3].upper()}-{unique_id}"

# Calculate clinical tiers based on the data sliders
if self_harm_triggered or phq9_score >= 15 or gad7_score >= 15:
    tier, color, alert_box, action = "RED TIER", "error", "🚨 RED TIER ESCALATION: ACUTE CRISIS INTERCEPT", "Immediate notification flagged to Ezekiel Kiago's console. Bypassing standard delays. Automated priority WhatsApp safety link dispatched to user."
elif 5 <= phq9_score <= 14 or 5 <= gad7_score <= 14:
    tier, color, alert_box, action = "YELLOW TIER", "warning", "🟡 YELLOW TIER ALERT: FUNCTIONAL BURNOUT RISK", "Proactive interception activated. Automated email invitation dispatched matching user anonymized token to this month's voluntary Virtual Wellness Booster Pod."
else:
    tier, color, alert_box, action = "GREEN TIER", "success", "🟢 GREEN TIER: OPTIMAL SYSTEMS RESILIENCE", "Preventive tracking activated. User granted on-demand access to the 14-day digital decompression micro-learning kits."

# 3. INTERACTIVE VISUAL DISPLAY
token = generate_anonymized_token(department)

st.write("### 🔍 Live Processing Stream (Data Protection Anonymization)")
st.info(f"**Generated Client Token:** `{token}`  \n**Target Department Grouping:** {department}")

st.write("### ⚡ Real-Time Automated Infrastructure Response")
if color == "success":
    st.success(alert_box)
elif color == "warning":
    st.warning(alert_box)
else:
    st.error(alert_box)

st.write(f"**System Dispatch Logic Execution:**  \n*{action}*")
st.write("---")

# 4. HR EXECUTIVE COMMITTEE SUMMARY GRAPHICS
st.write("### 📊 Macro-Level Workplace Visibility (Shared with HR)")
st.write("Data aggregates automatically to guide departmental budgeting without breaching employee privacy:")

# Mock macro percentages for visual display
col1, col2, col3 = st.columns(3)
col1.metric("Green Tier (Resilient)", "65%", "+2% this month")
col2.metric("Yellow Tier (Burnout)", "25%", "-1% this month")
col3.metric("Red Tier (Crisis)", "10%", "Stable")

st.write("---")
st.caption("🔒 Fully Compliant with the Data Protection Act of Kenya. Individual medical records remain decoupled from corporate employee profiles.")
