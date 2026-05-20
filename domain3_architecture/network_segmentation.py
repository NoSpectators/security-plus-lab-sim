NETWORK_SEGMENTS = {
    "DMZ": ["web_server"],
    "INTERNAL": ["db_server", "auth_server"]
}

def can_communicate(source, destination):
    if source == "DMZ" and destination == "db_server":
        return False
    return True