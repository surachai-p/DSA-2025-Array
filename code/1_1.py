score = [55, 62, 78, 80, 98]
#หาค่าเฉลี่ย
a = 0
for i in score:
    a += i
a = a/len(score)
print(f"Average is : {a}")
#หาคะแนนสูงสุดและต่ำที่สุด
print(f"Max score is : {max(score)}")
print(f"Min score is : {min(score)}")
#แสดงจำนวนคนที่ได้มากกว่าค่าเฉลี่ย
num = 0
for b in score:
    if b > a: 
        num += 1
print(f"Number of student who got more than AVG is : {num} ")