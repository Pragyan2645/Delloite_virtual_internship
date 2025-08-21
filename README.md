# Delloite_virtual_internship
Combine code into a unified format using Python
# JSON Telemetry Normalizer

This project converts messages stored in **two different JSON formats** into a **single unified format**.  
The goal is to normalize the data so that all messages look the same regardless of their original source.

---

## 📂 Project Structure
  - main.py # Python script with the solution
  - data1.json # Input file in ISO timestamp format
  - data2.json # Input file in milliseconds format
  - data-result.json # Output file (generated after running main.py)

---

## 📝 Data Formats

### Format 1 (data1.json) – ISO timestamps
```json
[
  { "id": 1, "timestamp": "2025-08-21T12:00:00Z", "text": "Hello world" }
]
```
### Format 2 (data2.json) – Milliseconds timestamps
```json
[
  { "msg_id": 3, "time_ms": 1755777600000, "body": "Hi from format2" }
]
```
### Target Unified Format (data-result.json)
```json
[
  { "id": 1, "timestamp": 1755777600000, "text": "Hello world" },
  { "id": 3, "timestamp": 1755777600000, "text": "Hi from format2" }
]
```
## ⚙️ How It Works

The program loads both input files.

If the message uses ISO format timestamps, they are converted into milliseconds.

If the message already uses milliseconds, it is used directly.

Field names are unified:

id / msg_id → id

timestamp / time_ms → timestamp

text / body → text

All normalized messages are written into data-result.json.

## ▶️ Run the Project

1. Open the project locally on your machine.
2. Make sure data1.json and data2.json are in the same folder as main.py.
3. Run the program:
```python
python main.py
```
4. After running, open data-result.json to see the combined, normalized messages.
---
## 🔑 Key Point

The main challenge is timestamp conversion:

- 2025-08-21T12:00:00Z (ISO) → 1755777600000 (milliseconds).
  This ensures all messages share the same time format.
