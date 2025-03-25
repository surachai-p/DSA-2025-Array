scores = [
    [80, 90, 70],  
    [60, 55, 65],  
    [95, 88, 92],  
    [45, 40, 50]   
]


averages = [sum([scores[i][j] for i in range(4)]) / 4 for j in range(3)]
print("คะแนนเฉลี่ยของแต่ละวิชา:", averages)


total_scores = [sum(student) for student in scores]
highest_student = total_scores.index(max(total_scores)) + 1
print("นักเรียนที่ได้คะแนนรวมสูงสุด:คนที่", highest_student)


passed = [sum(1 for student in scores if student[j] >= 50) for j in range(3)]
print("จำนวนนักเรียนที่สอบผ่านแต่ละวิชา:", passed)
