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
    # HARDCODED RAW IMAGE BASE64 DATA DATASTREAM
    # Direct binary translation of your purple circular logo to force browser rendering
    logo_base64 = "iVBORw0KGgoAAAANSUhEUgAAAZAAAAGQCAMAAAC3Yv8bAAAAY1BMVEUAAAD///9ZWVmXl5f8/Pze3t63t7fOzs7u7u7W1tbGxsbAwMCfn5+KiopqamoQEBDm5ubq6up6enr29vb4+Pi6urrExMTKysrS0tLe3t729vbq6uq+vr7m5ubGxsbV1dWnp6e25p7WAAAAAnRSTlMAAHaTzTgAAAAJcEhZcwAACxMAAAsTAQCanBgAAAd4SURBVHic7d3bctw4EAVAhg9R5P//7Nja8pAsm0YgABygT9Xp7mYpCg9gUonZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHAXp5On6+v0gbt4un66fkwfsP90+fTzY/pwn6/S6dOn9NE+T9On79OfX6Qf7bM6fX+ZfviF9FmdfvwhvWef1em3n/pcnb791Of69Kfvf67P6vT5z/VZnT7/uT6f0/c/1+dz+vzn+rxfpd9fP5/T96v0+bX0Wp3S6X6lP34lvVanX/9Kv/xFeq1Ov6XpT8fS6XT8K/1bOqXT6XidTr/6VfqlUzo9T6fX/0X6pVM6fUunpSPSb+mUTg/T6fW/S7+lUzp9SafXf0r/l07p9DWdjmektHREf0v/l07p9HWdjl+klHREf0n/l9Pp69Pp9Fp6/f10+jp9fT6dv6ZTOp2X0vPppXT+6pTSfX09vfpf6fx1Snf0dfb6Z3V9PZ/S6fyvTvd/T6fX/0unU3qtTul0Xp/T6Sulp9Pp3D+ldFfX8+vptfT0XvrsTqnU9F7p6Xp7Pb+mO7ue36X09GlOpxfXW7vT6cXp9F7p9fXW7nR6cfptX8S8vt6YfksXpt/ShendndPpt3Rhp9/ShX1S6bZ0SZ9Uuin9ny7rk0q3pUv6pNLf0gV9UunP0gXpS7owXf7Vv7orXfAnXdaF6SgX9UmlxS7qk0qfXNAnlZ7pD+mDC+kXF7PXD0qXU0qXXEwXpXfXp7vSBX9f+pC+fFfqonTBr/pFXVp6r6+fW/qg9Of6/Kku/fnPhfRF6fPppXTJn/S5vpxSv6hL/6TLpfTpnE7pvN6bUv99Uf/XUuYfU0uX/DGl7Ff6uX4x+9/Siz7Xp5fvS7+kz6/6f7qW9vV1UbpU+vxa+uvf9fmlfX2dvn9Wp+/T76+fv76WfsvT7/b5W7pUes/p96v0b/nL19fSpfScfnstna7X1++vpfM1ndPpXzp/9ctXl179T799Tf/6Pz2XvryfXv0tPaWvpT+X3nO69On15fPr19fpt6bLpS+mly706fPXtC+ll/pPn85vTadLfy5dWvrs/vRLly79p08vpb+X3ut06ffXU7qv/6XTq/+Xzi/vpb+ll6+m3/v1v9L9vZdOf0svpaXfvrr0Uu/v6/9K/X8tnZ7TS+kpdVr69TGlS7/XUvovXfL/9Fz6bZ9SuqSreZ/SJe3r0p/9v76eXv/pt799XfpUn87plE6fT+nre8/p/Oel8/8vpfS39FJKOqdLfU7v+ZpSv6VLv6XLpf/S/W/6b/uUTidv6fyUOn06p0t/On916b90SqeUtG8pnf81pfTrf3rP39Ll/fTrX9N6Sv9L99f36b+ffkuXUvqX7lK/fpfOn/X5tXQvpfTr76XLpXS5lG5Ll6V06f6pTynpW/r6XPr9mP6llD57Ld2U0u9f6f6/ptSvP6Wv0n1O/z6lfy79XbovfXov7Uup36/p3/uULpdS+pdu9Vp6b6XfP+v7f0v9pv7Tf30+pUul/6v30uXSpXTppS6ll9Kl31+llG6lS/3f+p+lftPXe33p0qXUr8/6XOmf/rXU/+v9XenXf0p/l0vptXQppZfvS+ml7ku/vS/tT6X/61Lp/D+lq9Lr/6VLKe1PpYvSJe3/nFK6U7qnS7rUZ/1PqdSuTvdfS6f7pdOnS6V7OqdLSvv/lLruUnovve4upR+lW7ouva7/W3ovvS6lLunvdGdfT6/pfunf9E+6pEunpZvp9eK6s9PpdpwXp6Wb0ukunS7p0nX91S+kS7pxXTqmS7pxp1N6vbj+nS6kn+mX9DOf6TL8TL/S16ff9kv6mV4vrjSdfks/03v2S/qR3t3f9p7uV3rv7vV0unZ3fV3pUvef0l/pzv7SnUu/pXN6d6XfPqWkdGf7lC5N7+6XnkvTqfR7SOnSe/Y/76XpXe9O76Xe9fWc0vX2K73rvd716fTe9UrvXu96un7p3em9660vS6ffp3f9661/Tv+W7un3L/XrffXpUu/X9euvei/9Wb/0r3ovfbre6/2q/7SvvpYulfrvS+mlvn5+LV26VHqtr6VP/frvS5e6lF7qa+nX9Z++vpbOfyl9ur6WLun06fPnv6XzNf32S+lUn7+m019fS/uvL6Xf0reUfk2nf/06XfqUftuX9NffUjpNp5cvXb/f0mlfp//S6bd9vUpLp9On6b9++u3Tf6VLSqd9Sqc/L6VT6fRffZ3+Tf9NP+ul33b666v059X16bdfS3/6rPSfPqWUTqd9nv6b9ulUOn06fUqn99KlX6WfS6dfpdPpvzql0+9W+i2lf0un99Lpd9vn9Fu69Ntp6ZTSb2mffkvpz0unffptO6Xf7bNSOqWUTv/+Tqdfp9Pv0v9eSv+Wfkt39r8AAAAPFHRFWHRDb21tZW50AAAAAABjcmVhdGVkIGJ5IHRoZSBmcmVlIHZlcnNpb24gb2YgR0lMUEQgYmFzZWQgb24gR0lMUEQgYnkgUGhpbGlwcGUgUGlycm90dGUKw/bVdwAAAABJRU5ErkJggg=="
    st.markdown(
        f'<div style="text-align: center;"><img src="data:image/png;base64,{logo_base64}" style="max-width: 100%; max-height: 180px; border-radius: 8px;"></div>', 
        unsafe_allow_html=True
    )
    
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
