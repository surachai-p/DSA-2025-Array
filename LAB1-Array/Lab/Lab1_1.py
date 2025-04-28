scores = [85, 90, 78, 92, 88]

average = sum(scores) / len(scores)

max_score = max(scores)
min_score = min(scores)

above_average_count = len([score for score in scores if score > average])

print("คะแนน:", scores)
print("ค่าเฉลี่ย:", round(average, 2))
print("คะแนนสูงสุด:", max_score)
print("คะแนนต่ำสุด:", min_score)
print("จำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย:", above_average_count)
