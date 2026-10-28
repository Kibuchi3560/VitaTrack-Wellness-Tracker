"""
calculations.py
Pure calculation functions for VitaTrack wellness scoring.

Stage 5  - Functions
Stage 6  - Constants and reusable logic
"""

# --- Wellness targets (constants) ---
WATER_TARGET = 8          # glasses per day
SLEEP_TARGET = 8.0        # hours per day
EXERCISE_TARGET = 30      # minutes per day
MOOD_TARGET = 7           # minimum mood rating out of 10


def calculate_water_score(glasses):
    """Return water score as a percentage, capped at 100."""
    return min((glasses / WATER_TARGET) * 100, 100.0)


def calculate_sleep_score(hours):
    """Return sleep score as a percentage, capped at 100."""
    return min((hours / SLEEP_TARGET) * 100, 100.0)


def calculate_exercise_score(minutes):
    """Return exercise score as a percentage, capped at 100."""
    return min((minutes / EXERCISE_TARGET) * 100, 100.0)


def calculate_mood_score(rating):
    """Return mood score as a percentage of 10."""
    return (rating / 10) * 100.0


def calculate_overall_score(water, sleep, exercise, mood):
    """Return the average of all four individual scores."""
    return (
        calculate_water_score(water)
        + calculate_sleep_score(sleep)
        + calculate_exercise_score(exercise)
        + calculate_mood_score(mood)
    ) / 4


def get_rating(score):
    """Return a qualitative rating for a given overall score."""
    if score >= 85:
        return "EXCELLENT"
    elif score >= 70:
        return "GOOD"
    elif score >= 50:
        return "FAIR"
    elif score >= 30:
        return "NEEDS IMPROVEMENT"
    else:
        return "POOR"


def get_advice(score):
    """Return personalised advice based on the overall score."""
    if score >= 85:
        return "Outstanding! You are thriving. Keep this routine!"
    elif score >= 70:
        return "Great job! Small improvements will make it excellent."
    elif score >= 50:
        return "You're on the right track. Focus on weaker areas."
    elif score >= 30:
        return "Try to build consistency. Start with one habit."
    else:
        return "Your wellness needs attention. Begin with small, daily steps."


# --- Status helpers used in reports ---

def get_water_status(glasses):
    if glasses >= WATER_TARGET:
        return "PASS"
    elif glasses >= WATER_TARGET / 2:
        return "NEAR"
    return "FAIL"


def get_sleep_status(hours):
    if hours >= SLEEP_TARGET:
        return "PASS"
    elif hours >= 6:
        return "NEAR"
    return "FAIL"


def get_exercise_status(minutes):
    if minutes >= EXERCISE_TARGET:
        return "PASS"
    elif minutes >= 15:
        return "NEAR"
    return "FAIL"


def get_mood_status(rating):
    if rating >= MOOD_TARGET:
        return "PASS"
    elif rating >= 5:
        return "NEAR"
    return "FAIL"