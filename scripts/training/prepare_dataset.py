"""Prepare BRUNO training dataset from synthetic and raw data sources."""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SYNTHETIC_PATH = REPO_ROOT / "data" / "synthetic" / "fire_scenarios.jsonl"
OUTPUT_PATH = REPO_ROOT / "data" / "processed" / "bruno_dataset.jsonl"

SYSTEM_PROMPT = (
    "You are BRUNO (Building Rescue and Unified Navigation Operations), "
    "an AI assistant trained to assist firefighters, company officers, and incident commanders "
    "with fireground tactics, incident command, hazmat, extrication, and rescue operations."
)


def format_record(record: dict) -> dict:
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(record["messages"])
    return {"messages": messages, "source": record.get("id", "synthetic")}


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    records = []

    if SYNTHETIC_PATH.exists():
        with open(SYNTHETIC_PATH, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    records.append(json.loads(line))

    raw_dir = REPO_ROOT / "data" / "raw"
    for raw_file in raw_dir.glob("*.jsonl"):
        with open(raw_file, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    records.append(json.loads(line))

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(format_record(record)) + "\n")

    print(f"Prepared {len(records)} records → {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
