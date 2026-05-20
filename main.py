# main.py

from core.engine import SecurityEngine
from shared.event import SecurityEvent

# -----------------------------
# Domain 1 Imports
# -----------------------------
from domain1_general_security.authentication import Authenticator
from domain1_general_security.access_control import AccessControl
from domain1_general_security.cryptography import generate_token

# -----------------------------
# Domain 2 Imports
# -----------------------------
from domain2_threats_vulnerabilites.attack_simulator import (
    simulate_attack_scenario
)
from domain2_threats_vulnerabilites.log_analyzer import analyze_logs
from domain2_threats_vulnerabilites.malware_simulator import detect_malware
from domain2_threats_vulnerabilites.vulnerability_rules import (
    check_vulnerable_ports
)

# -----------------------------
# Domain 3 Imports
# -----------------------------
from domain3_architecture.firewall import Firewall
from domain3_architecture.network_segmentation import can_communicate
from domain3_architecture.secure_design_principles import (
    list_principles
)

# -----------------------------
# Domain 4 Imports
# -----------------------------
from domain4_operations.siem_engine import process_events
from domain4_operations.incident_response import classify_incident
from domain4_operations.alerting import send_alert
from domain4_operations.forensic_logger import write_forensic_log

# -----------------------------
# Domain 5 Imports
# -----------------------------
from domain5_program_management.risk_engine import calculate_risk
from domain5_program_management.compliance_checker import audit_controls
from domain5_program_management.policy_engine import validate_password
from domain5_program_management.audit_report import generate_audit_report


def print_header(title):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def main():

    print_header("SECURITY+ SIMULATION PLATFORM")

    # =========================================================
    # DOMAIN 1 — GENERAL SECURITY CONCEPTS
    # =========================================================

    print_header("DOMAIN 1 — GENERAL SECURITY")

    auth = Authenticator()

    login_success = auth.login("admin", "password123")
    print(f"Login success: {login_success}")

    access = AccessControl()

    print(
        "Admin delete permission:",
        access.is_allowed("admin", "delete")
    )

    print(
        "Analyst delete permission:",
        access.is_allowed("analyst", "delete")
    )

    token = generate_token(16)
    print(f"Generated session token: {token}")

    password_check = validate_password("WeakPass")
    print(f"Password policy compliant: {password_check}")

    # =========================================================
    # DOMAIN 2 — THREATS & VULNERABILITIES
    # =========================================================

    print_header("DOMAIN 2 — THREATS & VULNERABILITIES")

    simulated_events = simulate_attack_scenario()

    print("Simulated attack events:")

    for event in simulated_events:
        print(event.to_dict())

    logs = [
        "LOGIN_FAIL admin",
        "LOGIN_FAIL root",
        "MALWARE payload.exe"
    ]

    log_analysis = analyze_logs(logs)

    print("\nLog Analysis:")
    print(log_analysis)

    malware_detected = detect_malware("payload.exe")

    print(f"\nMalware detected: {malware_detected}")

    open_ports = [22, 23, 80, 443, 445]

    vulnerable_services = check_vulnerable_ports(open_ports)

    print("\nVulnerable Services:")
    print(vulnerable_services)

    # =========================================================
    # DOMAIN 3 — SECURITY ARCHITECTURE
    # =========================================================

    print_header("DOMAIN 3 — SECURITY ARCHITECTURE")

    firewall = Firewall()

    print("Firewall inspection results:")

    for port in open_ports:
        result = firewall.inspect(port)
        print(f"Port {port}: {result}")

    segmentation_check = can_communicate(
        "DMZ",
        "db_server"
    )

    print(
        f"\nDMZ can communicate with db_server: "
        f"{segmentation_check}"
    )

    print("\nSecure Design Principles:")

    for principle in list_principles():
        print(f"- {principle}")

    # =========================================================
    # DOMAIN 4 — SECURITY OPERATIONS
    # =========================================================

    print_header("DOMAIN 4 — SECURITY OPERATIONS")

    engine = SecurityEngine()

    for event in simulated_events:
        engine.ingest_event(event)

    raw_events = engine.get_events()

    alerts = process_events(raw_events)

    print("SIEM Alerts:")

    for alert_type, event in alerts:

        severity = classify_incident(alert_type)

        print(
            f"\nAlert: {alert_type}"
        )

        print(
            f"Severity: {severity}"
        )

        print(
            f"Event: {event}"
        )

        write_forensic_log(event)

        send_alert(
            alert_type,
            severity,
            str(event)
        )

    # =========================================================
    # DOMAIN 5 — GOVERNANCE / RISK / COMPLIANCE
    # =========================================================

    print_header("DOMAIN 5 — GOVERNANCE / RISK / COMPLIANCE")

    risk_score = calculate_risk(
        impact=8,
        likelihood=5
    )

    print(f"Calculated risk score: {risk_score}")

    failed_controls = audit_controls()

    print("\nFailed Controls:")
    print(failed_controls)

    audit_report = generate_audit_report(
        failed_controls
    )

    print("\nAudit Report:")
    print(audit_report)

    # =========================================================
    # FINAL SUMMARY
    # =========================================================

    print_header("SIMULATION COMPLETE")

    print("Security+ simulation completed successfully.")


if __name__ == "__main__":
    main()