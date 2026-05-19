def classify_incident(alert_type):
    severity_map = {
        "BRUTE_FORCE": "LOW",
        "RECONNAISSANCE": "MEDIUM",
        "MALWARE": "CRITICAL"
    }
    return severity_map.get(alert_type, "UNKNOWN")