seats = [["ว่าง" for _ in range(5)] for _ in range(5)]

def show_seating():
    for i, row in enumerate(seats, start=1):
        print(f"แถว {i}: {' '.join(row)}")

def book_seat():
    row, col = map(int, input("กรอกแถวและที่นั่งที่ต้องการจอง (1-5) : ").split())
    if seats[row-1][col-1] == "ว่าง":
        seats[row-1][col-1] = "จอง"
        print("จองที่นั่งสำเร็จ")
    else:
        print("ที่นั่งนี้ถูกจองแล้ว")

def cancel_booking():
    row, col = map(int, input("กรอกแถวและที่นั่งที่ต้องการยกเลิก (1-5) : ").split())
    if seats[row-1][col-1] == "จอง":
        seats[row-1][col-1] = "ว่าง"
        print("ยกเลิกการจองสำเร็จ")
    else:
        print("ที่นั่งนี้ไม่ได้ถูกจอง")

def show_available_seats():
    available = sum(row.count("ว่าง") for row in seats)
    print(f"จำนวนที่นั่งว่างทั้งหมด: {available} ที่นั่ง")

def main():
    while True:
        print("\n=== เมนู ===")
        print("1. แสดงแผนผังที่นั่ง")
        print("2. จองที่นั่ง")
        print("3. ยกเลิกการจอง")
        print("4. แสดงจำนวนที่นั่งว่าง")
        print("5. ออกจากโปรแกรม")
        choice = input("เลือกเมนู: ")

        if choice == "1":
            show_seating()
        elif choice == "2":
            book_seat()
        elif choice == "3":
            cancel_booking()
        elif choice == "4":
            show_available_seats()
        elif choice == "5":
            break
        else:
            print("เลือกเมนูไม่ถูกต้อง")

if __name__ == "__main__":
    main()
