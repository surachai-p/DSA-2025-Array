##สร้างโปรแกรมจัดการที่นั่งในโรงภาพยนตร์:
#แสดงแผนผังที่นั่ง (ว่าง/จอง)
#จองที่นั่ง
#ยกเลิกการจอง
#แสดงจำนวนที่นั่งว่างทั้งหมด

def create_seats(rows, cols):
  """สร้างแผนผังที่นั่งเริ่มต้น"""
  return [[0 for _ in range(cols)] for _ in range(rows)]

def show_seats(seats):
  """แสดงแผนผังที่นั่ง"""
  for row in seats:
    print(' '.join(['O' if seat == 0 else 'X' for seat in row]))

def book_seat(seats, row, col):
  """จองที่นั่ง"""
  if 0 <= row < len(seats) and 0 <= col < len(seats[0]) and seats[row][col] == 0:
    seats[row][col] = 1
    print("จองที่นั่งสำเร็จ")
  else:
    print("ไม่สามารถจองที่นั่งได้")

def cancel_booking(seats, row, col):
  """ยกเลิกการจอง"""
  if 0 <= row < len(seats) and 0 <= col < len(seats[0]) and seats[row][col] == 1:
    seats[row][col] = 0
    print("ยกเลิกการจองสำเร็จ")
  else:
    print("ไม่สามารถยกเลิกการจองได้")

def count_empty_seats(seats):
  """นับจำนวนที่นั่งว่าง"""
  return sum(sum(row) for row in seats)

# สร้างโรงภาพยนตร์ที่มี 10 แถว 20 ที่นั่ง
rows = 5
cols = 10
seats = create_seats(rows, cols)

# แสดงแผนผังที่นั่งเริ่มต้น
show_seats(seats)

# ตัวอย่างการใช้งาน
book_seat(seats, 2, 3)  # จองที่นั่งแถวที่ 3 ที่นั่งที่ 4
book_seat(seats, 2, 1)
show_seats(seats)

cancel_booking(seats, 2, 3)  # ยกเลิกการจอง

print("จำนวนที่นั่งว่างทั้งหมด:", count_empty_seats(seats))