WATER_TARGET = 8         
SLEEP_TARGET = 8.0        
EXERCISE_TARGET = 30      
MOOD_TARGET = 7    

def calculate_water_score(glasses):
    return (min((glasses / WATER_TARGET) * 100, 100))

def calculate_sleep_score(hours):
    return (min((hours / SLEEP_TARGET) * 100, 100))

def calculate_exercise_score(minutes):
    return (min((minutes / EXERCISE_TARGET) * 100, 100))

def calculate_mood_score(rating):
    return (min((rating / MOOD_TARGET) * 100, 100))

def calculate_overall_score(water_score, sleep_score, exercise_score, mood_score):
    return (
        calculate_water_score(water_score)
        + calculate_sleep_score(sleep_score)
        + calculate_exercise_score(exercise_score) 
        + calculate_mood_score(mood_score)) / 4

def get_rating(score):
    if score >= 85:
        return "Outstanding! You are thriving. Keep this routine!"
    elif score >= 70:
        return "Great job! Small improvements will make it excellent"
    elif score >= 50:
        return "You're on the right track. Focus on weaker areas."
    elif score >= 30:
        return "Try to build consistency. Start with one habit."
    else:
        return "Your wellness needs attention. Begin with small, daily steps"

def get_water_status(glasses):
    if glasses >= WATER_TARGET:
        return f"[PASS] Water: You drank {glasses} glasses. Excellent hydration!"
    elif WATER_TARGET / 2 <= glasses < WATER_TARGET:
        return f"[NEAR] Water: You drank {glasses} glasses. Try to reach {WATER_TARGET}."
    else:
        return f"[FAIL] Water: Only {glasses} glasses. Drink more water!"

def get_sleep_status(hours):
    if hours >= SLEEP_TARGET:
        return f"[PASS] Sleep: {hours} hours. Great rest!"
    elif SLEEP_TARGET / 2 <= hours < SLEEP_TARGET:
        return f"[NEAR] Sleep: {hours} hours. Slightly below target."
    else:
        return f"[FAIL] Sleep: Only {hours} hours. You need more rest!"

def get_exercise_status(minutes):
    if minutes >= EXERCISE_TARGET:
        return f"[PASS] Exercise: {minutes} minutes. Great job!"
    elif EXERCISE_TARGET / 2 <= minutes < EXERCISE_TARGET:
        return f"[NEAR] Exercise: {minutes} minutes. Try to reach {EXERCISE_TARGET}."
    else:
        return f"[FAIL] Exercise: Only {minutes} minutes. You need more activity!"

def get_mood_status(rating):
    if rating >= MOOD_TARGET:
        return f"[PASS] Mood: {rating} out of {MOOD_TARGET}. Excellent mood!"
    elif MOOD_TARGET / 2 <= rating < MOOD_TARGET:
        return f"[NEAR] Mood: {rating} out of {MOOD_TARGET}. Try to improve."
    else:
        return f"[FAIL] Mood: Only {rating} out of {MOOD_TARGET}. Focus on your mental health." 