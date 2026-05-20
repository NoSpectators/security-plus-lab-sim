SECURITY_CONTROLS = {
    "MFA_ENABLED": True,
    "PASSWORD_POLICY": True,
    "LOG_MONITORING": False,
    "BACKUP_POLICY": True
}

def audit_controls():
    failed_controls = []
    for control, enabled in SECURITY_CONTROLS.items():
        if not enabled:
            failed_controls.append(control)

    return failed_controls