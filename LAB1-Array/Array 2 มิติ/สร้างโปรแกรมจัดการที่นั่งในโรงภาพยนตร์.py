seats = [[0 for _ in range(5)] for _ in range(5)]

def show_seats():
    print("แผนผังที่นั่ง (0 = ว่าง, 1 = จอง):")
    for row in seats:
        print(" ".join(map(str, row)))


def book_seat(row, col):
    if seats[row][col] == 0:
        seats[row][col] = 1
        print(f"จองที่นั่งแถว {row+1} คอลัมน์ {col+1} สำเร็จ!")
    else:
        print(f"ที่นั่งแถว {row+1} คอลัมน์ {col+1} ถูกจองไปแล้ว")

def cancel_seat(row, col):
    if seats[row][col] == 1:
        seats[row][col] = 0
        print(f"ยกเลิกที่นั่งแถว {row+1} คอลัมน์ {col+1} สำเร็จ!")
    else:
        print(f"ที่นั่งแถว {row+1} คอลัมน์ {col+1} ยังไม่ได้ถูกจอง")


def count_empty_seats():
    empty_count = sum(row.count(0) for row in seats)
    print(f"จำนวนที่นั่งว่างทั้งหมด: {empty_count}")

show_seats()
book_seat(2, 3)
cancel_seat(2, 3)
count_empty_seats()
show_seats()
