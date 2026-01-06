"""
Simple implementations for LAB1 exercises (1D arrays) in Python.
Provides:
- student_stats(scores): average, max, min, count above average
- Inventory class: add, remove, find, list_all

This file also contains a small demo when executed as __main__.
"""
from typing import List, Dict, Any


def student_stats(scores: List[float]) -> Dict[str, Any]:
    """Return statistics for a list of numeric scores.

    Result keys:
      - average: float (0.0 if empty)
      - max: highest score or None if empty
      - min: lowest score or None if empty
      - count_above_avg: number of scores strictly greater than average
    """
    if not scores:
        return {"average": 0.0, "max": None, "min": None, "count_above_avg": 0}

    avg = sum(scores) / len(scores)
    return {
        "average": avg,
        "max": max(scores),
        "min": min(scores),
        "count_above_avg": sum(1 for s in scores if s > avg),
    }


class Inventory:
    """A tiny inventory manager backed by a Python list.

    Methods:
      - add(item): append a new item
      - remove(item): remove first occurrence, return True if removed else False
      - find(item): return index of first occurrence or -1
      - list_all(): return a shallow copy of the items list
    """

    def __init__(self, items: List[str] = None):
        self._items: List[str] = list(items) if items else []

    def add(self, item: str) -> None:
        self._items.append(item)

    def remove(self, item: str) -> bool:
        try:
            self._items.remove(item)
            return True
        except ValueError:
            return False

    def find(self, item: str) -> int:
        try:
            return self._items.index(item)
        except ValueError:
            return -1

    def list_all(self) -> List[str]:
        return list(self._items)


if __name__ == "__main__":
    # demo for quick manual run
    scores = [65, 70, 80, 90, 100]
    stats = student_stats(scores)
    print(f"Scores: {scores}")
    print(f"Average: {stats['average']:.2f}, Max: {stats['max']}, Min: {stats['min']}, Above avg: {stats['count_above_avg']}")

    inv = Inventory()
    inv.add("apple")
    inv.add("banana")
    inv.add("orange")
    print("Inventory:", inv.list_all())
    inv.remove("banana")
    print("After remove banana:", inv.list_all())
