import json
from datetime import datetime

# IMPLEMENT: Convert ISO timestamp (e.g. "2025-08-21T12:00:00Z") to milliseconds
def iso_to_millis(iso_str):
    dt = datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%SZ")
    return int(dt.timestamp() * 1000)


# IMPLEMENT: Normalize a message into the unified format
def normalize_message(message, source_format):
    """
    message: dict with data
    source_format: either "format1" or "format2"
    """
    if source_format == "format1":  # ISO format
        return {
            "id": message["id"],
            "timestamp": iso_to_millis(message["timestamp"]),
            "text": message["text"]
        }
    elif source_format == "format2":  # already in ms
        return {
            "id": message["msg_id"],
            "timestamp": message["time_ms"],
            "text": message["body"]
        }
    else:
        raise ValueError("Unknown format")


def main():
    # Load both files
    with open("d:\Pragyan\projects and files\python files\delloite virtual intern\data1.json") as f:
        data1 = json.load(f)

    with open("d:\Pragyan\projects and files\python files\delloite virtual intern\data2.json") as f:
        data2 = json.load(f)

    # Normalize both datasets
    result = []
    for msg in data1:
        result.append(normalize_message(msg, "format1"))
    for msg in data2:
        result.append(normalize_message(msg, "format2"))

    # Save result
    with open("d:\Pragyan\projects and files\python files\delloite virtual intern\data-result.json", "w") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    main()
