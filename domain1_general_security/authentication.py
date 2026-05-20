
from domain1_general_security.cryptography import hash_sha256

class Authenticator:
    def __init__(self):
        self.users = {
            "admin": hash_sha256("password123")
        }
    def login(self, username, password):
        hashed = hash_sha256(password)

        if username not in self.users:
            return False
        return self.users[username] == hashed