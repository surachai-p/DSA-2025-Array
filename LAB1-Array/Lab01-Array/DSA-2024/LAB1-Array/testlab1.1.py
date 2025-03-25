### แบบฝึกหัดที่ 1: Array 1 มิติ

##1. จงเขียนโปรแกรมสร้าง Array เก็บคะแนนสอบของนักเรียน 5 คน และ:
# - หาค่าเฉลี่ย
# - หาคะแนนสูงสุดและต่ำสุด
# - แสดงจำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย

def calculate_scores():
  # สร้าง list เก็บคะแนนสอบ
  scores = []

  # รับค่าคะแนน
  scores = [int(input(f"ป้อนคะแนนของนักเรียนคนที่ {i+1}: ")) for i in range(5)]
  # หาค่าเฉลี่ย
  average = sum(scores) / len(scores)

  # หาค่าคะแนนสูงสุดและต่ำสุด
  max_score = max(scores)
  min_score = min(scores)

  # แสดงจำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย
  count_above_average = sum(1 for score in scores if score > average)

  # แสดงผลลัพธ์
  print("คะแนนสอบทั้งหมด:", scores)
  print("ค่าเฉลี่ย:", average)
  print("คะแนนสูงสุด:", max_score)
  print("คะแนนต่ำสุด:", min_score)
  print(f"จำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย: {count_above_average} คน")

calculate_scores()