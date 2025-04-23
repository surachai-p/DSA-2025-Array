# สร้างแผนผังที่นั่ง 5 แถว 6 ที่นั่งต่อแถว (0 = ว่าง, 1 = จองแล้ว)
seats = [[0 for _ in range(6)] for _ in range(5)]

# ฟังก์ชันแสดงแผนผังที่นั่ง
def show_seating():
    print("\nแผนผังที่นั่ง (0 = ว่าง, 1 = จองแล้ว):")
    for row in seats:
        print(" ".join(map(str, row)))

# ฟังก์ชันจองที่นั่ง
def book_seat():
    row = int(input("กรุณากรอกแถวที่ต้องการจอง (1-5): ")) - 1
    col = int(input("กรุณากรอกที่นั่งในแถวนั้น (1-6): ")) - 1
    if seats[row][col] == 0:
        seats[row][col] = 1
        print("จองที่นั่งเรียบร้อย!")
    else:
        print("ที่นั่งนี้ถูกจองแล้ว กรุณาเลือกที่นั่งอื่น")

# ฟังก์ชันยกเลิกการจอง
def cancel_booking():
    row = int(input("กรุณากรอกแถวที่ต้องการยกเลิก (1-5): ")) - 1
    col = int(input("กรุณากรอกที่นั่งในแถวนั้น (1-6): ")) - 1
    if seats[row][col] == 1:
        seats[row][col] = 0
        print("ยกเลิกการจองเรียบร้อย!")
    else:
        print("ที่นั่งนี้ยังไม่ได้ถูกจอง")

# ฟังก์ชันแสดงจำนวนที่นั่งว่างทั้งหมด
def show_available_seats():
    available = sum(row.count(0) for row in seats)
    print(f"\nจำนวนที่นั่งว่างทั้งหมด: {available} ที่นั่ง")

# เมนูหลัก
def menu():
    while True:
        print("\n--- ระบบจัดการที่นั่งในโรงภาพยนตร์ ---")
        print("1. แสดงแผนผังที่นั่ง")
        print("2. จองที่นั่ง")
        print("3. ยกเลิกการจอง")
        print("4. แสดงจำนวนที่นั่งว่าง")
        print("5. ออกจากโปรแกรม")
        
        choice = input("กรุณาเลือกเมนู (1-5): ")
        
        if choice == '1':
            show_seating()
        elif choice == '2':
            book_seat()
        elif choice == '3':
            cancel_booking()
        elif choice == '4':
            show_available_seats()
        elif choice == '5':
            print("ออกจากโปรแกรม")
            break
        else:
            print("เลือกเมนูไม่ถูกต้อง กรุณาเลือกใหม่")

# เรียกใช้งานเมนูหลัก
menu()
