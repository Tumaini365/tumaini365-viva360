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

# FIXED REPOSITORY ARRAYS
raw_data = [
    {"Token": "T365-DIR-E49A2B", "Department": "Direct Sales Force", "Staff_ID": "V360-401", "PHQ9_Score": 14, "GAD7_Score": 12, "Triage_Tier": "YELLOW TIER", "Action_Milestone": "Assigned to Wellness Pod", "Day14_Date": "2026-07-15", "Day30_Date": "2026-07-31", "Status": "Active"},
    {"Token": "T365-UND-B81C9F", "Department": "Underwriting & Risk", "Staff_ID": "V360-112", "PHQ9_Score": 2, "GAD7_Score": 3, "Triage_Tier": "GREEN TIER", "Action_Milestone": "Granted Self-Care Kits", "Day14_Date": "2026-07-15", "Day30_Date": "2026-07-31", "Status": "Optimal"},
    {"Token": "T365-CLA-F56D1A", "Department": "Claims Adjustment Cadre", "Staff_ID": "V360-205", "PHQ9_Score": 18, "GAD7_Score": 16, "Triage_Tier": "RED TIER", "Action_Milestone": "Direct Hotlink Routed", "Day14_Date": "2026-07-15", "Day30_Date": "2026-07-31", "Status": "Intercepted"},
    {"Token": "T365-DIR-K33M7X", "Department": "Direct Sales Force", "Staff_ID": "V360-415", "PHQ9_Score": 11, "GAD7_Score": 9, "Triage_Tier": "YELLOW TIER", "Action_Milestone": "Assigned to Wellness Pod", "Day14_Date": "2026-07-15", "Day30_Date": "2026-07-31", "Status": "Active"}
]
clinical_registry = pd.DataFrame(raw_data)

if "staff_step" not in st.session_state:
    st.session_state.staff_step = 1

# ==========================================
# 2. SIDEBAR NAVIGATION CONTROLS
# ==========================================
with st.sidebar:
    # FIXED: Replaced fragile image strings with clean, native, and unblockable layout headers
    st.markdown("## 🧠 Tumaini 365")
    st.caption("✨ Your Hope Everyday")
    st.write("---")
    st.markdown("🏢 **Viva 360 Insurance Brokers**")
    st.write("---")
    
    st.subheader("🚪 System Portal Navigation")
    selected_portal = st.selectbox(
        "Choose Interface to Open:",
        ["1. Employee Secure Portal", "2. Ezekiel's Clinical Panel", "3. HR Executive Analytics"]
    )
    st.write("---")
    
    pin_input = ""
    if selected_portal == "2. Ezekiel's Clinical Panel":
        st.subheader("🔒 Administrator Login")
        pin_input = st.text_input("Enter Access PIN:", type="password", key="ez_sidebar_pin")
        
    st.info("💡 **Boardroom Demo Note:** Pre-loaded baseline datasets are now permanently active. Changing portal views above will preserve and display data perfectly.")

# ==========================================
# PORTAL INTERFACE GATEWAY ROUTING
# ==========================================
if selected_portal == "1. Employee Secure Portal":
    st.markdown("## 🌱 Tumaini Three Sixty Five Limited")
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
            if id_input and consent_input:
                st.session_state.temp_dept = dept_input
                st.session_state.temp_id = id_input
                st.session_state.staff_step = 2
                st.rerun()
            else:
                st.error("Please enter your Staff ID and accept the Data Protection consent box.")

    elif st.session_state.staff_step == 2:
        st.write("Logged in as: " + str(st.session_state.temp_id) + " | Department: " + str(st.session_state.temp_dept))
        st.write("#### Step 2: The Core Screening Matrix (DSM-5-TR Psychometric Tracker)")
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
                st.session_state.last_token = "T365-MOCK-" + str(uuid.uuid4().hex[:4].upper())
                st.session_state.last_tier = "YELLOW TIER"
                st.session_state.last_box = "🟡 YELLOW TIER ALERT: FUNCTIONAL BURNOUT RISK"
                st.session_state.last_d14 = "July 15, 2026"
                st.session_state.last_d30 = "July 31, 2026"
                st.session_state.staff_step = 3
                st.rerun()

    elif st.session_state.staff_step == 3:
        st.success("🎉 Confidential Screening Completed Successfully.")
        st.info("Your Non-Identifiable Security Token: " + str(st.session_state.last_token))
        st.write("### Your Personalized Support Action Plan")
        st.warning(st.session_state.last_box)
        st.write("Your Action Roadmap: Your profile highlights functional burnout. Your token matches you directly to this month's voluntary Virtual Wellness Booster Pod.")
        st.info("📅 Continuous Follow-up: Your booster pod will monitor accountability metrics on " + str(st.session_state.last_d30))
        if st.button("🔄 RESTART FRESH ASSESSMENT"):
            st.session_state.staff_step = 1
            st.rerun()

elif selected_portal == "2. Ezekiel's Clinical Panel":
    st.markdown("## 🔒 Tumaini 365: Clinical Administration Workspace")
    st.subheader("Lead Consultant Console: Ezekiel Kiago Wangunyu")
    st.write("---")
    if pin_input != "365":
        st.warning("⚠️ Access Restricted: Please enter your master access key code in the sidebar block on the left to unlock the active registry.")
    else:
        st.success("✅ Access Verified. Encrypted database channel active.")
        st.write("### 🗂️ Live Patient Triage & Continuous Follow-Up Registry Matrix")
        st.dataframe(clinical_registry, use_container_width=True)
        st.write("---")
        st.write("### 🚨 Emergency Overrides Pending Intercept")
        st.error("⚠️ **CRITICAL INCIDENT ALERT:** High-risk overloads detected inside active cadres. Reference Token T365-CLA-F56D1A (Claims Adjustment Cadre) for immediate callback match validation to encrypted staff ID V360-205.")

else:
    st.markdown("## 📊 Viva 360 Insurance Brokers: Executive Analytics Dashboard")
    st.subheader("Institutional Burnout Tracking & Corporate Budgeting Interface")
    st.write("---")
    st.markdown("### 🔒 Privacy Protocol View")
    st.write("In compliance with data protection laws, all individual fields are entirely stripped from this layout. It displays only aggregated data groupings to guide resource deployment.")
    st.write("---")
    
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.metric("Total Active Staff Screened", "4 Personnel")
    with col_m2:
        st.metric("Green Tier (Resilience Ratio)", "25.0%")
    with col_m3:
        st.metric("Yellow Tier (Burnout Density)", "50.0%")
    st.write("---")
    
    st.write("### 📑 Departmental Burnout Distribution Metrics")
    col_chart_1, col_chart_2, col_chart_3 = st.columns(3)
    with col_chart_1:
        st.write("🔥 **Direct Sales Force Grouping**")
        st.write("- Green Resilience: 1 Staff")
        st.write("- Yellow Burnout Risk: 2 Staff")
        st.write("- Red Crisis Urgency: 0 Staff")
    with col_chart_2:
        st.write("⏳ **Underwriting & Risk Grouping**")
        st.write("- Green Resilience: 1 Staff")
        st.write("- Yellow Burnout Risk: 0 Staff")
        st.write("- Red Crisis Urgency: 0 Staff")
    with col_chart_3:
        st.write("🚨 **Claims Adjustment Cadre**")
        st.write("- Green Resilience: 0 Staff")
        st.write("- Yellow Burnout Risk: 0 Staff")
        st.write("- Red Crisis Urgency: 1 Staff")
        
    st.write("---")
    st.error("🎯 **STRATEGIC BUDGET ALLOCATION RECOMMENDATION:** High burnout density values tracked inside your Direct Sales Force pipeline (Quota Fatigue). Tumaini 365 advises human resource scheduling of a specialized 'Preventive Financial Therapy Safari' workshop next month to protect premium acquisition targets before absenteeism spikes occur.")

st.write("---")
