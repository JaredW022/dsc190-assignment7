import csv
from datetime import datetime
from pathlib import Path

SOURCE = Path("data/raw/events.csv")
OUTPUT = Path("data/clean/events.csv")
COLUMNS = ["user_id", "timestamp", "event_type", "duration_seconds"]
VALID_EVENTS = {"click", "login", "scroll", "view", "purchase"}


def parse_timestamp(value: str) -> datetime:
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        return datetime.strptime(value, "%m/%d/%Y %H:%M:%S")


OUTPUT.parent.mkdir(parents=True, exist_ok=True)

with SOURCE.open(newline="") as source, OUTPUT.open("w", newline="") as output:
    reader = csv.DictReader(source)
    writer = csv.DictWriter(output, fieldnames=COLUMNS)
    writer.writeheader()

    for row in reader:
        values = {column: (row.get(column) or "").strip() for column in COLUMNS}
        if not all(values.values()):
            continue
        if values["event_type"] not in VALID_EVENTS:
            continue

        try:
            duration = int(values["duration_seconds"])
            timestamp = parse_timestamp(values["timestamp"])
        except ValueError:
            continue

        if duration <= 0:
            continue

        values["duration_seconds"] = str(duration)
        values["timestamp"] = timestamp.strftime("%Y-%m-%dT%H:%M:%S")
        writer.writerow(values)
