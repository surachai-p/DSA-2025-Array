# ข้อ 1: โปรแกรมจัดการคะแนนนักเรียน (Array 2 มิติ)

def student_scores():
    students = 4
    subjects = 3
    scores = []
    
    # รับค่าคะแนน
    for i in range(students):
        scores.append([int(input(f"กรอกคะแนนของนักเรียน {i+1} วิชา {j+1}: ")) for j in range(subjects)])
    
    # คำนวณค่าเฉลี่ยของแต่ละวิชา
    avg_scores = [sum(subject) / students for subject in zip(*scores)]
    
    # หานักเรียนที่ได้คะแนนรวมสูงสุด
    total_scores = [sum(student) for student in scores]
    max_index = total_scores.index(max(total_scores))
    
    # นับจำนวนนักเรียนที่สอบผ่านในแต่ละวิชา (คะแนนผ่าน >= 50)
    pass_counts = [sum(1 for student in scores if student[i] >= 50) for i in range(subjects)]
    
    print(f"ค่าเฉลี่ยของแต่ละวิชา: {avg_scores}")
    print(f"นักเรียนที่ได้คะแนนรวมสูงสุดคือคนที่ {max_index + 1}")
    print(f"จำนวนคนที่สอบผ่านในแต่ละวิชา: {pass_counts}")

# ข้อ 2: โปรแกรมจัดการที่นั่งในโรงภาพยนตร์

def cinema_seating():
    rows, cols = 5, 5  # ขนาดแถวและคอลัมน์ของที่นั่ง
    seats = [[0] * cols for _ in range(rows)]
    
    while True:
        print("\nแผนผังที่นั่ง:")
        for row in seats:
            print(" ".join("O" if seat == 0 else "X" for seat in row))
        
        print("\n1. จองที่นั่ง")
        print("2. ยกเลิกการจอง")
        print("3. แสดงจำนวนที่นั่งว่างทั้งหมด")
        print("4. ออกจากโปรแกรม")
        
        choice = input("เลือกเมนู (1-4): ")
        
        if choice == '1':
            r, c = map(int, input("กรอกแถวและคอลัมน์ที่ต้องการจอง (0-4 0-4): ").split())
            if seats[r][c] == 0:
                seats[r][c] = 1
                print("จองที่นั่งสำเร็จ!")
            else:
                print("ที่นั่งนี้ถูกจองแล้ว!")
        elif choice == '2':
            r, c = map(int, input("กรอกแถวและคอลัมน์ที่ต้องการยกเลิกการจอง: ").split())
            if seats[r][c] == 1:
                seats[r][c] = 0
                print("ยกเลิกการจองสำเร็จ!")
            else:
                print("ที่นั่งนี้ยังไม่ได้จอง!")
        elif choice == '3':
            print(f"จำนวนที่นั่งว่างทั้งหมด: {sum(row.count(0) for row in seats)}")
        elif choice == '4':
            print("ออกจากโปรแกรม")
            break
        else:
            print("กรุณาเลือกเมนูให้ถูกต้อง!")

# student_scores()  # ใช้เมื่อต้องการรันโปรแกรมคะแนน
# cinema_seating()  # ใช้เมื่อต้องการรันโปรแกรมโรงภาพยนตร์