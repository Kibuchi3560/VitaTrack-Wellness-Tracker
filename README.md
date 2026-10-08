# VitaTrack – Habit & Wellness Tracker

A Python command-line application for logging and analysing daily wellness habits.
Built as the **Python Programming Semester-Long Individual Application Project**.

## Problem Statement
Many people struggle to maintain consistent daily wellness habits. Existing apps
are often complex or require internet connectivity. VitaTrack provides a simple,
offline, command-line tool for tracking water intake, sleep, exercise, and mood,
calculating a wellness score, and providing personalised feedback.

## Target Users
University students and young professionals who want a lightweight, offline
wellness tracker without needing a smartphone or internet connection.

## Features
1. **Log Daily Wellness** – record water, sleep, exercise, and mood.
2. **View All Records** – tabular view of every logged day.
3. **View Report for a Date** – detailed report card with scores and advice.
4. **View Statistics** – averages, best day, worst day.
5. **Delete a Record** – with confirmation prompt.
6. **Export Summary Report** – writes a text summary to `data/summary_report.txt`.
7. **Persistent Storage** – records saved to `data/wellness_log.txt`.

## Project Structure
VitaTrack_Project/
├── main.py
├── modules/
│ ├── init.py
│ ├── calculations.py
│ ├── records.py
│ ├── reports.py
│ ├── storage.py
│ └── validation.py
├── data/
│ └── wellness_log.txt
├── test/
│ └── test_vitatrack.py
└── README.md