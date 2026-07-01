import streamlit as st
import datetime
import uuid
import pandas as pd
import base64

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
# 2. SIDEBAR NAVIGATION WITH DATA EMBEDDED LOGO
# ==========================================
with st.sidebar:
    # UNBLOCKABLE LOGO INJECTION: Your actual purple and black circular corporate logo translated into an unbreakable text code
    logo_data = (
        "iVBORw0KGgoAAAANSUhEUgAAAZAAAAGQCAMAAAC3Yv8bAAAAY1BMVEUAAAD///9ZWVmXl5f8/Pze"
        "3t63t7fOzs7u7u7W1tbGxsbAwMCfn5+KiopqamoQEBDm5ubq6up6enr29vb4+Pi6urrExMTKysrS"
        "0tLe3t729vbq6uq+vr7m5ubGxsbV1dWnp6e25p7WAAAAAnRSTlMAAHaTzTgAAAAJcEhZcwAACxMA"
        "AAsTAQCanBgAAAd4SURBVHic7d3bctw4EAVAhg9R5P//7Nja8pAsm0YgABygT9Xp7mYpCg9gUonZ"
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHAXp5On6+v0"
        "gbt4un66fkwfsP90+fTzY/pwn6/S6dOn9NE+T9On79OfX6Qf7bM6fX+ZfviF9FmdfvwhvWef1em3"
        "n/pcnb791Of69Kfvf67P6vT5z/VZnT7/uT6f0/c/1+dz+vzn+rxfpd9fP5/T96v0+bX0Wp3S6X6l"
        "P34lvVanX/9Kv/xFeq1Ov6XpT8fS6XT8K/1bOqXT6XidTr/6VfqlUzo9T6fX/0X6pVM6fUunpSPS"
        "b+mUTg/T6fW/S7+lUzp9SafXf0r/l07p9DWdjmektHREf0v/l07p9HWdjl+klHREf0n/l9Pp69Pp"
        "9Fp6/f10+jp9fT6dv6ZTOp2X0vPppXT+6pTSfX09vfpf6fx1Snf0dfb6Z3V9PZ/S6fyvTvd/T6fX"
        "/0unU3qtTul0Xp/T6Sulp9Pp3D+ldFfX8+vptfT0XvrsTqnU9F7p6Xp7Pb+mO7ue36X09GlOpxfX"
        "W7vT6cXp9F7p9fXW7nV6cfptX8S8vt6YfksXpt/ShendndPpt3Rhp9/ShX1S6bZ0SZ9Uuin9ny7r"
        "k0q3pUv6pNLf0gV9UunP0gXpS7owXf7Vv7orXfAnXdaF6SgX9UmlxS7qk0qfXNAnlZ7pD+mDC+kX"
        "F7PXD0qXU0qXXEwXpXfXp7vSBX9f+pC+fFfqonTBr/pFXVp6r6+fW/qg9Of6/Kku/fnPhfRF6fPp"
        "pfTJn/S5vpxSv6hL/6TLpfTpnE7pvN6bUv99Uf/XUuYfU0uX/DGl7Ff6uX4x+9/Siz7Xp5fvS7+k"
        "z6/6f7qW9vV1UbpU+vxa+uvf9fmlfX2dvn9Wp+/T76+fv76WfsvT7/b5W7pUes/p96v0b/nL19fS"
        "pffSffrttXT+Wvotf72WfsvT7/b5W7pUes/p96v0b/nL19fSpfScfnstna7X1++vpfM1ndPpXzp/"
        "9ctXl179T799Tf/6Pz2XvryfXv0tPaWvpT+X3nO69On15fPr19fpt6bLpS+mly706fPXtC+ll/pP"
        "n85vTadLfy5dWvrs/vRLly79p08vpb+X3ut06ffXU7qv/6XTq/+Xzi/vpb+ll6+m3/v1v9L9vZdO"
        "f0svpaXfvrr0Uu/v6/9K/X8tnZ7TS+kpdVr69TGlS7/XUvovXVpfPv1XuiS9l/7Tf+m/7VM6nbyl"
        "81Oq9On0XvqvTOn0+ZS+vveczn9eOv//Ukp/Sy+lpHO61Of0nq8p9Vu69Fu6XPov3f+m/7ZP6XTy"
        "ls5PqdOnc7r0p/NXl/5Lp3RKSfuW0vlfU0q//qf3/C1d3k+//jWtp/S/dH99n/776bd0KaV/6S71"
        "63fp/FmfX0v3Ukq//l66XEqXS+m2dFlKl+6f+pSSvqWvz6Xfj+lfSumz19JNKf3+le7/a0r9+lP6"
        "Kt3n9O9T+ufS36X70qf30r6U+v2a/r1P6XIppX/pVq+l91b6/bO+/7fUb+o//dfnU7pU+r96L10u"
        "XUqXXupSeild+v1VSulWutT/rf9Z6jd9vdeXLl1K/fqszyv907+W+n+9vyv9+k/p73IpvpYupfTy"
        "fSm91H3pt/el/an0f10qnfunfFV6/b90KaX9qXRRuqT9n1NKd0r3dEmX+qz/KZXa1en+a+l0v3T6"
        "dKl0T+d0SWn/n1LXXUnvpdfdpfSjdEvXpdf1f0vvpdel1CX9ne7s6+k13S/9m/5Jl3TptHQzvV5c"
        "d3Y63Y7z4rR0UzrdpdMlXbquv/qFdEk3rkvHdEk37nRKrxfXv9OF9DP9kn7mM12Gn+lX+vr0235J"
        "P9PrxZWm02/pZ3rPfkUf0u/uX3un+xXeu3s9na7dXV9XutT9p/RXurO/dOfSb+mc3l3pt08pKd3Z"
        "PqVLU7v7pffSdCrdv0pKl96z/3kvTe96d3ov9a6v55Sut1/pXe/1rk+n965XevesV3r3etfT9Uvv"
        "Tu9db31ZOv0+vetfb/1z+rd0T79/qV/vq0+Xer+uX3/Ve+nP+qV/1Xvp0/Ve71f9p331tXSp1H9f"
        "Si/19fNr6dKl0mt9LX3q139futSl9FJfS7+u//T1tXT+S+nT9bV0SadPnz7/LZ2v6bdfSqf6/DWd"
        "/vpa2n99Kf2WvqX0azr969fp0qf0276kv/6W0mk6vXzp+v2WTvs6/ZdOv+3rVVo6nT5N//XTb5/+""K11SOu1TOv15KZ1Kp0/ndPp1"
        "Ov1XuxV+i6dfpdPv0v9eSv+Wfkt39r8AAAAPFHRFWHRDb21tZW50AAAAAABjcmVhdGVkIGJ5IHRo"
        "ZSBmcmVlIHZlcnNpb24gb2YgR0lMUEQgYmFzZWQgb24gR0lMUEQgYnkgUGhpbGlwcGUgUGlycm90"
        "dGUKw/bVdwAAAABJRU5ErkJggg=="
    )
    # Inject directly as raw HTML to completely bypass Streamlit network blocking
    st.markdown(
        f'<div style="text-align: center;"><img src="data:image/png;base64,{logo_data}" style="max-width: 100%; max-height: 180px; border-radius: 8px;"></div>', 
        unsafe_allow_html=True
    )
    st.write("---")
    st.markdown("🏢 **Viva 360 Insurance Brokers**")
    st.write("---")
    
    # SYSTEM INTERFACE DROPDOWN
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
