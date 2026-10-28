"""
VitaTrack - Habit & Wellness Tracker
Main entry point with menu-driven interface.

Stages implemented:
  Stage 4  - Loops and iteration (menu loop)
  Stage 5  - Functions
  Stage 6  - Data structures (list of dicts)
  Stage 7  - File handling (via modules.storage)
  Stage 8  - Error handling (via modules.validation)
  Stage 9  - Modular programming
"""

from modules.records import add_record, view_all_records, delete_record, view_report_for_date
from modules.reports import display_statistics, export_summary_report
from modules.storage import load_records
from modules.validation import get_valid_menu_choice

MENU = """
============================================================
              VitaTrack - Main Menu
============================================================
  1. Log Daily Wellness
  2. View All Records
  3. View Report for a Date
  4. View Statistics
  5. Delete a Record
  6. Export Summary Report
  7. Exit
============================================================
"""


def main():
    print("=" * 60)
    print("   Welcome to VitaTrack - Your Personal Wellness Tracker")
    print("=" * 60)

    # Load existing records from file (Stage 7 + 8)
    records = load_records()
    print(f"  Loaded {len(records)} record(s) from storage.\n")

    # Menu loop (Stage 4)
    while True:
        print(MENU)
        choice = get_valid_menu_choice("Select an option (1-7): ", [1, 2, 3, 4, 5, 6, 7])

        if choice == 1:
            records = add_record(records)
        elif choice == 2:
            view_all_records(records)
        elif choice == 3:
            view_report_for_date(records)
        elif choice == 4:
            display_statistics(records)
        elif choice == 5:
            records = delete_record(records)
        elif choice == 6:
            export_summary_report(records)
        elif choice == 7:
            print("\n  Thank you for using VitaTrack. Stay well!")
            print("=" * 60)
            break


if __name__ == "__main__":
    main()