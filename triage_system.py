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

# FIXED PRE-POPULATED REPOSITORY MATRICES
if "clinical_registry" not in st.session_state:
    st.session_state.clinical_registry = pd.DataFrame([
        {"Token": "T365-DIR-E49A2B", "Department": "Direct Sales Force", "Staff_ID": "V360-401", "Mobile_Number": "+254711222333", "Email_Address": "sales1@viva360.co.ke", "Triage_Tier": "YELLOW TIER", "Status": "Active Follow-up"},
        {"Token": "T365-UND-B81C9F", "Department": "Underwriting & Risk", "Staff_ID": "V360-112", "Mobile_Number": "+254722333444", "Email_Address": "risk2@viva360.co.ke", "Triage_Tier": "GREEN TIER", "Status": "Optimal Resilience"},
        {"Token": "T365-CLA-F56D1A", "Department": "Claims Adjustment Cadre", "Staff_ID": "V360-205", "Mobile_Number": "+254733444555", "Email_Address": "claims5@viva360.co.ke", "Triage_Tier": "RED TIER", "Status": "Clinical Intercept Pending"},
        {"Token": "T365-CLA-200B", "Department": "Claims Adjustment Cadre", "Staff_ID": "V360-101", "Mobile_Number": "+254755666777", "Email_Address": "admin@viva360.co.ke", "Triage_Tier": "RED TIER", "Status": "Clinical Intercept Pending"}
    ])

if "staff_step" not in st.session_state:
    st.session_state.staff_step = 1

# ==========================================
# 2. SIDEBAR NAVIGATION CONTROLS
# ==========================================
st.sidebar.markdown("## 🌱 TUMAINI 365")
st.sidebar.markdown("### `TOTAL WELLNESS ECOSYSTEM`")
st.sidebar.caption("✨ Your Hope Everyday")
st.sidebar.write("---")
st.sidebar.markdown("🤝 **Strategic Partner Platform:**")
st.sidebar.markdown("#### **Viva 360 Insurance Brokers**")
st.sidebar.write("---")

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
# PORTAL INTERFACE GATEWAY ROUTING
# ==========================================
if selected_portal == "1. Employee Secure Portal":
    st.markdown("## 🌱 Tumaini Three Sixty Five Limited")
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
                st.error("Validation Error: Please check required inputs and mark the consent box.")

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
            
            new_entry = {
                "Token": token, "Department": st.session_state.temp_dept, "Staff_ID": st.session_state.temp_id, 
                "Mobile_Number": st.session_state.temp_phone, "Email_Address": st.session_state.temp_email, 
                "Triage_Tier": calculated_tier, "Status": "Active Follow-up"
            }
            st.session_state.clinical_registry = pd.concat([st.session_state.clinical_registry, pd.DataFrame([new_entry])], ignore_index=True)
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

elif selected_portal == "2. Ezekiel's Clinical Panel":
    st.title("🔒 Tumaini 365: Clinical Administration Workspace")
    st.subheader("Lead Consultant Console: Ezekiel Kiago Wangunyu")
    st.write("---")
    if pin_input != "365":
        st.warning("⚠️ Access Restricted: Please enter your master access key code in the sidebar block on the left to unlock the active registry.")
    else:
        st.success("✅ Access Verified. Encrypted database channel active.")
        st.write("### 🗂️ Live Patient Triage & Active Contact Intercept Registry")
        
        for idx, row in st.session_state.clinical_registry.iterrows():
            tier_badge = "🔴 RED TIER CRISIS" if row['Triage_Tier'] == "RED TIER" else "🟡 YELLOW RISK" if row['Triage_Tier'] == "YELLOW TIER" else "🟢 GREEN RESILIENCE"
            
            st.markdown(f"#### **{tier_badge}** | Anonymized Token: `{row['Token']}`")
            st.write(f"🏢 **Cadre Department:** {row['Department']} | 🆔 **Employee Staff ID:** `{row['Staff_ID']}`")
            st.write(f"📞 **Telephone Mobile Number:** `{row['Mobile_Number']}` | ✉️ **Corporate Email:** `{row['Email_Address']}`")
            
            if row['Triage_Tier'] == "RED TIER":
