from shared.event import SecurityEvent

class SecurityEngine:
    def __init__(self):
        self.events = []

    def ingest_event(self, event: SecurityEvent):
        self.events.append(event)

    def get_events(self):
        return [e.to_dict() for e in self.events]

    def clear(self):
        self.events = []