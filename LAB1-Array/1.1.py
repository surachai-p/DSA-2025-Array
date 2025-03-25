scores = [99, 88, 68, 78, 59]


total_score = 0
for score in scores:
    total_score += score
average_score = total_score / len(scores)


max_score = scores[0]
min_score = scores[0]
for score in scores:
    if score > max_score:
        max_score = score
    if score < min_score:
        min_score = score


above_average_count = 0
for score in scores:
    if score > average_score:
        above_average_count += 1


print("คะแนนเฉลี่ย: {:.2f}".format(average_score))
print("คะแนนสูงสุด: ", max_score)
print("คะแนนต่ำสุด: ", min_score)
print("จำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย: ", above_average_count)


