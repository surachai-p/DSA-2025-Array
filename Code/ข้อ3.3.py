# ฟังก์ชันเก็บคะแนนของนักเรียน 3 ห้อง (ห้องละ 5 คน, สอบ 4 วิชา)
def input_scores():
    scores = {}
    rooms = ["ห้อง A", "ห้อง B", "ห้อง C"]
    
    for room in rooms:
        print(f"\nกรุณากรอกคะแนนสำหรับ {room}:")
        students = []
        for i in range(1, 6):  # นักเรียน 5 คน
            print(f"  นักเรียน {i}:")
            student_scores = []
            for j in range(1, 5):  # สอบ 4 วิชา
                score = float(input(f"    วิชา {j}: "))
                student_scores.append(score)
            students.append(student_scores)
        scores[room] = students
    return scores

# ฟังก์ชันคำนวณคะแนนเฉลี่ยของแต่ละห้อง
def calculate_averages(scores):
    print("\nคะแนนเฉลี่ยของแต่ละห้อง:")
    for room, students in scores.items():
        total_score = sum(sum(student) for student in students)
        num_students = len(students)
        avg_score = total_score / (num_students * len(students[0]))  # จำนวนวิชาคือ 4
        print(f"{room}: {avg_score:.2f} คะแนน")

# ฟังก์ชันหานักเรียนที่ได้คะแนนรวมสูงสุดในแต่ละห้อง
def find_top_students(scores):
    print("\nนักเรียนที่ได้คะแนนรวมสูงสุดในแต่ละห้อง:")
    for room, students in scores.items():
        total_scores = [sum(student) for student in students]
        max_score = max(total_scores)
        top_student = total_scores.index(max_score) + 1  # หาคนที่ได้คะแนนสูงสุด
        print(f"{room}: นักเรียนที่ {top_student} (คะแนน {max_score})")

# ฟังก์ชันแสดงจำนวนนักเรียนที่สอบผ่านทุกวิชาในแต่ละห้อง
def count_passed_students(scores):
    passing_score = 50
    print("\nจำนวนนักเรียนที่สอบผ่านทุกวิชาในแต่ละห้อง:")
    for room, students in scores.items():
        passed_count = sum(all(score >= passing_score for score in student) for student in students)
        print(f"{room}: {passed_count} คน")

# เมนูหลัก
def menu():
    scores = input_scores()  # เรียกใช้ฟังก์ชันให้ผู้ใช้กรอกคะแนน
    while True:
        print("\n--- ระบบวิเคราะห์ผลการเรียน ---")
        print("1. แสดงคะแนนเฉลี่ยของแต่ละห้อง")
        print("2. แสดงนักเรียนที่ได้คะแนนรวมสูงสุดในแต่ละห้อง")
        print("3. แสดงจำนวนนักเรียนที่สอบผ่านทุกวิชาในแต่ละห้อง")
        print("4. ออกจากโปรแกรม")
        
        choice = input("กรุณาเลือกเมนู (1-4): ")
        
        if choice == '1':
            calculate_averages(scores)
        elif choice == '2':
            find_top_students(scores)
        elif choice == '3':
            count_passed_students(scores)
        elif choice == '4':
            print("ออกจากโปรแกรม")
            break
        else:
            print("เลือกเมนูไม่ถูกต้อง กรุณาเลือกใหม่")

# เรียกใช้งานเมนูหลัก
menu()
