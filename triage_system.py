import datetime
import uuid

# ==========================================
# TUMAINI THREE SIXTY FIVE LIMITED
# DIGITAL TRIAGE & FOLLOW-UP INFRASTRUCTURE
# ==========================================

class TumainiTriageSystem:
    def __init__(self):
        # Secure, isolated clinical database.
        # Decoupled from corporate employer systems to guarantee anonymity.
        self.client_database = {}
        
    def generate_anonymized_token(self, department):
        """Generates a secure pseudonymized token compliant with Data Protection Acts."""
        unique_id = uuid.uuid4().hex[:6].upper()
        dept_code = department[:3].upper()
        return f"T365-{dept_code}-{unique_id}"

    def calculate_triage_tier(self, phq9_score, gad7_score, self_harm_triggered):
        """
        Applies clinical conditional routing logic based on DSM-5-TR baselines.
        Returns: Tier String, Color Code, and Immediate Operational Priority.
        """
        # Rule 1: Emergency override for any active self-harm or crisis flag
        if self_harm_triggered or (phq9_score >= 15) or (gad7_score >= 15):
            return "RED TIER", "CRITICAL BLACK/RED", "EMERGENCY CLINICAL INTERCEPT REQUIRED"
        
        # Rule 2: Interception triggers for functional burnout and anxiety
        elif (5 <= phq9_score <= 14) or (5 <= gad7_score <= 14):
            return "YELLOW TIER", "AMBER/YELLOW", "PROACTIVE INTERCEPTION & BOOSTER POD MATCHING"
        
        # Rule 3: Baseline maintenance for optimal resilience
        else:
            return "GREEN TIER", "EMERALD/GREEN", "AUTOMATED 14-DAY RESILIENCE PUSH"

    def process_new_screening(self, staff_id, department, phq9_responses, gad7_responses):
        """
        Processes inbound digital form data, calculates metrics, logs entries,
        and prints real-time workflow actions.
        """
        # Summing clinical scores (each question rated 0 to 3)
        total_phq9 = sum(phq9_responses)
        total_gad7 = sum(gad7_responses)
        
        # PHQ-9 Question 9 tracks suicidal ideation/self-harm. 
        # Any score >= 1 (Several Days or more) triggers an emergency override.
        self_harm_flag = phq9_responses[8] >= 1 
        
        # Process tiering logic
        tier, color, priority_action = self.calculate_triage_tier(total_phq9, total_gad7, self_harm_flag)
        
        # Generate the secure, non-identifiable tracking token
        client_token = self.generate_anonymized_token(department)
        
        # Setting automated tracking milestones to avoid one-off sessions
        today = datetime.date.today()
        day_14_followup = today + datetime.timedelta(days=14)
        day_30_followup = today + datetime.timedelta(days=30)
        
        # Log the anonymized record inside the secure registry
        self.client_database[client_token] = {
            "department": department,
            "phq9_score": total_phq9,
            "gad7_score": total_gad7,
            "tier": tier,
            "action_milestone": priority_action,
            "day_14_date": day_14_followup.strftime('%Y-%m-%d'),
            "day_30_date": day_30_followup.strftime('%Y-%m-%d'),
            "status": "Active Pipeline"
        }
        
        # Trigger Automated Communications Network Flow
        self.execute_notification_trigger(client_token, tier, department)
        return client_token

    def execute_notification_trigger(self, token, tier, department):
        """Simulates automated API hooks sending tailored text/email follow-ups."""
        print(f"\n[DASHBOARD ALERT] New Inbound Record Processed Successfully.")
        print(f"├─ Secure Token : {token}")
        print(f"├─ Business Unit: {department}")
        print(f"└─ Stratification: {tier}")
        print("-" * 75)
        
        if tier == "RED TIER":
            print(f"🚨 [EMERGENCY OVERRIDE TRIGGERED] Instant payload dispatched to Ezekiel Kiago's console.")
            print(f"📲 [AUTOMATED WHATSAPP DISPATCHED] -> To client {token}:")
            print(f"   'You do not have to carry this load alone. Click this single-press link to lock a secure,")
            print(f"    priority call with Ezekiel Kiago right now, or contact our 24/7 hotline directly.'")
            
        elif tier == "YELLOW TIER":
            print(f"⚡ [PROACTIVE TRIGGER ACTIVATED] Bypassing motivational one-off session structure.")
            print(f"📬 [AUTOMATED CALENDAR PUSH] -> To client {token}:")
            print(f"   'Your screening indicates high burnout risk. You have unlocked an anonymous seat")
            print(f"    in this month's voluntary Wellness Booster Pod running on Zoom/Teams.'")
            
        elif tier == "GREEN TIER":
            print(f"🌱 [PREVENTIVE TRIGGER ACTIVATED] Launching resilience tracking loops.")
            print(f"📧 [AUTOMATED MICRO-LEARNING DISPATCH] -> To client {token}:")
            print(f"   'Your baseline resilience is optimal. Access your customized 14-day digital")
            print(f"    decompression kit (time-blocking guides & mindfulness files) to hold your boundary.'")
            
    def compile_hr_macro_metrics(self):
        """Compiles aggregated metadata for corporate leadership without breaching privacy."""
        total_records = len(self.client_database)
        if total_records == 0:
            return "No records available."
            
        green_count = sum(1 for c in self.client_database.values() if c['tier'] == 'GREEN TIER')
        yellow_count = sum(1 for c in self.client_database.values() if c['tier'] == 'YELLOW TIER')
        red_count = sum(1 for c in self.client_database.values() if c['tier'] == 'RED TIER')
        
        print("\n" + "="*75)
        print("         VIVA 365 INSURANCE BROKERS: MACRO ORGANIZATIONAL VISIBILITY")
        print("   (Shared with HR Executive Committee - Fully Pseudonymized Data Groupings)")
        print("="*75)
        print(f"📊 Total Active Corporate Staff Screened: {total_records}")
        print(f"🟢 Green Tier (Optimal Resilience)      : {green_count} staff ({green_count/total_records*100:.1f}%)")
        print(f"🟡 Yellow Tier (Functional Burnout Risk): {yellow_count} staff ({yellow_count/total_records*100:.1f}%)")
        print(f"🔴 Red Tier (Clinical Crisis Intercept) : {red_count} staff ({red_count/total_records*100:.1f}%)")
        print("="*75)

# ==========================================
# LIVE TEST EXECUTION RIG (SIMULATION)
# ==========================================
if __name__ == "__main__":
    # Initialize the Tumaini 365 Core Engine
    tumaini_system = TumainiTriageSystem()
    
    print("Initializing Live Framework Simulation...")
    
    # Simulation Case 1: Frontline Sales Agent with severe burnout & emotional strain
    # Form input mimics a high-anxiety screening
    tumaini_system.process_new_screening(
        staff_id="V365-102",
        department="Direct Sales Force",
        phq9_responses=[1, 2, 2, 1, 2, 2, 1, 1, 0], # Sum = 12 (Moderate/Yellow)
        gad7_responses=[2, 3, 2, 2, 2, 2, 1]       # Sum = 14 (Moderate/Yellow)
    )
    
    # Simulation Case 2: Underwriting Specialist managing optimal workloads
    tumaini_system.process_new_screening(
        staff_id="V365-045",
        department="Underwriting & Risk",
        phq9_responses=[0, 1, 0, 0, 1, 0, 0, 0, 0], # Sum = 2 (Mild/Green)
        gad7_responses=[1, 0, 1, 0, 0, 0, 0]       # Sum = 2 (Mild/Green)
    )
    
    # Simulation Case 3: Claims Adjuster experiencing an active acute crisis (Self-harm question triggered)
    tumaini_system.process_new_screening(
        staff_id="V365-089",
        department="Claims Adjustment Cadre",
        phq9_responses=[2, 2, 3, 3, 2, 2, 1, 1, 2], # Sum = 18 + Q9 Triggered (Critical/Red)
        gad7_responses=[3, 3, 2, 2, 3, 2, 2]       # Sum = 17 (Critical/Red)
    )
    
    # Compile the final anonymized overview metrics for the Viva 365 Human Resources Director
    tumaini_system.compile_hr_macro_metrics()
