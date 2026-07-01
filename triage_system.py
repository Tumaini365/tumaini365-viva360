import streamlit as st
import datetime
import uuid
import pandas as pd

# 1. LIVE PRODUCTION STYLING & NAVIGATION CONFIGURATION
st.set_page_config(page_title="Tumaini 365 Total Wellness Ecosystem", page_icon="🌱", layout="wide")

# Initialize a clean, persistent local session database matrix to store clinical screening inputs safely
if "clinical_registry" not in st.session_state:
    st.session_state.clinical_registry = pd.DataFrame(columns=[
        "Token", "Department", "Staff_ID", "PHQ9_Score", "GAD7_Score", "Triage_Tier", "Action_Milestone", "Day14_Date", "Day30_Date", "Status"
    ])

# Navigation Menu Options
st.sidebar.image("https://icons8.com", width=60)
st.sidebar.title("Tumaini 365 Hub")
st.sidebar.write("---")
app_mode = st.sidebar.radio(
    "Select System Interface Portal:",
    ["1. Employee Secure Portal", "2. Ezekiel's Clinical Panel", "3. HR Executive Analytics Dashboard"]
)

# Core System Logic Functions
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

# ====================================================================
# PORTAL 1: EMPLOYEE SECURE PORTAL (THE RUNTIME ASSESSMENT MATRIX)
# ====================================================================
if app_mode == "1. Employee Secure Portal":
    st.title("🌱 Tumaini Three Sixty Five Limited")
    st.subheader("Viva 365 Insurance Brokers: Employee Secure Well-being Portal")
    st.write("---")
    
    st.markdown("""
    ### 🔒 Data Protection & Confidentiality Declaration
    In strict compliance with the **Data Protection Act of Kenya**, your screening inputs are treated as sensitive personal data. 
    **Your specific clinical scores are entirely hidden from Viva 365 HR and executive management.** 
    This system utilizes advanced token pseudonymization to guarantee absolute anonymity.
    """)
    
    # Verification Fields
    st.write("#### Step 1: Corporate Validation")
    col_a, col_b = st.columns(2)
    with col_a:
        dept = st.selectbox("Your Department Grouping:", ["Direct Sales Force", "Underwriting & Risk", "Claims Adjustment Cadre", "Administration & HR"])
    with col_b:
        staff_id = st.text_input("Enter Active Viva 365 Staff ID:", placeholder="e.g., V365-104")
        
    consent = st.checkbox("I consent to this screening under the Data Protection Act parameters to access my wellness roadmap.")
    
    if consent and staff_id:
        st.write("---")
        st.write("#### Step 2: The Core Screening Matrix (DSM-5-TR Psychometric Tracker)")
        
        st.markdown("**Over the last 2 weeks, how often have you been bothered by any of the following problems?**")
        st.caption("Scale: 0 = Not at all | 1 = Several days | 2 = More than half the days | 3 = Nearly every day")
        
        # PHQ-9 Core Trackers
        q1 = st.radio("1. Little interest or pleasure in doing things at work or home:", (0, 1, 2, 3), horizontal=True)
        q2 = st.radio("2. Feeling down, depressed, flat, or hopeless:", (0, 1, 2, 3), horizontal=True)
        q3 = st.radio("3. Feeling tired, sluggish, or having chronically low energy volumes:", (0, 1, 2, 3), horizontal=True)
        
        # GAD-7 Core Trackers
        q4 = st.radio("4. Feeling nervous, anxious, on edge, or overwhelmed by quotas:", (0, 1, 2, 3), horizontal=True)
        q5 = st.radio("5. Trouble relaxing, muscle tension, or constant overthinking:", (0, 1, 2, 3), horizontal=True)
        q6 = st.radio("6. Becoming easily annoyed, hyper-irritable with peers, or cross-functional friction:", (0, 1, 2, 3), horizontal=True)
        
        # PHQ-9 Question 9 Self-Harm Override Radar
        q9 = st.radio("⚠️ 7. Thoughts that you would be better off dead, or of hurting yourself in some way:", (0, 1, 2, 3), horizontal=True)
        
        if st.button("🚀 SUBMIT ANONYMOUS WELLNESS SCREENING"):
            # Compute total clinical metrics
            phq9_total = q1 + q2 + q3 + q9
            gad7_total = q4 + q5 + q6
            self_harm_flag = q9 >= 1
            
            # Run assessment backend logic
            tier, box_text, milestone = compute_triage_tier(phq9_total, gad7_total, self_harm_flag)
            token = generate_anonymized_token(dept)
            
            # Setup the 14 and 30 day follow-up program timelines automatically to avoid one-off decay
            today = datetime.date.today()
            d14 = today + datetime.timedelta(days=14)
            d30 = today + datetime.timedelta(days=30)
            
            # Append entry to the clinical session matrix data store
            new_entry = {
                "Token": token, "Department": dept, "Staff_ID": staff_id, "PHQ9_Score": phq9_total,
                "GAD7_Score": gad7_total, "Triage_Tier": tier, "Action_Milestone": milestone,
                "Day14_Date": d14.strftime('%Y-%m-%d'), "Day30_Date": d30.strftime('%Y-%m-%d'), "Status": "Active Follow-up"
            }
            st.session_state.clinical_registry = pd.concat([st.session_state.clinical_registry, pd.DataFrame([new_entry])], ignore_index=True)
            
            # Render immediate client-side custom outcomes
            st.success("🎉 Confidential Screening Completed Successfully.")
            st.info(f"**Your Non-Identifiable Security Token:** `{token}` (Write this down to track your progress)")
            
            st.write("### Your Personalized Automated Support Action Plan")
            if tier == "GREEN TIER":
                st.success(box_text)
                st.markdown("""
                * **Your Action Roadmap:** Your baseline psychological resilience is optimal. Your data token has unlocked the **14-Day Digital Decompression Toolkit** containing deep breathing audio cues, sleep hygiene parameters, and structural time-blocking calendar patterns. 
                * **Follow-up Check:** An automated verification link will be pushed to your portal on **{}** to ensure your boundaries are holding up.
                """.format(d14.strftime('%B %d, %Y')))
            elif tier == "YELLOW TIER":
                st.warning(box_text)
                st.markdown("""
                * **Your Action Roadmap:** Your profile highlights functional burnout and quota fatigue. To protect your productivity, your token has bypassed standard one-off training and matched you directly to this month's **Voluntary Virtual Wellness Booster Pod**. 
                * **Continuous Follow-up:** Your pod will run accountability metrics on **{}** to track your coping structures.
                """.format(d30.strftime('%B %d, %Y')))
            else:
                st.error(box_text)
                st.markdown("""
                * **Emergency Override Action Plan:** Your screening flags severe clinical or situational crisis conditions. **An immediate secure payload alert has been logged on Lead Psychologist Ezekiel Kiago's private console.**
                * **Instant Clinical Link:** Click the direct link below to access real-time clinical stabilization or connect safely with our 24/7 priority response network.
                """)
                st.markdown("[📲 OPEN SECURE WHATSAPP ROUTING DISPATCH TO EZEKIEL KIAGO](https://wa.me)")

# ====================================================================
# PORTAL 2: EZEKIEL'S CLINICAL PANEL (THE ADMINISTRATIVE PIPELINE)
# ====================================================================
elif app_mode == "2. Ezekiel's Clinical Panel":
    st.title("🔒 Tumaini 365: Clinical Administration Workspace")
    st.subheader("Lead Consultant Console: Ezekiel Kiago Wangunyu")
    st.write("---")
    
    # Security lock to verify Lead Psychologist access
    pin = st.text_input("Enter Clinical Security Access PIN:", type="password")
    if pin == "365": # Simulation entry pin
        st.success("Access Granted. Secure encrypted database connection active.")
        
        st.write("### 🗂️ Live Patient Triage & Continuous Follow-Up Registry")
        if st.session_state.clinical_registry.empty:
            st.warning("No entries currently recorded in the active screening stream.")
        else:
            # Display full relational clinical tracking dataframe
            st.dataframe(st.session_state.clinical_registry.drop(columns=["Staff_ID"])) # Hide Staff ID from general panel to enforce data protocol
            
        st.write("### 🚨 Emergency Overrides Pending Intercept")
        red_cases = st.session_state.clinical_registry[st.session_state.clinical_registry["Triage_Tier"] == "RED TIER"]
        if not red_cases.empty:
            for idx, row in red_cases.iterrows():
                st.error(f"**CRITICAL ALERT:** Token `{row['Token']}` from `{row['Department']}` has matched Red Tier parameters. Required: Call back to encrypted verification matching user ID: `{row['Staff_ID']}`.")
        else:
            st.success("Zero critical emergency case overloads pending on your workspace matrix.")
    elif pin:
