# ข้อมูลคะแนนของนักเรียนในแต่ละห้อง (ห้องละ 5 คน, สอบ 4 วิชา)
scores = {
    "ห้อง1": [
        [80, 75, 90, 85],  # นักเรียน 1
        [70, 60, 65, 75],  # นักเรียน 2
        [85, 90, 95, 80],  # นักเรียน 3
        [60, 55, 70, 65],  # นักเรียน 4
        [78, 82, 85, 80]   # นักเรียน 5
    ],
    "ห้อง2": [
        [90, 85, 88, 92],  # นักเรียน 1
        [75, 80, 70, 68],  # นักเรียน 2
        [88, 85, 92, 90],  # นักเรียน 3
        [65, 60, 55, 58],  # นักเรียน 4
        [92, 89, 95, 90]   # นักเรียน 5
    ],
    "ห้อง3": [
        [70, 80, 85, 90],  # นักเรียน 1
        [60, 58, 65, 70],  # นักเรียน 2
        [85, 90, 92, 88],  # นักเรียน 3
        [75, 77, 80, 82],  # นักเรียน 4
        [80, 85, 89, 86]   # นักเรียน 5
    ]
}

# ฟังก์ชันคำนวณค่าเฉลี่ยคะแนนของห้อง
def calculate_average(room_scores):
    total = 0
    count = 0
    for scores in room_scores:
        total += sum(scores)
        count += len(scores)
    return total / count

# ฟังก์ชันหานักเรียนที่มีคะแนนรวมสูงสุดในห้อง
def find_top_student(room_scores):
    max_score = -float('inf')
    top_student = -1
    for student_index, scores in enumerate(room_scores):
        total_score = sum(scores)
        if total_score > max_score:
            max_score = total_score
            top_student = student_index + 1  # เพิ่ม 1 เพื่อให้ตรงกับหมายเลขนักเรียน
    return top_student, max_score

# ฟังก์ชันหาจำนวนนักเรียนที่สอบผ่านทุกวิชาในห้อง
def count_passing_students(room_scores, passing_score=60):
    passing_count = 0
    for scores in room_scores:
        if all(score >= passing_score for score in scores):
            passing_count += 1
    return passing_count

# วิเคราะห์ผลการเรียน
highest_avg_room = None
highest_avg_score = -float('inf')
top_students = {}
passing_students = {}

for room, room_scores in scores.items():
    # ค่าเฉลี่ยคะแนนของห้อง
    avg_score = calculate_average(room_scores)
    if avg_score > highest_avg_score:
        highest_avg_score = avg_score
        highest_avg_room = room
    
    # นักเรียนที่มีคะแนนรวมสูงสุดในห้อง
    top_student, top_score = find_top_student(room_scores)
    top_students[room] = (top_student, top_score)
    
    # นักเรียนที่สอบผ่านทุกวิชาในห้อง
    passing_count = count_passing_students(room_scores)
    passing_students[room] = passing_count

# แสดงผลลัพธ์
print(f"ห้องที่มีคะแนนเฉลี่ยสูงสุด: {highest_avg_room} (คะแนนเฉลี่ย {highest_avg_score:.2f})\n")
for room in scores:
    top_student, top_score = top_students[room]
    passing_count = passing_students[room]
    print(f"{room}:")
    print(f"  นักเรียนที่มีคะแนนรวมสูงสุด: นักเรียน {top_student} (คะแนนรวม {top_score})")
    print(f"  นักเรียนที่สอบผ่านทุกวิชา: {passing_count} คน\n")
