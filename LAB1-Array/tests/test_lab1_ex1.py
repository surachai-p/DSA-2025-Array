import os
import sys
import unittest

# Ensure the src/ folder is importable from tests (handles the hyphen in LAB1-Array)
HERE = os.path.dirname(__file__)
SRC = os.path.abspath(os.path.join(HERE, "..", "src"))
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from lab1_ex1 import student_stats, Inventory


class TestStudentStats(unittest.TestCase):
    def test_basic_stats(self):
        scores = [60, 70, 80, 90, 100]
        result = student_stats(scores)
        self.assertAlmostEqual(result["average"], 80.0)
        self.assertEqual(result["max"], 100)
        self.assertEqual(result["min"], 60)
        # numbers strictly above average (80) are 90 and 100
        self.assertEqual(result["count_above_avg"], 2)

    def test_all_equal(self):
        scores = [50, 50, 50, 50, 50]
        result = student_stats(scores)
        self.assertAlmostEqual(result["average"], 50.0)
        self.assertEqual(result["count_above_avg"], 0)

    def test_empty(self):
        result = student_stats([])
        self.assertEqual(result["average"], 0.0)
        self.assertIsNone(result["max"])
        self.assertIsNone(result["min"])
        self.assertEqual(result["count_above_avg"], 0)


class TestInventory(unittest.TestCase):
    def test_add_find_remove_list(self):
        inv = Inventory()
        inv.add("apple")
        inv.add("banana")
        inv.add("orange")
        self.assertEqual(inv.find("apple"), 0)
        self.assertEqual(inv.find("orange"), 2)
        self.assertEqual(inv.find("missing"), -1)

        self.assertTrue(inv.remove("banana"))
        self.assertEqual(inv.list_all(), ["apple", "orange"])

        self.assertFalse(inv.remove("banana"))


if __name__ == "__main__":
    unittest.main()
