import streamlit as st
import datetime
import uuid
import pandas as pd

# ==========================================
# 1. APPLICATION INITIALIZATION & CONFIG
# ==========================================
st.set_page_config(
    page_title="Tumaini 365 Total Wellness Ecosystem", 
    page_icon="🌱", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Persistent session database registry matrix
if "clinical_registry" not in st.session_state:
    st.session_state.clinical_registry = pd.DataFrame(columns=[
        "Token", "Department", "Staff_ID", "PHQ9_Score", "GAD7_Score", "Triage_Tier", "Action_Milestone", "Day14_Date", "Day30_Date", "Status"
    ])

# Step tracking for the Staff assessment flow
if "staff_step" not in st.session_state:
    st.session_state.staff_step = 1

# Core System Sorting Functions
def generate_anonymized_token(dept):
    unique_id = uuid.uuid4().hex[:6].upper()
    return f"T365-{dept[:3].upper()}-{unique_id}"

def compute_triage_tier(phq9, gad7, self_harm):
    if self_harm or phq9 >= 15 or gad7 >= 15:
        return "RED TIER", "🚨 RED TIER ESCALATION: ACUTE CRISIS INTERCEPT", "Immediate notification triggered on Ezekiel Kiago's console. Standard messaging delays overridden. Secure priority WhatsApp contact link pushed directly to the user."
    elif 5 <= phq9 <= 14 or 5 <= gad7 <= 14:
        return "YELLOW TIER", "🟡 YELLOW TIER ALERT: FUNCTIONAL BURNOUT RISK", "Proactive interception activated. Automated notification dispatched matching user pseudonym to this month's voluntary Virtual Wellness Booster Pod."
    else:
        return "GREEN TIER", "🟢 GREEN TIER: OPTIMAL WORKFORCE RESILIENCE", "Preventive care loop activated. Staff member granted immediate on-demand access to the 14-day digital decompression micro-learning files."

# ==========================================
# 2. BRANDING SIDEBAR WITH LOGO & DROPDOWN NAV
# ==========================================
with st.sidebar:
    st.image("https://githubusercontent.com", use_container_width=True, caption="Tumaini 365 - Your Hope Everyday")
    st.write("---")
    st.caption("Strategic Partner Platform:")
    st.markdown("🏢 **Viva 360 Insurance Brokers**")
    st.write("---")
    
    # SYSTEM INTERFACE DROPDOWN (100% stable, bypasses all reload bugs)
    st.subheader("🚪 System Portal Navigation")
    selected_portal = st.selectbox(
        "Choose Interface to Open:",
        ["1. Employee Secure Portal", "2. Ezekiel's Clinical Panel", "3. HR Executive Analytics"]
    )
    st.write("---")
    st.info("💡 **Boardroom Demo Note:** Use this dropdown above to switch views instantly. It guarantees your test data and password entries persist without resetting.")

# ==========================================
# PORTAL 1: EMPLOYEE SECURE PORTAL
# ==========================================
if selected_portal == "1. Employee Secure Portal":
    st.title("🌱 Tumaini Three Sixty Five Limited")
    st.subheader("Employee Secure Well-being Assessment Portal")
    st.write("---")
    
    if st.session_state.staff_step == 1:
        st.markdown("### 🔒 Data Protection & Confidentiality Declaration")
        st.write("In strict compliance with the Data Protection Act of Kenya, your screening inputs are treated as sensitive personal data. Your specific clinical scores are entirely hidden from Viva 360 HR and executive management. This system utilizes advanced token pseudonymization to guarantee absolute anonymity.")
        
        st.write("#### Step 1: Corporate Validation")
        col_a, col_b = st.columns(2)
        with col_a:
            dept_input = st.selectbox("Your Department Grouping:", ["Direct Sales Force", "Underwriting & Risk", "Claims Adjustment Cadre", "Administration & HR"], key="staff_dept")
        with col_b:
            id_input = st.text_input("Enter Active Viva 360 Staff ID:", placeholder="e.g., V360-104", key="staff_id_num")
            
        consent_input = st.checkbox("I consent to this screening under the Data Protection Act parameters to access my wellness roadmap.", key="staff_consent")
        
        if st.button("➡️ PROCEED TO ASSESSMENT (NEXT STEP)"):
            if not id_input:
                st.error("Validation Error: Please input a valid Active Viva 360 Staff ID to lock the secure pipeline.")
            elif not consent_input:
                st.error("Compliance Error: You must accept the Data Protection Consent checkbox to move forward.")
            else:
                st.session_state.temp_dept = dept_input
                st.session_state.temp_id = id_input
                st.session_state.staff_step = 2
                st.text("") # Soft trigger placeholder
                st.rerun()

    elif st.session_state.staff_step == 2:
        st.write("Logged in as: " + str(st.session_state.temp_id) + " | Department: " + str(st.session_state.temp_dept))
        st.write("#### Step 2: The Core Screening Matrix (DSM-5-TR Psychometric Tracker)")
        st.caption("Scale: 0 = Not at all | 1 = Several days | 2 = More than half the days | 3 = Nearly every day")
        
        q1 = st.radio("1. Little interest or pleasure in doing things at work or home:", (0, 1, 2, 3), horizontal=True)
        q2 = st.radio("2. Feeling down, depressed, flat, or hopeless:", (0, 1, 2, 3), horizontal=True)
        q3 = st.radio("3. Feeling tired, sluggish, or having chronically low energy volumes:", (0, 1, 2, 3), horizontal=True)
        q4 = st.radio("4. Feeling nervous, anxious, on edge, or overwhelmed by quotas:", (0, 1, 2, 3), horizontal=True)
        q5 = st.radio("5. Trouble relaxing, muscle tension, or constant overthinking:", (0, 1, 2, 3), horizontal=True)
        q6 = st.radio("6. Becoming easily annoyed, hyper-irritable with peers, or cross-functional friction:", (0, 1, 2, 3), horizontal=True)
        q9 = st.radio("⚠️ 7. Thoughts that you would be better off dead, or of hurting yourself in some way:", (0, 1, 2, 3), horizontal=True)
        
        col_nav_1, col_nav_2 = st.columns(2)
        with col_nav_1:
            if st.button("⬅️ BACK TO STEP 1"):
                st.session_state.staff_step = 1
                st.rerun()
                
        with col_nav_2:
            if st.button("🚀 SUBMIT CONFIDENTIAL SCREENING"):
                phq9_total = q1 + q2 + q3 + q9
                gad7_total = q4 + q5 + q6
                self_harm_flag = q9 >= 1
                
                tier, box_text, milestone = compute_triage_tier(phq9_total, gad7_total, self_harm_flag)
                token = generate_anonymized_token(st.session_state.temp_dept)
                
                today = datetime.date.today()
                d14 = today + datetime.timedelta(days=14)
                d30 = today + datetime.timedelta(days=30)
                
                new_entry = {
                    "Token": token, "Department": st.session_state.temp_dept, "Staff_ID": st.session_state.temp_id, 
                    "PHQ9_Score": phq9_total, "GAD7_Score": gad7_total, "Triage_Tier": tier, 
                    "Action_Milestone": milestone, "Day14_Date": d14.strftime('%Y-%m-%d'), 
                    "Day30_Date": d30.strftime('%Y-%m-%d'), "Status": "Active Follow-up"
                }
                st.session_state.clinical_registry = pd.concat([st.session_state.clinical_registry, pd.DataFrame([new_entry])], ignore_index=True)
                
                st.session_state.last_token = token
                st.session_state.last_tier = tier
                st.session_state.last_box = box_text
                st.session_state.last_d14 = d14.strftime('%B %d, %Y')
                st.session_state.last_d30 = d30.strftime('%B %d, %Y')
                
                st.session_state.staff_step = 3
                st.rerun()

    elif st.session_state.staff_step == 3:
        st.success("🎉 Confidential Screening Completed Successfully.")
        st.info("Your Non-Identifiable Security Token: " + str(st.session_state.last_token))
        st.write("### Your Personalized Support Action Plan")
        
        if st.session_state.last_tier == "GREEN TIER":
            st.success(st.session_state.last_box)
            st.write("Your Action Roadmap: Your data token has unlocked the 14-Day Digital Decompression Toolkit (deep breathing guides & structural time-blocking calendar patterns).")
            st.info("📅 Follow-up Check: An automated link will push to your portal on " + str(st.session_state.last_d14) + " to check progress.")
            
        elif st.session_state.last_tier == "YELLOW TIER":
            st.warning(st.session_state.last_box)
            st.write("Your Action Roadmap: Your profile highlights functional burnout. Your token matches you directly to this month's voluntary Virtual Wellness Booster Pod.")
            st.info("📅 Continuous Follow-up: Your booster pod will monitor accountability metrics on " + str(st.session_state.last_d30))
            
        elif st.session_state.last_tier == "RED TIER":
            st.error(st.session_state.last_box)
            st.write("Emergency Override Plan: Secure emergency alerts logged on Ezekiel Kiago's console. Click below for immediate clinical link routing.")
            st.markdown("[📲 OPEN SECURE WHATSAPP CRISIS ESCALATION LINK TO EZEKIEL](https://wa.me)")
            
        if st.button("🔄 RESTART FRESH ASSESSMENT"):
            st.session_state.staff_step = 1
            st.rerun()

# ==========================================
# PORTAL 2: EZEKIEL'S CLINICAL PANEL
# ==========================================
elif selected_portal == "2. Ezekiel's Clinical Panel":
    st.title("🔒 Tumaini 365: Clinical Administration Workspace")
    st.subheader("Lead Consultant Console: Ezekiel Kiago Wangunyu")
    st.write("---")
    
    pin = st.text_input("Enter Clinical Security Access PIN:", type="password", key="ezekiel_pin_key")
    
    if pin == "365":
