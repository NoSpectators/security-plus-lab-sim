def analyze_logs(logs):
    findings = {
        "failed_logins": 0,
        "malware_alerts": 0
    }
    for log in logs:
        if "LOGIN_FAIL" in log:
            findings["failed_logins"] += 1
        if "MALWARE" in log:
            findings["malware_alerts"] += 1

    return findings