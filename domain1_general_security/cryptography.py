import hashlib, secrets

def hash_sha256(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def generate_token(length=32):
    return secrets.token_hex(length)

def verify_hash(data, existing_hash):
    return hash_sha256(data) == existing_hash