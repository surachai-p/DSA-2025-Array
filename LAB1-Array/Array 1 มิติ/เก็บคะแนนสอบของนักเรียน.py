
a = [80, 90, 75, 88, 95]
avg = sum(a) / len(a)
max = max(a)
min = min(a)
avg_count = len([score for score in a if score > avg])
print(f"ค่าเฉลี่ย: {avg:.2f}")
print(f"คะแนนสูงสุด: {max}")
print(f"คะแนนต่ำสุด: {min}")
print(f"จำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย: {avg_count}")
