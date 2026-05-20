PASSWORD_POLICY = {
    "min_length": 12,
    "require_special": True
}

def validate_password(password):
    if len(password) < PASSWORD_POLICY["min_length"]:
        return False
    special_chars = "!@#$%^&*"
    if PASSWORD_POLICY["require_special"]:
        return any(c in special_chars for c in password)
    return True