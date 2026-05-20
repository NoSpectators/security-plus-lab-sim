class AccessControl:
    def __init__(self):
        self.permissions =  {
            "admin": ["read", "write", "delete"],
            "analyst": ["read"],
            "guest": [],
        }
    def is_allowed(self, role, action):
        return action in self.permissions.get(role, [])