from shared.event import SecurityEvent

def simulate_attack_scenario():
    return [
        SecurityEvent("PORT_SCAN", "attacker", {"target": "192.168.1.10"}),
        SecurityEvent("LOGIN_FAIL", "attacker", {"user": "admin"}),
        SecurityEvent("LOGIN_FAIL", "attacker", {"user": "admin"}),
        SecurityEvent("MALWARE_EXECUTION", "endpoint", {"file": "payload.exe"})
    ]