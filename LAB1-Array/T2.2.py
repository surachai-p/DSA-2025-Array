class Cinema:
    def __init__(self, rows, cols):
        # สร้างแผนผังที่นั่ง 2 มิติ (เริ่มต้นทั้งหมดว่าง)
        self.seats = [['ว่าง' for _ in range(cols)] for _ in range(rows)]

    def show_seats(self):
        """แสดงแผนผังที่นั่ง"""
        print("แผนผังที่นั่ง:")
        for row in self.seats:
            print(' '.join(row))
        print()

    def book_seat(self, row, col):
        """จองที่นั่ง"""
        if self.seats[row][col] == 'ว่าง':
            self.seats[row][col] = 'จอง'
            print(f"จองที่นั่ง {row+1}-{col+1} เรียบร้อยแล้ว\n")
        else:
            print(f"ที่นั่ง {row+1}-{col+1} ถูกจองแล้ว\n")

    def cancel_booking(self, row, col):
        """ยกเลิกการจอง"""
        if self.seats[row][col] == 'จอง':
            self.seats[row][col] = 'ว่าง'
            print(f"ยกเลิกการจองที่นั่ง {row+1}-{col+1} เรียบร้อยแล้ว\n")
        else:
            print(f"ที่นั่ง {row+1}-{col+1} ยังไม่ถูกจอง\n")

    def available_seats(self):
        """แสดงจำนวนที่นั่งว่างทั้งหมด"""
        available_count = sum(row.count('ว่าง') for row in self.seats)
        print(f"จำนวนที่นั่งว่างทั้งหมด: {available_count} ที่\n")


# สร้างออบเจ็กต์ Cinema สำหรับโรงภาพยนตร์
cinema = Cinema(5, 5)  # สมมติว่าโรงภาพยนตร์มี 5 แถว 5 คอลัมน์

# ตัวอย่างการใช้งานฟังก์ชันต่างๆ
cinema.show_seats()  # แสดงแผนผังที่นั่ง

# จองที่นั่ง
cinema.book_seat(0, 0)  # จองที่นั่งแถว 1 คอลัมน์ 1
cinema.book_seat(1, 2)  # จองที่นั่งแถว 2 คอลัมน์ 3

# แสดงแผนผังที่นั่งหลังจอง
cinema.show_seats()

# ยกเลิกการจอง
cinema.cancel_booking(0, 0)  # ยกเลิกที่นั่งแถว 1 คอลัมน์ 1

# แสดงแผนผังที่นั่งหลังยกเลิก
cinema.show_seats()

# แสดงจำนวนที่นั่งว่าง
cinema.available_seats()