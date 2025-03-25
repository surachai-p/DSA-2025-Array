
scores = [[[80, 75, 90, 85], [85, 70, 80, 95], [78, 82, 88, 92], [90, 85, 78, 80], [88, 91, 95, 87]],  # ห้อง 1
          [[70, 75, 80, 85], [68, 70, 75, 80], [85, 80, 88, 90], [90, 85, 88, 92], [60, 65, 70, 72]],  # ห้อง 2
          [[88, 85, 92, 80], [85, 80, 95, 87], [78, 82, 80, 85], [85, 87, 90, 92], [90, 88, 93, 89]]]  # ห้อง 3


average_scores = [sum(sum(student) for student in room) / (5 * 4) for room in scores]
max_avg_room = average_scores.index(max(average_scores)) + 1
print(f"ห้องที่มีคะแนนเฉลี่ยสูงสุด: ห้อง {max_avg_room}")


for i, room in enumerate(scores):
    total_scores = [sum(student) for student in room]
    highest_student = total_scores.index(max(total_scores)) + 1
    print(f"ห้อง {i+1}: นักเรียนที่ได้คะแนนรวมสูงสุด: นักเรียนคนที่ {highest_student}")


for i, room in enumerate(scores):
    passed_students = sum(1 for student in room if all(subject >= 50 for subject in student))
    print(f"ห้อง {i+1}: จำนวนที่สอบผ่านทุกวิชา: {passed_students} คน")
