# ข้อมูลคะแนนสอบของนักเรียน
students = {
    "นักเรียน1": [60, 70, 80],
    "นักเรียน2": [45, 55, 65],
    "นักเรียน3": [75, 85, 95],
    "นักเรียน4": [50, 60, 40]
}

# คำนวณคะแนนเฉลี่ยของแต่ละวิชา
subject_avg = [
    sum(scores[i] for scores in students.values()) / len(students) 
    for i in range(3)
]

# หานักเรียนที่ได้คะแนนรวมสูงสุด
highest_student = max(students, key=lambda name: sum(students[name]))
highest_total = sum(students[highest_student])

# แสดงจำนวนนักเรียนที่สอบผ่านแต่ละวิชา (คะแนนผ่าน ≥ 50)
pass_counts = [
    sum(1 for scores in students.values() if scores[i] >= 50)
    for i in range(3)
]

# แสดงผลลัพธ์
print("คะแนนเฉลี่ยของแต่ละวิชา:", [round(avg, 2) for avg in subject_avg])
print(f"นักเรียนที่ได้คะแนนรวมสูงสุด: {highest_student} (รวม {highest_total} คะแนน)")
print("จำนวนนักเรียนที่สอบผ่านแต่ละวิชา:", pass_counts)
