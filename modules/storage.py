"""
storage.py
File handling: load and save wellness records.

Stage 7 - File Handling
Stage 8 - Error Handling
"""

import os

# Path relative to project root (where main.py lives)
DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "wellness_log.txt")


def ensure_data_file():
    """Create data directory and file if they do not exist."""
    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                f.write("")
    except OSError as e:
        print(f"  [!] Could not create data file: {e}")


def load_records():
    """
    Load records from the data file.
    Returns a list of dictionaries.
    Handles missing file and malformed lines gracefully.
    """
    ensure_data_file()
    records = []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) != 5:
                    print(f"  [!] Skipping malformed line {line_num}.")
                    continue
                try:
                    record = {
                        "date": parts[0],
                        "water": int(parts[1]),
                        "sleep": float(parts[2]),
                        "exercise": int(parts[3]),
                        "mood": int(parts[4]),
                    }
                    records.append(record)
                except ValueError:
                    print(f"  [!] Skipping line {line_num} (invalid numeric data).")
    except FileNotFoundError:
        print("  [!] Data file not found. Starting with an empty log.")
    except OSError as e:
        print(f"  [!] Error reading data file: {e}")
    return records


def save_records(records):
    """Write all records back to the data file. Returns True on success."""
    ensure_data_file()
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            for r in records:
                f.write(
                    f"{r['date']}|{r['water']}|{r['sleep']}|{r['exercise']}|{r['mood']}\n"
                )
        return True
    except OSError as e:
        print(f"  [!] Error saving records: {e}")
        return False