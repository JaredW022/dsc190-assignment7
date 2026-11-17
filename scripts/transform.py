import csv
from pathlib import Path

SOURCE = Path("data/clean/events.csv")
OUTPUT = Path("data/transformed/events.csv")
COLUMNS = ["user_id", "timestamp", "event_type", "duration_seconds", "date"]

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

with SOURCE.open(newline="") as source, OUTPUT.open("w", newline="") as output:
    reader = csv.DictReader(source)
    writer = csv.DictWriter(output, fieldnames=COLUMNS)
    writer.writeheader()

    for row in reader:
        row["date"] = row["timestamp"][:10]
        writer.writerow(row)
