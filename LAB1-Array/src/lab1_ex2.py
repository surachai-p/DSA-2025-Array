"""
2D array exercises for LAB1.
- analyze_scores(scores_matrix): scores_matrix is a list of rows, each row represents a student and contains scores for N subjects.
  Returns subject averages, index of student with highest total, and pass counts per subject (pass >= 50).

- CinemaSeating class: simple seat map manager with booking/cancel/check and count of available seats.

Demo in __main__.
"""
from typing import List, Dict, Any, Tuple


def analyze_scores(scores: List[List[float]]) -> Dict[str, Any]:
    """Analyze a 2D scores matrix.

    Args:
      scores: list of students, each student is a list of subject scores (length M)

    Returns dict with:
      - subject_averages: List[float] length M
      - top_student_index: int index (0-based) of student with highest total (ties: first)
      - pass_counts: List[int] per subject (score >= 50)
    """
    if not scores:
        return {"subject_averages": [], "top_student_index": -1, "pass_counts": []}

    num_students = len(scores)
    num_subjects = max(len(row) for row in scores)

    # Normalize rows: if some rows shorter, treat missing scores as 0
    norm = [row + [0] * (num_subjects - len(row)) for row in scores]

    subject_sums = [0.0] * num_subjects
    pass_counts = [0] * num_subjects
    totals = []

    for row in norm:
        totals.append(sum(row))
        for i, val in enumerate(row):
            subject_sums[i] += val
            if val >= 50:
                pass_counts[i] += 1

    subject_averages = [subject_sums[i] / num_students for i in range(num_subjects)]
    top_student_index = max(range(num_students), key=lambda i: totals[i])

    return {
        "subject_averages": subject_averages,
        "top_student_index": top_student_index,
        "pass_counts": pass_counts,
    }


class CinemaSeating:
    """Simple seating grid manager.

    Seats are represented as boolean: False = available, True = booked.
    Rows are 0..R-1 and cols 0..C-1.
    """

    def __init__(self, rows: int, cols: int):
        if rows <= 0 or cols <= 0:
            raise ValueError("rows and cols must be positive")
        self.rows = rows
        self.cols = cols
        self._seats = [[False for _ in range(cols)] for _ in range(rows)]

    def book(self, r: int, c: int) -> bool:
        """Book seat (r,c). Return True if booked, False if already booked or invalid."""
        if not self._valid(r, c):
            return False
        if self._seats[r][c]:
            return False
        self._seats[r][c] = True
        return True

    def cancel(self, r: int, c: int) -> bool:
        """Cancel booking. Return True if canceled, False if seat was free or invalid."""
        if not self._valid(r, c):
            return False
        if not self._seats[r][c]:
            return False
        self._seats[r][c] = False
        return True

    def is_booked(self, r: int, c: int) -> bool:
        if not self._valid(r, c):
            return False
        return self._seats[r][c]

    def available_count(self) -> int:
        return sum(1 for r in range(self.rows) for c in range(self.cols) if not self._seats[r][c])

    def _valid(self, r: int, c: int) -> bool:
        return 0 <= r < self.rows and 0 <= c < self.cols

    def __str__(self) -> str:
        lines = []
        for row in self._seats:
            lines.append("".join("X" if x else "O" for x in row))
        return "\n".join(lines)


if __name__ == "__main__":
    # Demo for scores
    scores = [
        [80, 70, 90],
        [60, 65, 55],
        [90, 95, 85],
        [40, 45, 30],
    ]
    out = analyze_scores(scores)
    print("Subject averages:", out["subject_averages"])
    print("Top student index:", out["top_student_index"])
    print("Pass counts per subject:", out["pass_counts"])

    # Demo for cinema
    cinema = CinemaSeating(3, 4)
    cinema.book(0, 0)
    cinema.book(1, 2)
    print("Cinema map:\n", cinema)
    print("Available seats:", cinema.available_count())
