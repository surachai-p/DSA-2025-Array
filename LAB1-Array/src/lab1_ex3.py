"""
3D array exercises for LAB1.

Functions provided:
- analyze_temperatures(temps): temps[city][day][time] => returns average per city and max (day,time,value) per city
- analyze_classrooms(classrooms): classrooms[room][student][subject] => returns room averages, best room index,
  top student per room, and count of students passing all subjects per room

Includes demo in __main__.
"""
from typing import List, Dict, Any, Tuple


def analyze_temperatures(temps: List[List[List[float]]]) -> Dict[str, Any]:
    """Analyze temperature data for multiple cities.

    Args:
      temps: list of cities; each city is list of days; each day is list of measurements per time
             shape: C x D x T (cities x days x times_per_day)

    Returns:
      {
        "avg_per_city": List[float],
        "max_info_per_city": List[Tuple[int, int, float]]  # (day_index, time_index, value)
      }
    """
    if not temps:
        return {"avg_per_city": [], "max_info_per_city": []}

    avg_per_city: List[float] = []
    max_info_per_city: List[Tuple[int, int, float]] = []

    for city in temps:
        if not city:
            avg_per_city.append(0.0)
            max_info_per_city.append((-1, -1, float("-inf")))
            continue
        total = 0.0
        count = 0
        max_val = float("-inf")
        max_day = -1
        max_time = -1
        for d_idx, day in enumerate(city):
            for t_idx, val in enumerate(day):
                total += val
                count += 1
                if val > max_val:
                    max_val = val
                    max_day = d_idx
                    max_time = t_idx
        avg_per_city.append(total / count if count else 0.0)
        max_info_per_city.append((max_day, max_time, max_val))

    return {"avg_per_city": avg_per_city, "max_info_per_city": max_info_per_city}


def analyze_classrooms(classrooms: List[List[List[float]]]) -> Dict[str, Any]:
    """Analyze multiple classrooms' scores.

    Args:
      classrooms: list of rooms; each room is list of students; each student is list of subject scores

    Returns dict with:
      - room_averages: List[float]
      - best_room_index: int index of room with highest average (ties -> first)
      - top_student_per_room: List[int] index of student with highest total per room
      - pass_all_counts: List[int] number of students in room who passed all subjects (>=50)
    """
    if not classrooms:
        return {"room_averages": [], "best_room_index": -1, "top_student_per_room": [], "pass_all_counts": []}

    room_averages: List[float] = []
    top_student_per_room: List[int] = []
    pass_all_counts: List[int] = []

    for room in classrooms:
        if not room:
            room_averages.append(0.0)
            top_student_per_room.append(-1)
            pass_all_counts.append(0)
            continue
        total_room = 0.0
        count_scores = 0
        student_totals: List[float] = []
        pass_all = 0
        for student in room:
            if not student:
                student_totals.append(0.0)
                continue
            s_total = sum(student)
            student_totals.append(s_total)
            total_room += s_total
            count_scores += len(student)
            # passed all subjects?
            if all(score >= 50 for score in student):
                pass_all += 1
        room_avg = total_room / count_scores if count_scores else 0.0
        room_averages.append(room_avg)
        # top student index (first occurrence of max)
        top_idx = max(range(len(student_totals)), key=lambda i: student_totals[i]) if student_totals else -1
        top_student_per_room.append(top_idx)
        pass_all_counts.append(pass_all)

    best_room_index = max(range(len(room_averages)), key=lambda i: room_averages[i]) if room_averages else -1

    return {
        "room_averages": room_averages,
        "best_room_index": best_room_index,
        "top_student_per_room": top_student_per_room,
        "pass_all_counts": pass_all_counts,
    }


if __name__ == "__main__":
    # Demo: temperatures for 3 cities, 7 days, 4 times per day (use small sample values)
    city0 = [[20 + d + t for t in range(4)] for d in range(7)]
    city1 = [[25 + d + t * 0.5 for t in range(4)] for d in range(7)]
    city2 = [[15 + d * 0.2 + t for t in range(4)] for d in range(7)]
    temps = [city0, city1, city2]
    out = analyze_temperatures(temps)
    print("Avg per city:", out["avg_per_city"])
    print("Max info per city:", out["max_info_per_city"])

    # Demo: classrooms: 3 rooms, each with students and 4 subjects
    rooms = [
        [[60, 70, 80, 90], [50, 50, 50, 50], [30, 40, 20, 10], [100, 90, 80, 70], [55, 65, 75, 85]],
        [[40, 45, 50, 55], [60, 60, 60, 60], [70, 80, 90, 100], [50, 49, 51, 52], [30, 30, 30, 30]],
        [[90, 90, 90, 90], [85, 85, 85, 85], [40, 60, 80, 100], [60, 60, 60, 60], [49, 51, 52, 53]],
    ]
    info = analyze_classrooms(rooms)
    print("Room averages:", info["room_averages"])
    print("Best room index:", info["best_room_index"])
    print("Top student per room:", info["top_student_per_room"])
    print("Pass-all counts per room:", info["pass_all_counts"])
