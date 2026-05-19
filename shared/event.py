from datetime import datetime

class SecurityEvent:
    def __init__(self, event_type, source, data):
        self.timestamp = datetime.now().isoformat()
        self.event_type = event_type
        self.source = source
        self.data = data

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "event_type": self.event_type,
            "source": self.source,
            "data": self.data
        }