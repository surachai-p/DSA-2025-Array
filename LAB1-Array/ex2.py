# ข้อมูลคะแนน: 4 คน, 3 วิชา (วิชา1, วิชา2, วิชา3)
scores = [
    [65, 70, 80],  # นักเรียนคนที่ 1
    [45, 55, 60],  # นักเรียนคนที่ 2
    [90, 88, 95],  # นักเรียนคนที่ 3
    [50, 40, 55]   # นักเรียนคนที่ 4
]

num_students = len(scores)
num_subjects = len(scores[0])

# คำนวณคะแนนเฉลี่ยของแต่ละวิชา
subject_averages = []
for subject_index in range(num_subjects):
    total = sum(scores[student][subject_index] for student in range(num_students))
    avg = total / num_students
    subject_averages.append(avg)

# หานักเรียนที่ได้คะแนนรวมสูงสุด
max_total = -1
top_student = -1
for student_index in range(num_students):
    total_score = sum(scores[student_index])
    if total_score > max_total:
        max_total = total_score
        top_student = student_index + 1  # +1 เพื่อให้แสดงเป็นคนที่ 1,2,3,4

# แสดงจำนวนนักเรียนที่สอบผ่านแต่ละวิชา (คะแนนผ่าน ≥ 50)
pass_counts = [0] * num_subjects
for subject_index in range(num_subjects):
    for student_index in range(num_students):
        if scores[student_index][subject_index] >= 50:
            pass_counts[subject_index] += 1

# แสดงผลลัพธ์
print("คะแนนของนักเรียนแต่ละคน:")
for idx, score in enumerate(scores, 1):
    print(f"นักเรียนคนที่ {idx}: {score}")

print("\nคะแนนเฉลี่ยของแต่ละวิชา:")
for i in range(num_subjects):
    print(f"วิชา {i+1}: {subject_averages[i]:.2f}")

print(f"\nนักเรียนที่ได้คะแนนรวมสูงสุด: นักเรียนคนที่ {top_student} (รวม {max_total} คะแนน)")

print("\nจำนวนนักเรียนที่สอบผ่านแต่ละวิชา (คะแนน ≥ 50):")
for i in range(num_subjects):
    print(f"วิชา {i+1}: {pass_counts[i]} คน")
