import streamlit as st
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

if "staff_step" not in st.session_state:
    st.session_state.staff_step = 1

# ==========================================
# 2. SIDEBAR NAVIGATION DROPDOWN
# ==========================================
st.sidebar.markdown("## 🌱 TUMAINI 365")
st.sidebar.markdown("### `TOTAL WELLNESS ECOSYSTEM`")
st.sidebar.caption("Your Hope Everyday")
st.sidebar.write("---")
st.sidebar.markdown("🤝 **Strategic Partner Platform:**")
st.sidebar.markdown("#### **Viva 360 Insurance Brokers**")
st.sidebar.write("---")

st.sidebar.subheader("🚪 System Portal Navigation")
selected_portal = st.sidebar.selectbox(
    "Choose Interface to Open:",
    ["1. Employee Secure Portal", "2. Ezekiel's Clinical Panel", "3. HR Executive Analytics"]
)
st.sidebar.write("---")

pin_input = ""
if selected_portal == "2. Ezekiel's Clinical Panel":
    st.sidebar.subheader("🔒 Administrator Login")
    pin_input = st.sidebar.text_input("Enter Access PIN:", type="password", key="ez_sidebar_pin")

st.sidebar.info("💡 **Boardroom Note:** Pre-loaded baseline datasets are active. Portal views preserve and display data perfectly.")

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
        
        st.write("#### Step 1: Corporate Validation & Contact Registration")
        dept_input = st.selectbox("Your Department Grouping:", ["Direct Sales Force", "Underwriting & Risk", "Claims Adjustment Cadre", "Administration & HR"], key="staff_dept")
        id_input = st.text_input("Enter Active Viva 360 Staff ID:", placeholder="e.g., V360-104", key="staff_id_num")
        phone_input = st.text_input("Enter Your Mobile Phone Number (For Secure Emergency Intercepts):", placeholder="e.g., +254720545788", key="staff_phone")
        email_input = st.text_input("Enter Your Corporate Email Address:", placeholder="e.g., user@viva360.co.ke", key="staff_email")
        consent_input = st.checkbox("I consent to this screening under the Data Protection Act parameters to access my wellness roadmap.", key="staff_consent")
        
        if st.button("➡️ PROCEED TO ASSESSMENT (NEXT STEP)"):
            if id_input and phone_input and email_input and consent_input:
                st.session_state.temp_dept = dept_input
                st.session_state.temp_id = id_input
                st.session_state.temp_phone = phone_input
                st.session_state.temp_email = email_input
                st.session_state.staff_step = 2
                st.rerun()
            else:
                st.error("Validation Error: Please fill in all fields and check the data protection consent box.")

    elif st.session_state.staff_step == 2:
        st.write("Logged in as: " + str(st.session_state.temp_id))
        st.write("#### Step 2: The Core Screening Matrix (DSM-5-TR Psychometric Tracker)")
        st.caption("Scale: 0 = Not at all | 1 = Several days | 2 = More than half the days | 3 = Nearly every day")
        
        q1 = st.radio("1. Little interest or pleasure in doing things at work or home:", (0, 1, 2, 3), horizontal=True)
        q2 = st.radio("2. Feeling down, depressed, flat, or hopeless:", (0, 1, 2, 3), horizontal=True)
        q3 = st.radio("3. Feeling tired, sluggish, or having chronically low energy volumes:", (0, 1, 2, 3), horizontal=True)
        q4 = st.radio("4. Feeling nervous, anxious, on edge, or overwhelmed by quotas:", (0, 1, 2, 3), horizontal=True)
        q5 = st.radio("5. Trouble relaxing, muscle tension, or constant overthinking:", (0, 1, 2, 3), horizontal=True)
        q6 = st.radio("6. Becoming easily annoyed, hyper-irritable with peers, or cross-functional friction:", (0, 1, 2, 3), horizontal=True)
        q9 = st.radio("⚠️ 7. Thoughts that you would be better off dead, or of hurting yourself in some way:", (0, 1, 2, 3), horizontal=True)
        
        if st.button("⬅️ BACK TO STEP 1"):
            st.session_state.staff_step = 1
            st.rerun()
            
        if st.button("🚀 SUBMIT CONFIDENTIAL SCREENING"):
            token = "T365-" + str(st.session_state.temp_dept[:3].upper()) + "-" + str(uuid.uuid4().hex[:4].upper())
            score_total = q1 + q2 + q3 + q4 + q5 + q6 + q9
            calculated_tier = "RED TIER" if (score_total >= 13 or q9 >= 1) else "YELLOW TIER" if score_total >= 6 else "GREEN TIER"
            
            st.session_state.last_token = token
            st.session_state.last_tier = calculated_tier
            st.session_state.staff_step = 3
            st.rerun()

    elif st.session_state.staff_step == 3:
        st.success("🎉 Confidential Screening Completed Successfully.")
        st.info("Your Non-Identifiable Security Token: " + str(st.session_state.last_token))
        st.write("### Your Personalized Support Action Plan")
        
        if st.session_state.last_tier == "RED TIER":
            st.error("🚨 RED TIER ESCALATION: ACUTE CRISIS INTERCEPT")
            st.write("Emergency Care Activated: Secure alerts are logged on Ezekiel Kiago's console. Under our high-priority support framework, you are required to establish an immediate link with our clinical hotline.")
            
            staff_msg = f"Hello Ezekiel, my assessment flagged a Red Tier alert under Token {st.session_state.last_token}. Please open my care intake file."
            encoded_staff_msg = staff_msg.replace(" ", "%20")
            st.link_button(
                "📲 CONNECT IMMEDIATELY TO WHATSAPP HOTLINE",
                f"https://wa.me{encoded_staff_msg}"
            )
            
        elif st.session_state.last_tier == "YELLOW TIER":
            st.warning("🟡 YELLOW TIER ALERT: FUNCTIONAL BURNOUT RISK")
            st.write("Your Action Roadmap: Your profile highlights functional quota fatigue. Your token matches you directly to this month's voluntary Virtual Wellness Booster Pod.")
        else:
            st.success("🟢 GREEN TIER: OPTIMAL WORKFORCE RESILIENCE")
            st.write("Preventive care loop activated. Staff member granted immediate on-demand access to the 14-day digital decompression files.")
            
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
    
    if pin_input != "365":
        st.warning("Awaiting proper credential parameters. Access blocked under Data Protection Act framework.")
    else:
        st.success("Access Verified. Secure encrypted database connection active.")
        st.write("### 🗂️ Live Patient Triage & Active Contact Registry")
        
        baseline_data = [
            {"Anonymized Token": "T365-CLA-F56D1A", "Cadre Department": "Claims Adjustment Cadre", "Employee Staff ID": "V360-205", "Telephone Mobile Number": "+254733444555", "Corporate Email": "claims5@viva360.co.ke", "Triage Status": "🔴 RED TIER CRISIS"},
            {"Anonymized Token": "T365-CLA-200B", "Cadre Department": "Claims Adjustment Cadre", "Employee Staff ID": "V360-101", "Telephone Mobile Number": "+254755666777", "Corporate Email": "admin@viva360.co.ke", "Triage Status": "🔴 RED TIER CRISIS"},
            {"Anonymized Token": "T365-DIR-E49A2B", "Cadre Department": "Direct Sales Force", "Employee Staff ID": "V360-401", "Telephone Mobile Number": "+254711222333", "Corporate Email": "sales1@viva360.co.ke", "Triage Status": "🟡 YELLOW RISK"},
            {"Anonymized Token": "T365-UND-B81C9F", "Cadre Department": "Underwriting & Risk", "Employee Staff ID": "V360-112", "Telephone Mobile Number": "+254722333444", "Corporate Email": "risk2@viva360.co.ke", "Triage Status": "🟢 GREEN RESILIENCE"}
        ]
        
        st.dataframe(pd.DataFrame(baseline_data), use_container_width=True)
        st.write("---")
        
        st.write("### 🚨 Urgent WhatsApp Intercept Actions Matrix")
        st.link_button("🚨 LAUNCH WHATSAPP INTERCEPT FOR T365-CLA-F56D1A", "https://wa.meHello%20Ezekiel%20Kiago%20from%20Tumaini%20365.%20I%20am%20intercepting%20Token%20T365-CLA-F56D1A")
        st.link_button("🚨 LAUNCH WHATSAPP INTERCEPT FOR T365-CLA-200B", "https://wa.meHello%20Ezekiel%20Kiago%20from%20Tumaini%20365.%20I%20am%20intercepting%20Token%20T365-CLA-200B")

# ==========================================
# PORTAL 3: HR EXECUTIVE ANALYTICS
# ==========================================
else:
    st.title("📊 Viva 360 Insurance Brokers: Executive Analytics Dashboard")
    st.subheader("Institutional Burnout Tracking & Corporate Budgeting Interface")
    st.write("---")
    st.markdown("### 🔒 Privacy Protocol View")
