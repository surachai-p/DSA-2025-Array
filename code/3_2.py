import random

scores = [[[random.randint(0, 100) for _ in range(4)] for _ in range(5)] for _ in range(3)]

for layer in scores:
    for row in layer:
        print(row)
    print()

room_averages = [sum(sum(student) for student in room) / (5 * 4) for room in scores]
print(f"ค่าเฉลี่ยคะแนนแต่ละห้อง{room_averages}")

highest_avg_room = room_averages.index(max(room_averages)) + 1
print("ห้องที่มีคะแนนเฉลี่ยสูงสุดคือห้องที่", highest_avg_room, "ค่าเฉลี่ย:", max(room_averages))

for room_index, room in enumerate(scores):
    total_scores = [sum(student) for student in room]
    top_student = total_scores.index(max(total_scores)) + 1
    print(f"\nห้องที่ {room_index+1}:\nนักเรียนที่ได้คะแนนรวมสูงสุดคือคนที่ {top_student}, คะแนนรวม: {max(total_scores)}")

    pass_count = sum(all(score >= 50 for score in student) for student in room)
    print(f"จำนวนนักเรียนที่สอบผ่านทุกวิชา:", pass_count)