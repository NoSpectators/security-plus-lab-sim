class Firewall:
    def __init__(self):
        self.allowed_ports = {80, 443}
        self.blocked_ports = {23, 445}
    def inspect(self, port):
        if port in self.blocked_ports:
            return "BLOCK"
        if port in self.allowed_ports:
            return "ALLOW"