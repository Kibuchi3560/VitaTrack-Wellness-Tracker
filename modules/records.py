"""
records.py
Record management: add, view, search, and delete wellness records.

Stage 6 - Data Structures (list of dicts)
Stage 8 - Error Handling
"""

from modules.calculations import calculate_overall_score
from modules.storage import save_records
from modules.validation import (
    get_valid_int,
    get_valid_float,
    get_valid_date,
    get_yes_no,
)


def add_record(records):
    """Prompt user for a new record and save it."""
    print("\n--- Log Daily Wellness ---")
    date = get_valid_date("Date (YYYY-MM-DD) [Enter for today]: ")

    # Prevent duplicates
    for r in records:
        if r["date"] == date:
            print(f"  [!] A record for {date} already exists.")
            if get_yes_no("  Overwrite it? (y/n): "):
                records.remove(r)
                break
            else:
                print("  Cancelled.")
                return records

    water = get_valid_int("Glasses of water (0-50): ", 0, 50)
    sleep = get_valid_float("Hours of sleep (0-24): ", 0, 24)
    exercise = get_valid_int("Minutes of exercise (0-600): ", 0, 600)
    mood = get_valid_int("Mood rating (1-10): ", 1, 10)

    record = {
        "date": date,
        "water": water,
        "sleep": sleep,
        "exercise": exercise,
        "mood": mood,
    }
    records.append(record)
    if save_records(records):
        print(f"\n  [OK] Record for {date} saved successfully!")
    return records


def view_all_records(records):
    """Display a tabular view of all records."""
    if not records:
        print("\n  No records found. Start logging your day!")
        return
    print("\n" + "=" * 72)
    print(f"{'Date':<14}{'Water':<12}{'Sleep':<12}{'Exercise':<12}{'Mood':<10}{'Score':<8}")
    print("=" * 72)
    for r in sorted(records, key=lambda x: x["date"]):
        score = calculate_overall_score(r["water"], r["sleep"], r["exercise"], r["mood"])
        print(
            f"{r['date']:<14}"
            f"{str(r['water']) + ' gl':<12}"
            f"{str(r['sleep']) + ' h':<12}"
            f"{str(r['exercise']) + ' min':<12}"
            f"{str(r['mood']) + '/10':<10}"
            f"{score:.1f}"
        )
    print("=" * 72)


def view_report_for_date(records):
    """Prompt for a date and display the detailed report for that date."""
    if not records:
        print("\n  No records to view.")
        return
    from modules.reports import display_daily_report

    date = get_valid_date("Enter date to view (YYYY-MM-DD): ", allow_today=False)
    for r in records:
        if r["date"] == date:
            display_daily_report(r)
            return
    print(f"\n  No record found for {date}.")


def delete_record(records):
    """Prompt for a date and delete that record after confirmation."""
    if not records:
        print("\n  No records to delete.")
        return records
    date = get_valid_date("Enter date to delete (YYYY-MM-DD): ", allow_today=False)
    for i, r in enumerate(records):
        if r["date"] == date:
            if get_yes_no(f"  Delete record for {date}? (y/n): "):
                records.pop(i)
                if save_records(records):
                    print(f"  [OK] Record for {date} deleted.")
            else:
                print("  Deletion cancelled.")
            return records
    print(f"  No record found for {date}.")
    return records