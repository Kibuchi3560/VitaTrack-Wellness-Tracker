"""
reports.py
Report generation and statistics.

Stage 5 - Functions
Stage 6 - Data Structures
Stage 7 - File Handling (export)
"""

from modules.calculations import (
    WATER_TARGET, SLEEP_TARGET, EXERCISE_TARGET, MOOD_TARGET,
    calculate_water_score, calculate_sleep_score,
    calculate_exercise_score, calculate_mood_score,
    calculate_overall_score, get_rating, get_advice,
    get_water_status, get_sleep_status,
    get_exercise_status, get_mood_status,
)


def display_daily_report(record):
    """Print a detailed wellness report for one record."""
    date = record["date"]
    water, sleep = record["water"], record["sleep"]
    exercise, mood = record["exercise"], record["mood"]

    water_score = calculate_water_score(water)
    sleep_score = calculate_sleep_score(sleep)
    exercise_score = calculate_exercise_score(exercise)
    mood_score = calculate_mood_score(mood)
    overall = calculate_overall_score(water, sleep, exercise, mood)

    print("\n" + "=" * 60)
    print(f"          Wellness Report for {date}")
    print("=" * 60)
    print(f"{'Metric':<14}{'Value':<18}{'Score':<10}{'Status':<8}")
    print("-" * 60)
    print(f"{'Water':<14}{str(water) + ' glasses':<18}{water_score:>6.1f}%   {get_water_status(water):<8}")
    print(f"{'Sleep':<14}{str(sleep) + ' hours':<18}{sleep_score:>6.1f}%   {get_sleep_status(sleep):<8}")
    print(f"{'Exercise':<14}{str(exercise) + ' min':<18}{exercise_score:>6.1f}%   {get_exercise_status(exercise):<8}")
    print(f"{'Mood':<14}{str(mood) + '/10':<18}{mood_score:>6.1f}%   {get_mood_status(mood):<8}")
    print("-" * 60)
    print(f"OVERALL SCORE : {overall:.1f}/100")
    print(f"RATING        : {get_rating(overall)}")
    print(f"ADVICE        : {get_advice(overall)}")
    print("=" * 60)


def display_statistics(records):
    """Show averages, best day, worst day, and total logs."""
    if not records:
        print("\n  No records to analyse.")
        return

    n = len(records)
    avg_water = sum(r["water"] for r in records) / n
    avg_sleep = sum(r["sleep"] for r in records) / n
    avg_exercise = sum(r["exercise"] for r in records) / n
    avg_mood = sum(r["mood"] for r in records) / n

    scored = [
        (r["date"], calculate_overall_score(r["water"], r["sleep"], r["exercise"], r["mood"]))
        for r in records
    ]
    avg_score = sum(s for _, s in scored) / n
    best_date, best_score = max(scored, key=lambda x: x[1])
    worst_date, worst_score = min(scored, key=lambda x: x[1])

    print("\n" + "=" * 60)
    print("                VitaTrack Statistics")
    print("=" * 60)
    print(f"Total records logged : {n}")
    print("-" * 60)
    print(f"Average Water        : {avg_water:.1f} glasses (target {WATER_TARGET})")
    print(f"Average Sleep        : {avg_sleep:.1f} hours   (target {SLEEP_TARGET})")
    print(f"Average Exercise     : {avg_exercise:.1f} min     (target {EXERCISE_TARGET})")
    print(f"Average Mood         : {avg_mood:.1f}/10       (target {MOOD_TARGET}+)")
    print(f"Average Wellness     : {avg_score:.1f}/100")
    print("-" * 60)
    print(f"Best day  : {best_date}  ({best_score:.1f}/100)")
    print(f"Worst day : {worst_date} ({worst_score:.1f}/100)")
    print("=" * 60)


def export_summary_report(records):
    """Write a plain-text summary report to data/summary_report.txt."""
    if not records:
        print("\n  No records to export.")
        return

    n = len(records)
    avg_score = sum(
        calculate_overall_score(r["water"], r["sleep"], r["exercise"], r["mood"])
        for r in records
    ) / n

    lines = []
    lines.append("=" * 60)
    lines.append("           VitaTrack - Wellness Summary Report")
    lines.append("=" * 60)
    lines.append(f"Total records : {n}")
    lines.append(f"Average score : {avg_score:.1f}/100")
    lines.append(f"Rating        : {get_rating(avg_score)}")
    lines.append("-" * 60)
    lines.append(f"{'Date':<14}{'Water':<10}{'Sleep':<10}{'Exercise':<12}{'Mood':<8}{'Score':<8}")
    lines.append("-" * 60)
    for r in sorted(records, key=lambda x: x["date"]):
        score = calculate_overall_score(r["water"], r["sleep"], r["exercise"], r["mood"])
        lines.append(
            f"{r['date']:<14}{r['water']:<10}{r['sleep']:<10}{r['exercise']:<12}{r['mood']:<8}{score:.1f}"
        )
    lines.append("=" * 60)

    try:
        with open("data/summary_report.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print("\n  [OK] Summary report exported to data/summary_report.txt")
    except OSError as e:
        print(f"  [!] Could not export report: {e}")