from datetime import datetime

def write_forensic_log(event):
    timestamp = datetime.now().isoformat()
    log_line = f"{timestamp} | {event}\n"
    with open("forensic.log", "a") as f:
        f.write(log_line)