# เก็บคะแนนสอบ 3 วิชาของนักเรียน 4 คน
scores = [
    [80, 70, 90],  
    [60, 50, 75],  
    [85, 95, 88],  
    [45, 55, 60]   
]

average_subjects = [sum(subject) / len(subject) for subject in zip(*scores)]

total_scores = [sum(student) for student in scores]
max_total_score = max(total_scores)
top_student = total_scores.index(max_total_score) + 1

pass_count = [sum(1 for student in scores if student[i] >= 50) for i in range(3)]

print(f"คะแนนเฉลี่ยแต่ละวิชา: {average_subjects}")
print(f"นักเรียนที่ได้คะแนนรวมสูงสุด: นักเรียน {top_student} ({max_total_score} คะแนน)")
print(f"จำนวนนักเรียนที่สอบผ่านแต่ละวิชา: {pass_count}")
