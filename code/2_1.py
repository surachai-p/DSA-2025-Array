score = [
    [45, 48, 59, 70],
    [51, 65, 92, 87],
    [80, 60, 40, 99]
]

avg = [sum(row)/4 for row in score]
print(f"คะแนนเฉลี่ยของแต่ละวิชาคือ {avg}")

total = [sum(col) for col in zip(*score)]
max_score = max(total)
print(f"นักเรียนคนที่ {total.index(max_score)+1} ได้คะแนนสูงสุด")

pass_student = []
for i in range(3):
    num = 0
    for j in range(4):
        if score[i][j] >= 50:
            num += 1
    pass_student.append(num)

print(f"จำนวนนักเรียนที่ผ่านในแต่ละวิชา {pass_student}")