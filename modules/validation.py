"""
validation.py
Input validation and error handling helpers.

Stage 8 - Error Handling
"""

from datetime import datetime


def get_valid_name(prompt="Enter your name: "):
    """Prompt until a non-empty name of at least 2 characters is entered."""
    while True:
        try:
            name = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  [!] Input interrupted.")
            raise
        if not name:
            print("  [!] Name cannot be empty. Please try again.")
            continue
        if len(name) < 2:
            print("  [!] Name must be at least 2 characters.")
            continue
        return name


def get_valid_int(prompt, min_val=None, max_val=None):
    """Prompt until a valid integer within optional bounds is entered."""
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("  [!] Invalid input. Please enter a whole number.")
            continue
        except (EOFError, KeyboardInterrupt):
            print("\n  [!] Input interrupted.")
            raise
        if min_val is not None and value < min_val:
            print(f"  [!] Value must be at least {min_val}.")
            continue
        if max_val is not None and value > max_val:
            print(f"  [!] Value must be at most {max_val}.")
            continue
        return value


def get_valid_float(prompt, min_val=None, max_val=None):
    """Prompt until a valid float within optional bounds is entered."""
    while True:
        try:
            value = float(input(prompt).strip())
        except ValueError:
            print("  [!] Invalid input. Please enter a number (e.g. 7.5).")
            continue
        except (EOFError, KeyboardInterrupt):
            print("\n  [!] Input interrupted.")
            raise
        if min_val is not None and value < min_val:
            print(f"  [!] Value must be at least {min_val}.")
            continue
        if max_val is not None and value > max_val:
            print(f"  [!] Value must be at most {max_val}.")
            continue
        return value


def get_valid_date(prompt="Enter date (YYYY-MM-DD) or press Enter for today: ", allow_today=True):
    """Prompt until a valid YYYY-MM-DD date is entered."""
    while True:
        try:
            date_str = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  [!] Input interrupted.")
            raise
        if not date_str and allow_today:
            return datetime.now().strftime("%Y-%m-%d")
        if not date_str:
            print("  [!] Date cannot be empty.")
            continue
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("  [!] Invalid date format. Use YYYY-MM-DD (e.g. 2025-01-15).")


def get_valid_menu_choice(prompt, valid_choices):
    """Prompt until a menu choice from valid_choices is entered."""
    while True:
        try:
            choice = int(input(prompt).strip())
        except ValueError:
            print("  [!] Invalid input. Please enter a number.")
            continue
        except (EOFError, KeyboardInterrupt):
            print("\n  [!] Input interrupted.")
            raise
        if choice not in valid_choices:
            print(f"  [!] Invalid option. Choose from {valid_choices}.")
            continue
        return choice


def get_yes_no(prompt="Confirm? (y/n): "):
    """Prompt until 'y' or 'n' is entered. Returns True for 'y'."""
    while True:
        try:
            answer = input(prompt).strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n  [!] Input interrupted.")
            raise
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("  [!] Please enter 'y' or 'n'.")