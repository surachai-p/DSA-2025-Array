import os
import sys
import unittest

HERE = os.path.dirname(__file__)
SRC = os.path.abspath(os.path.join(HERE, "..", "src"))
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from lab1_ex3 import analyze_temperatures, analyze_classrooms


class TestAnalyzeTemperatures(unittest.TestCase):
    def test_basic(self):
        # 2 cities, 2 days, 2 times per day
        city0 = [[10, 20], [30, 40]]  # avg = 25, max = 40 at (1,1)
        city1 = [[5, 5], [5, 5]]      # avg = 5, max = 5 at (0,0)
        temps = [city0, city1]
        out = analyze_temperatures(temps)
        self.assertEqual(len(out["avg_per_city"]), 2)
        self.assertAlmostEqual(out["avg_per_city"][0], 25.0)
        self.assertEqual(out["max_info_per_city"][0], (1, 1, 40))
        self.assertEqual(out["max_info_per_city"][1], (0, 0, 5))

    def test_empty(self):
        out = analyze_temperatures([])
        self.assertEqual(out["avg_per_city"], [])
        self.assertEqual(out["max_info_per_city"], [])


class TestAnalyzeClassrooms(unittest.TestCase):
    def test_basic(self):
        # 2 rooms, each room has 2 students, each student has 3 subjects
        rooms = [
            [[60, 70, 80], [50, 50, 50]],
            [[30, 40, 50], [100, 100, 100]],
        ]
        out = analyze_classrooms(rooms)
        # room averages: room0 avg = (60+70+80+50+50+50)/6 = 60, room1 avg = (30+40+50+100+100+100)/6 = 70
        self.assertAlmostEqual(out["room_averages"][0], 60.0)
        self.assertAlmostEqual(out["room_averages"][1], 70.0)
        self.assertEqual(out["best_room_index"], 1)
        # top student per room -> room0 student0 (210) vs student1 (150)
        self.assertEqual(out["top_student_per_room"][0], 0)
        # pass-all counts (>=50): room0 -> student0 yes, student1 yes -> 2; room1 -> only student1 has all >=50 (100s) -> 1
        self.assertEqual(out["pass_all_counts"][0], 2)
        self.assertEqual(out["pass_all_counts"][1], 1)

    def test_empty(self):
        out = analyze_classrooms([])
        self.assertEqual(out["room_averages"], [])
        self.assertEqual(out["best_room_index"], -1)
        self.assertEqual(out["top_student_per_room"], [])
        self.assertEqual(out["pass_all_counts"], [])


if __name__ == '__main__':
    unittest.main()
