def generate_audit_report(findings):
    return {
        "total_findings": len(findings),
        "findings": findings,
        "status": "FAIL" if findings else "PASS"
    }