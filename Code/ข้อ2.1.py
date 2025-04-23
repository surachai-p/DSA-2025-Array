# ให้ผู้ใช้กรอกคะแนนของนักเรียน 4 คนใน 3 วิชา
scores = []
print("กรุณากรอกคะแนนของนักเรียน 4 คน (แต่ละคนมี 3 วิชา):")
for i in range(4):  # นักเรียน 4 คน
    print(f"\nนักเรียนคนที่ {i + 1}:")
    student_scores = [int(input(f"วิชา {j + 1}: ")) for j in range(3)]
    scores.append(student_scores)

# คำนวณคะแนนเฉลี่ยของแต่ละวิชา
subject_averages = [sum(subject) / len(scores) for subject in zip(*scores)]
print("\nคะแนนเฉลี่ยของแต่ละวิชา:", [round(avg, 2) for avg in subject_averages])


# หานักเรียนที่ได้คะแนนรวมสูงสุด
total_scores = [sum(student) for student in scores]
max_score = max(total_scores)
top_student = total_scores.index(max_score) + 1
print(f"\nนักเรียนที่ได้คะแนนรวมสูงสุด: คนที่ {top_student} (คะแนน {max_score})")

# หาจำนวนนักเรียนที่สอบผ่านแต่ละวิชา (คะแนนผ่าน ≥ 50)
passes = [len([score for score in subject if score >= 50]) for subject in zip(*scores)]
for i, count in enumerate(passes, start=1):
    print(f"จำนวนนักเรียนที่สอบผ่านวิชา {i}: {count} คน") 
