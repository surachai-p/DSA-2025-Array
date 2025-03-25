# เก็บคะแนนสอบของนักเรียน 4 คนใน 3 วิชา
scores = [
    [80, 70, 90],  # นักเรียน 1
    [55, 85, 60],  # นักเรียน 2
    [40, 45, 65],  # นักเรียน 3
    [95, 92, 88]   # นักเรียน 4
]

# 1. คำนวณคะแนนเฉลี่ยของแต่ละวิชา
subject_averages = []
for i in range(3):  # 3 วิชา
    total_score = sum([scores[j][i] for j in range(4)])
    subject_averages.append(total_score / 4)

# แสดงคะแนนเฉลี่ยของแต่ละวิชา
print("คะแนนเฉลี่ยของแต่ละวิชา:")
for i, avg in enumerate(subject_averages, start=1):
    print(f"วิชาที่ {i}: {avg:.2f}")

# 2. หานักเรียนที่ได้คะแนนรวมสูงสุด
total_scores_per_student = [sum(student_scores) for student_scores in scores]
max_score = max(total_scores_per_student)
top_student = total_scores_per_student.index(max_score) + 1  # บวก 1 เพื่อให้ตรงกับลำดับนักเรียน
print(f"\nคะแนนรวมสูงสุดคือของนักเรียนที่ {top_student} ด้วยคะแนนรวม {max_score}")

# 3. แสดงจำนวนนักเรียนที่สอบผ่านแต่ละวิชา (คะแนน ≥ 50)
passing_count_per_subject = []
for i in range(3):  # 3 วิชา
    passing_count = sum(1 for j in range(4) if scores[j][i] >= 50)
    passing_count_per_subject.append(passing_count)

# แสดงจำนวนนักเรียนที่สอบผ่านในแต่ละวิชา
print("\nจำนวนนักเรียนที่สอบผ่านในแต่ละวิชา (คะแนน ≥ 50):")
for i, count in enumerate(passing_count_per_subject, start=1):
    print(f"วิชาที่ {i}: {count} คน")