"""
validation.py
Input validation and error handling helpers.

Stage 8 - Error Handling
"""

from datetime import datetime

def get_valid_name(prompt="Enter your name: "):
    while True:
        try:
            name = input(prompt).strip()
            if len(name) >= 2:
                return name
            else:
                print("Name must be at least 2 characters long. Please try again.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            exit()
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.") 

def get_valid_int(prompt, min_value=None, max_value=None):
    while True:
        try:
            number = int(input(prompt).strip())
            if min_value is not None and number < min_value:
                print(f"Value must be at least {min_value}. Please try again.")
            elif max_value is not None and number > max_value:
                print(f"Value must be at most {max_value}. Please try again.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            exit()
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.") 

def get_valid_float(prompt, min_value=None, max_value=None):
    while True:
        try:
            number = float(input(prompt).strip())
            if min_value is not None and number < min_value:
                print(f"Value must be at least {min_value}. Please try again.")
            elif max_value is not None and number > max_value:
                print(f"Value must be at most {max_value}. Please try again.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            exit()
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

def get_valid_date(prompt="Enter a date (YYYY-MM-DD): "):
    while True:
        try:
            date_str = input(prompt).strip()
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            return date_obj.date()
        except ValueError:
            print("Invalid date format. Please enter in YYYY-MM-DD format.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            exit()
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

def get_valid_time(prompt="Enter a time (HH:MM): "):
    while True:
        try:
            time_str = input(prompt).strip()
            time_obj = datetime.strptime(time_str, "%H:%M")
            return time_obj.time()
        except ValueError:
            print("Invalid time format. Please enter in HH:MM format.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            exit()
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

def get_valid_datetime(prompt="Enter a date and time (YYYY-MM-DD HH:MM): "):
    while True:
        try:
            datetime_str = input(prompt).strip()
            datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
            return datetime_obj
        except ValueError:
            print("Invalid date and time format. Please enter in YYYY-MM-DD HH:MM format.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            exit()
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

def get_valid_choice(prompt, choices):
    while True:
        try:
            choice = input(prompt).strip()
            if choice in choices:
                return choice
            else:
                print(f"Invalid choice. Please select from {choices}.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            exit()
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

def get_valid_yes_no(prompt="Enter 'yes' or 'no': "):
    while True:
        try:
            response = input(prompt).strip().lower()
            if response in ['y', 'n']:
                return response
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            exit()
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")