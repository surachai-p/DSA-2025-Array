 # กำหนดแถวและคอลัมน์ของโรงภาพยนตร์ (เช่น 5 แถว 5 คอลัมน์)
rows = 5
cols = 5

# สร้างแผนผังที่นั่ง (ว่าง = 0, จอง = 1)
seats = [[0 for _ in range(cols)] for _ in range(rows)]

# ฟังก์ชันแสดงแผนผังที่นั่ง
def show_seats():
    print("\nแผนผังที่นั่ง (0 = ว่าง, 1 = จอง):")
    print("   " + " ".join(f"{i+1}" for i in range(cols)))
    for i in range(rows):
        row_display = " ".join(str(seats[i][j]) for j in range(cols))
        print(f"{i+1}  {row_display}")
    print()

# ฟังก์ชันจองที่นั่ง
def book_seat():
    row = int(input("กรอกหมายเลขแถวที่ต้องการจอง (1-5): ")) - 1
    col = int(input("กรอกหมายเลขคอลัมน์ที่ต้องการจอง (1-5): ")) - 1
    if seats[row][col] == 0:
        seats[row][col] = 1
        print("จองที่นั่งเรียบร้อย!\n")
    else:
        print("ที่นั่งนี้ถูกจองแล้ว!\n")

# ฟังก์ชันยกเลิกการจอง
def cancel_seat():
    row = int(input("กรอกหมายเลขแถวที่ต้องการยกเลิก (1-5): ")) - 1
    col = int(input("กรอกหมายเลขคอลัมน์ที่ต้องการยกเลิก (1-5): ")) - 1
    if seats[row][col] == 1:
        seats[row][col] = 0
        print("ยกเลิกการจองเรียบร้อย!\n")
    else:
        print("ที่นั่งนี้ยังว่างอยู่!\n")

# ฟังก์ชันแสดงจำนวนที่นั่งว่างทั้งหมด
def show_available():
    available = sum(seat == 0 for row in seats for seat in row)
    print(f"จำนวนที่นั่งว่างทั้งหมด: {available} ที่นั่ง\n")

# เมนูหลัก
while True:
    print("=== ระบบจัดการที่นั่งในโรงภาพยนตร์ ===")
    print("1. แสดงแผนผังที่นั่ง")
    print("2. จองที่นั่ง")
    print("3. ยกเลิกการจอง")
    print("4. แสดงจำนวนที่นั่งว่างทั้งหมด")
    print("5. ออกจากโปรแกรม")

    choice = input("เลือกเมนู (1-5): ")
    print()

    if choice == "1":
        show_seats()
    elif choice == "2":
        book_seat()
    elif choice == "3":
        cancel_seat()
    elif choice == "4":
        show_available()
    elif choice == "5":
        print("ออกจากโปรแกรมแล้ว")
        break
    else:
        print("กรุณาเลือกเมนูให้ถูกต้อง (1-5)\n")
