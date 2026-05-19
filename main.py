from core.engine import SecurityEngine
from domain2_threats_vulnerabilites.attack_simulator import simulate_attack_scenario
from domain4_operations.siem_engine import process_events
from domain4_operations.incident_response import classify_incident
from domain5_program_management.risk_engine import calculate_risk

print("\n=== SECURITY+ SIMULATION START ===\n")

engine = SecurityEngine()

# 1. Generate attack chain
events = simulate_attack_scenario()

# 2. Ingest into engine
for e in events:
    engine.ingest_event(e)

# 3. Extract raw events
raw_events = engine.get_events()

# 4. SIEM processing
alerts = process_events(raw_events)

print("\n[ALERTS]")
for alert_type, event in alerts:
    severity = classify_incident(alert_type)
    risk = calculate_risk(impact=8, likelihood=5)

    print(f"{alert_type} | {severity} | Risk={risk}")