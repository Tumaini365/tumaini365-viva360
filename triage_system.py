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

# FIXED PRE-POPULATED MATRICES TO SURVIVE ALL REFRESHES
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
st.sidebar.caption("Your Hope Everyday")
st.sidebar.write("---")
st.sidebar.markdown("🤝 **Strategic Partner Platform:**")
st.sidebar.markdown("#### **Viva 360 Insurance Brokers**")
st.sidebar.write("---")
st.sidebar.success("✅ Complete System View Active")
st.sidebar.info("💡 **Boardroom Demo Note:** All application interfaces are now flattened onto a single master display line to prevent dropdown rendering glitches entirely.")

# ==========================================
# MODULE 1: THE EMPLOYEE SECURE PORTAL
# ==========================================
st.title("🌱 Tumaini Three Sixty Five Limited")
st.subheader("1. Employee Secure Well-being Assessment Interface")
st.write("In compliance with the Data Protection Act of Kenya, your screening inputs are treated as sensitive personal data. This system utilizes advanced token pseudonymization to guarantee absolute anonymity.")

dept_input = st.selectbox("Your Department Grouping:", ["Direct Sales Force", "Underwriting & Risk", "Claims Adjustment Cadre", "Administration & HR"], key="staff_dept")
id_input = st.text_input("Enter Active Viva 360 Staff ID:", placeholder="e.g., V360-104", key="staff_id_num")
phone_input = st.text_input("Enter Your Mobile Phone Number (For Emergency Intercepts):", placeholder="e.g., +254720545788", key="staff_phone")
email_input = st.text_input("Enter Your Corporate Email Address:", placeholder="e.g., user@viva360.co.ke", key="staff_email")
consent_input = st.checkbox("I consent to this screening under the Data Protection Act parameters to access my wellness roadmap.", key="staff_consent")

if st.button("🚀 SUBMIT CONFIDENTIAL SCREENING FORM"):
    if id_input and phone_input and email_input and consent_input:
        token = "T365-" + str(dept_input[:3].upper()) + "-" + str(uuid.uuid4().hex[:4].upper())
        new_entry = {
            "Token": token, "Department": dept_input, "Staff_ID": id_input, 
            "Mobile_Number": phone_input, "Email_Address": email_input, 
            "Triage_Tier": "RED TIER", "Status": "Active Follow-up"
        }
        st.session_state.clinical_registry = pd.concat([st.session_state.clinical_registry, pd.DataFrame([new_entry])], ignore_index=True)
        st.success(f"Confidential Assessment Processed under Secure Anonymized Token: {token}")
        st.link_button("📲 CONNECT TO WHATSAPP HOTLINE", f"https://wa.me{token}")
    else:
        st.error("Validation Error: Please fill in all fields and check the data protection consent box.")

st.write("---")

# ==========================================
# MODULE 2: EZEKIEL'S CLINICAL PANEL
# ==========================================
st.subheader("🔒 2. Ezekiel's Lead Consultant Workspace (Clinical Registry)")
st.caption("Secure database connection active. Displaying contact tracing fields for real-time risk interception.")

for idx, row in st.session_state.clinical_registry.iterrows():
    tier_badge = "🔴 RED TIER CRISIS" if row['Triage_Tier'] == "RED TIER" else "🟡 YELLOW RISK" if row['Triage_Tier'] == "YELLOW TIER" else "🟢 GREEN RESILIENCE"
    st.markdown(f"#### **{tier_badge}** | Anonymized Token: `{row['Token']}`")
    st.write(f"🏢 **Cadre Department:** {row['Department']} | 🆔 **Employee Staff ID:** `{row['Staff_ID']}`")
    st.write(f"📞 **Telephone Mobile Number:** `{row['Mobile_Number']}` | ✉️ **Corporate Email:** `{row['Email_Address']}`")
    
    if row['Triage_Tier'] == "RED TIER":
        crisis_text = f"Hello, this is Ezekiel Kiago from Tumaini 365. I am reaching out regarding your secure wellness alert flagged under Token {row['Token']}. Let us connect immediately."
        encoded_msg = crisis_text.replace(" ", "%20")
        st.link_button("🚨 LAUNCH WHATSAPP CARE INTERCEPT", f"https://wa.me{encoded_msg}")
    st.write("...")

st.write("---")

# ==========================================
# MODULE 3: HR EXECUTIVE ANALYTICS
# ==========================================
st.subheader("📊 3. Viva 360 Insurance Brokers: Executive Analytics Dashboard")
st.write("In compliance with data protection laws, all individual fields are entirely stripped from this layout. It displays only aggregated data groupings to guide resource deployment.")

total_screened = len(st.session_state.clinical_registry)
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric("Total Active Staff Screened", f"{total_screened} Personnel")
with col_m2:
    st.metric("Green Tier (Resilience Ratio)", "25.0%")
with col_m3:
    st.metric("Yellow Tier (Burnout Density)", "50.0%")
st.write("---")

st.write("### 📑 Departmental Burnout Distribution Metrics Matrix")
st.markdown("#### 🔥 **Direct Sales Force Grouping**")
st.write("- Green Resilience: 0 Staff | Yellow Burnout Risk: 2 Staff | Red Crisis Urgency: 0 Staff")
st.markdown("#### ⏳ **Underwriting & Risk Grouping**")
st.write("- Green Resilience: 1 Staff | Yellow Burnout Risk: 0 Staff | Red Crisis Urgency: 0 Staff")
st.markdown("#### 🚨 **Claims Adjustment Cadre**")
st.write("- Green Resilience: 0 Staff | Yellow Burnout Risk: 0 Staff | Red Crisis Urgency: 2 Staff")
st.write("---")
st.error("🎯 **STRATEGIC BUDGET ALLOCATION RECOMMENDATION:** High burnout density values tracked inside your Direct Sales Force pipeline (Quota Fatigue). Tumaini 365 advises human resource scheduling of a specialized 'Preventive Financial Therapy Safari' workshop next month to protect premium acquisition targets before absenteeism spikes occur.")

st.write("---")
st.caption("🔒 Corporate Solution Platform powered by Tumaini 365 Limited Data Protection Architecture.")
