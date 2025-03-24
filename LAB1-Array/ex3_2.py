import random

# กำหนดค่าพื้นฐาน
num_classes = 3
students_per_class = 5
subjects = 4
pass_score = 50

# สร้างข้อมูลคะแนนแบบสุ่ม [ห้อง][นักเรียน][วิชา]
scores = [[[random.randint(30, 100) for _ in range(subjects)] for _ in range(students_per_class)] for _ in range(num_classes)]

# หาห้องที่มีคะแนนเฉลี่ยสูงสุด
class_averages = []
for c in range(num_classes):
    total = 0
    count = 0
    for s in range(students_per_class):
        for sub in range(subjects):
            total += scores[c][s][sub]
            count += 1
    avg = total / count
    class_averages.append(avg)

best_class = class_averages.index(max(class_averages)) + 1

# หานักเรียนที่ได้คะแนนรวมสูงสุดในแต่ละห้อง
top_students = []
for c in range(num_classes):
    max_total = -1
    top_student = -1
    for s in range(students_per_class):
        total = sum(scores[c][s])
        if total > max_total:
            max_total = total
            top_student = s + 1
    top_students.append((top_student, max_total))

# แสดงจำนวนนักเรียนที่สอบผ่านทุกวิชาในแต่ละห้อง
pass_counts = []
for c in range(num_classes):
    count = 0
    for s in range(students_per_class):
        if all(score >= pass_score for score in scores[c][s]):
            count += 1
    pass_counts.append(count)

# แสดงผลลัพธ์
print(f"\nห้องที่มีคะแนนเฉลี่ยสูงสุด: ห้องที่ {best_class} ({max(class_averages):.2f} คะแนน)\n")

for c in range(num_classes):
    print(f"ห้องที่ {c+1}:")
    print(f"- นักเรียนคนที่ {top_students[c][0]} ได้คะแนนรวมสูงสุด ({top_students[c][1]} คะแนน)")
    print(f"- จำนวนคนที่สอบผ่านทุกวิชา: {pass_counts[c]} คน\n")

# แสดงข้อมูลคะแนนทั้งหมด (Optional)
for c in range(num_classes):
    print(f"คะแนนของห้องที่ {c+1}:")
    for s in range(students_per_class):
        print(f"  นักเรียน {s+1}: {scores[c][s]}")
    print()
