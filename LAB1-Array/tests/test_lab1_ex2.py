import os
import sys
import unittest

HERE = os.path.dirname(__file__)
SRC = os.path.abspath(os.path.join(HERE, "..", "src"))
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from lab1_ex2 import analyze_scores, CinemaSeating


class TestAnalyzeScores(unittest.TestCase):
    def test_basic(self):
        scores = [
            [80, 70, 90],
            [60, 65, 55],
            [90, 95, 85],
            [40, 45, 30],
        ]
        out = analyze_scores(scores)
        # subject averages
        self.assertEqual(len(out["subject_averages"]), 3)
        self.assertAlmostEqual(out["subject_averages"][0], (80+60+90+40)/4)
        # top student index -> student 2 (0-based index)
        self.assertEqual(out["top_student_index"], 2)
        # pass counts (>=50)
        self.assertEqual(out["pass_counts"], [3, 3, 3])

    def test_empty(self):
        out = analyze_scores([])
        self.assertEqual(out["subject_averages"], [])
        self.assertEqual(out["top_student_index"], -1)
        self.assertEqual(out["pass_counts"], [])

    def test_uneven_rows(self):
        # second row missing last subject -> treated as 0
        scores = [ [50, 60, 70], [80, 90] ]
        out = analyze_scores(scores)
        self.assertEqual(len(out["subject_averages"]), 3)
        # pass counts: subject 3 has only one student with 70
        self.assertEqual(out["pass_counts"][2], 1)


class TestCinemaSeating(unittest.TestCase):
    def test_booking_and_cancel(self):
        c = CinemaSeating(2, 3)
        self.assertTrue(c.book(0, 0))
        self.assertFalse(c.book(0, 0))  # already booked
        self.assertTrue(c.is_booked(0, 0))
        self.assertEqual(c.available_count(), 5)
        self.assertTrue(c.cancel(0, 0))
        self.assertFalse(c.is_booked(0, 0))
        self.assertEqual(c.available_count(), 6)
        self.assertFalse(c.cancel(0, 0))  # already free
        # invalid coords
        self.assertFalse(c.book(-1, 0))
        self.assertFalse(c.cancel(10, 10))


if __name__ == '__main__':
    unittest.main()
