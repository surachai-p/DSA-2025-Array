
import random

scores = [
    [[random.randint(30, 100) for _ in range(4)] for _ in range(5)] for _ in range(3)
]

average_room_scores = [sum(sum(student) for student in room) / (5 * 4) for room in scores]
highest_avg_room_idx = average_room_scores.index(max(average_room_scores)) + 1

top_students = []
for room in scores:
    total_scores = [sum(student) for student in room]
    max_score = max(total_scores)
    top_students.append(total_scores.index(max_score) + 1)

students_passing_all = [
    sum(1 for student in room if all(subject >= 50 for subject in student)) for room in scores
]

print(f"ห้องที่มีคะแนนเฉลี่ยสูงสุด: ห้อง {highest_avg_room_idx}")
for room_idx, (top_student, passing_count) in enumerate(zip(top_students, students_passing_all), 1):
    print(f"ห้อง {room_idx}:")
    print(f"  นักเรียนที่ได้คะแนนรวมสูงสุด: นักเรียน {top_student}")
    print(f"  จำนวนนักเรียนที่สอบผ่านทุกวิชา: {passing_count}")
