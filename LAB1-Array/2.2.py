seats = [["ว่าง" for _ in range(5)] for _ in range(3)]  # แผนผังที่นั่ง

def show_seats():
    for row in seats: print(" | ".join(row))
    
def book_seat(row, col):
    if seats[row][col] == "ว่าง": seats[row][col] = "จอง"
    else: print("ที่นั่งนี้ถูกจองแล้ว!")
    
def cancel_booking(row, col):
    if seats[row][col] == "จอง": seats[row][col] = "ว่าง"
    else: print("ที่นั่งนี้ยังไม่ได้จอง!")

def count_empty_seats():
    print("ที่นั่งว่างทั้งหมด:", sum(row.count("ว่าง") for row in seats))


while True:
    show_seats()
    action = input("เลือก: (จอง/ยกเลิก/ออก): ").strip().lower()
    if action == "ออก": break
    row, col = map(int, input("กรุณากรอกแถวและคอลัมน์ (1-3, 1-5): ").split())
    if action == "จอง": book_seat(row-1, col-1)
    elif action == "ยกเลิก": cancel_booking(row-1, col-1)
    count_empty_seats()

