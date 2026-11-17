import csv
from datetime import date
from pathlib import Path

SOURCE = Path("data/transformed/events.csv")
OUTPUT = Path("data/features/events.csv")
COLUMNS = [
    "user_id",
    "timestamp",
    "event_type",
    "duration_seconds",
    "date",
    "duration_minutes",
    "weekday",
]

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

with SOURCE.open(newline="") as source, OUTPUT.open("w", newline="") as output:
    reader = csv.DictReader(source)
    writer = csv.DictWriter(output, fieldnames=COLUMNS)
    writer.writeheader()

    for row in reader:
        row["duration_minutes"] = int(row["duration_seconds"]) / 60
        row["weekday"] = date.fromisoformat(row["date"]).strftime("%A")
        writer.writerow(row)
