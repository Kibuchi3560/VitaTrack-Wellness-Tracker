"""
test_vitatrack.py
Unit tests for VitaTrack calculation and status functions.

Stage 10 - Testing and Refinement
Run with: python -m unittest discover test
"""

import os
import sys
import unittest

# Make project root importable when running tests from /test
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.calculations import (
    WATER_TARGET, SLEEP_TARGET, EXERCISE_TARGET, MOOD_TARGET,
    calculate_water_score, calculate_sleep_score,
    calculate_exercise_score, calculate_mood_score,
    calculate_overall_score, get_rating, get_advice,
    get_water_status, get_sleep_status,
    get_exercise_status, get_mood_status,
)


class TestScores(unittest.TestCase):

    # --- Normal ---
    def test_water_normal(self):
        self.assertEqual(calculate_water_score(4), 50.0)

    def test_sleep_normal(self):
        self.assertEqual(calculate_sleep_score(4.0), 50.0)

    def test_exercise_normal(self):
        self.assertEqual(calculate_exercise_score(15), 50.0)

    def test_mood_normal(self):
        self.assertEqual(calculate_mood_score(5), 50.0)

    # --- Boundary ---
    def test_water_exact_target(self):
        self.assertEqual(calculate_water_score(WATER_TARGET), 100.0)

    def test_water_above_target_capped(self):
        self.assertEqual(calculate_water_score(WATER_TARGET + 10), 100.0)

    def test_water_zero(self):
        self.assertEqual(calculate_water_score(0), 0.0)

    def test_sleep_zero(self):
        self.assertEqual(calculate_sleep_score(0), 0.0)

    def test_mood_max(self):
        self.assertEqual(calculate_mood_score(10), 100.0)

    def test_mood_min(self):
        self.assertEqual(calculate_mood_score(0), 0.0)

    # --- Overall ---
    def test_overall_all_targets(self):
        self.assertEqual(
            calculate_overall_score(WATER_TARGET, SLEEP_TARGET, EXERCISE_TARGET, 10),
            100.0,
        )

    def test_overall_zero(self):
        self.assertEqual(calculate_overall_score(0, 0, 0, 0), 0.0)

    def test_overall_mixed(self):
        result = calculate_overall_score(4, 4.0, 15, 5)
        self.assertEqual(result, 50.0)


class TestRatings(unittest.TestCase):

    def test_rating_excellent(self):
        self.assertEqual(get_rating(90), "EXCELLENT")

    def test_rating_good(self):
        self.assertEqual(get_rating(75), "GOOD")

    def test_rating_fair(self):
        self.assertEqual(get_rating(55), "FAIR")

    def test_rating_needs_improvement(self):
        self.assertEqual(get_rating(40), "NEEDS IMPROVEMENT")

    def test_rating_poor(self):
        self.assertEqual(get_rating(10), "POOR")

    def test_rating_boundary_85(self):
        self.assertEqual(get_rating(85), "EXCELLENT")

    def test_rating_boundary_70(self):
        self.assertEqual(get_rating(70), "GOOD")

    def test_rating_boundary_50(self):
        self.assertEqual(get_rating(50), "FAIR")

    def test_rating_boundary_30(self):
        self.assertEqual(get_rating(30), "NEEDS IMPROVEMENT")


class TestStatuses(unittest.TestCase):

    def test_water_pass(self):
        self.assertEqual(get_water_status(WATER_TARGET), "PASS")

    def test_water_near(self):
        self.assertEqual(get_water_status(WATER_TARGET // 2), "NEAR")

    def test_water_fail(self):
        self.assertEqual(get_water_status(1), "FAIL")

    def test_sleep_pass(self):
        self.assertEqual(get_sleep_status(8.0), "PASS")

    def test_sleep_near(self):
        self.assertEqual(get_sleep_status(6.5), "NEAR")

    def test_sleep_fail(self):
        self.assertEqual(get_sleep_status(4.0), "FAIL")

    def test_exercise_pass(self):
        self.assertEqual(get_exercise_status(30), "PASS")

    def test_exercise_near(self):
        self.assertEqual(get_exercise_status(20), "NEAR")

    def test_exercise_fail(self):
        self.assertEqual(get_exercise_status(5), "FAIL")

    def test_mood_pass(self):
        self.assertEqual(get_mood_status(8), "PASS")

    def test_mood_near(self):
        self.assertEqual(get_mood_status(5), "NEAR")

    def test_mood_fail(self):
        self.assertEqual(get_mood_status(2), "FAIL")


if __name__ == "__main__":
    unittest.main(verbosity=2)