def calculate_scores():
  """
  ฟังก์ชันคำนวณค่าสถิติต่างๆ ของคะแนนสอบนักเรียน

  Returns:
    None
  """

  # รับค่าคะแนนสอบจากผู้ใช้
  scores = []
  for i in range(5):
    score = float(input(f"กรอกคะแนนสอบของนักเรียนคนที่ {i+1}: "))
    scores.append(score)

  # คำนวณค่าเฉลี่ย
  average = sum(scores) / len(scores)

  # หาค่าสูงสุดและต่ำสุด
  max_score = max(scores)
  min_score = min(scores)

  # นับจำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย
  count_above_average = sum(score > average for score in scores)

  # แสดงผลลัพธ์
  print("\nผลลัพธ์:")
  print(f"ค่าเฉลี่ย: {average:.2f}")
  print(f"คะแนนสูงสุด: {max_score}")
  print(f"คะแนนต่ำสุด: {min_score}")
  print(f"จำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย: {count_above_average} คน")

if __name__ == "__main__":
  calculate_scores()