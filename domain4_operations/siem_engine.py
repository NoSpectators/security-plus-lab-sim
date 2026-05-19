def process_events(events):
    alerts = []

    for e in events:
        if e["event_type"] == "LOGIN_FAIL":
            alerts.append(("BRUTE_FORCE", e))
        if e["event_type"] == "PORT_SCAN":
            alerts.append(("RECONNAISSANCE", e))
        if e["event_type"] == "MALWARE_EXECUTION":
            alerts.append(("MALWARE", e))

    return alerts