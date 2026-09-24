"""
VitaTrack - Habit & Wellness Tracker
Python Semester-Long Individual Application Project
Stages 1-3 Submission (Single File)

Stage 1: Python Fundamentals - variables, data types, expressions, basic operators
Stage 2: Input and Output - input(), type conversion, formatted output
Stage 3: Conditional Statements - if/elif/else, comparison and logical operators

Note: Error handling and input validation will be added in Stage 8.
"""

WATER_TARGET = 8          # glasses per day
SLEEP_TARGET = 8.0        # hours per day
EXERCISE_TARGET = 30      # minutes per day
MOOD_TARGET = 7           # minimum mood rating (out of 10)


def main():

    
    print("      Welcome to VitaTrack Wellness Tracker")
    
    
    user_name = input("Enter your name: ")
    print(f"\nHello, {user_name}! Let's log your day.\n")

    water_glasses = int(input("How many glasses of water did you drink? "))
    sleep_hours = float(input("How many hours did you sleep? "))
    exercise_minutes = int(input("How many minutes did you exercise? "))
    mood_rating = int(input("Rate your mood today (1-10): "))

    
    water_score = min((water_glasses / WATER_TARGET) * 100, 100)
    sleep_score = min((sleep_hours / SLEEP_TARGET) * 100, 100)
    exercise_score = min((exercise_minutes / EXERCISE_TARGET) * 100, 100)
    mood_score = (mood_rating / 10) * 100
    overall_score = (water_score + sleep_score + exercise_score + mood_score) / 4


   
    print("              GOAL CHECK RESULTS")
    

    
    if water_glasses >= WATER_TARGET:
        print(f"[PASS] Water: You drank {water_glasses} glasses. Excellent hydration!")
    elif water_glasses >= WATER_TARGET / 2:
        print(f"[NEAR] Water: You drank {water_glasses} glasses. Try to reach {WATER_TARGET}.")
    else:
        print(f"[FAIL] Water: Only {water_glasses} glasses. Drink more water!")

    
    if sleep_hours >= SLEEP_TARGET:
        print(f"[PASS] Sleep: {sleep_hours} hours. Great rest!")
    elif sleep_hours >= 6:
        print(f"[NEAR] Sleep: {sleep_hours} hours. Slightly below target.")
    else:
        print(f"[FAIL] Sleep: Only {sleep_hours} hours. You need more rest!")

    
    if exercise_minutes >= EXERCISE_TARGET:
        print(f"[PASS] Exercise: {exercise_minutes} minutes. Well done!")
    elif exercise_minutes >= 15:
        print(f"[NEAR] Exercise: {exercise_minutes} minutes. Try for {EXERCISE_TARGET}.")
    else:
        print(f"[FAIL] Exercise: Only {exercise_minutes} minutes. Get moving!")

    
    if mood_rating >= MOOD_TARGET and sleep_hours >= 7:
        print(f"[PASS] Mood: {mood_rating}/10 and well-rested. Keep it up!")
    elif mood_rating >= MOOD_TARGET or exercise_minutes >= EXERCISE_TARGET:
        print(f"[NEAR] Mood: {mood_rating}/10. Some positive factors present.")
    else:
        print(f"[FAIL] Mood: {mood_rating}/10. Consider rest and activity.")


    
    print(f"       OVERALL WELLNESS SCORE: {overall_score:.1f}/100")
   

    if overall_score >= 85:
        rating = "EXCELLENT"
        advice = "Outstanding! You are thriving. Keep this routine!"
    elif overall_score >= 70:
        rating = "GOOD"
        advice = "Great job! Small improvements will make it excellent."
    elif overall_score >= 50:
        rating = "FAIR"
        advice = "You're on the right track. Focus on weaker areas."
    elif overall_score >= 30:
        rating = "NEEDS IMPROVEMENT"
        advice = "Try to build consistency. Start with one habit."
    else:
        rating = "POOR"
        advice = "Your wellness needs attention. Begin with small, daily steps."

    print(f"Rating : {rating}")
    print(f"Advice : {advice}")
    
    print(f"\nThank you for tracking with VitaTrack, {user_name}!")


if __name__ == "__main__":
    main()

