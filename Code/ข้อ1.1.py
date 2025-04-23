# รับคะแนนจากผู้ใช้
s = [int(input(f"กรอกคะแนนนักเรียนคนที่ {i+1}: ")) for i in range(5)]

# หาค่าเฉลี่ย
average = sum(s) / len(s)

# หาคะแนนสูงสุดและต่ำสุด
h = max(s)
l = min(s)

# แสดงผลลัพธ์
print(f"\nค่าเฉลี่ยของคะแนน: {average:.2f}")
print(f"คะแนนสูงสุด: {h}")
print(f"คะแนนต่ำสุด: {l}")

# หาจำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย
a = len([score for score in s if score > average])
print(f"จำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย: {a}")

