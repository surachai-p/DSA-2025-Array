##เขียนโปรแกรมวิเคราะห์ผลการเรียน:
#เก็บคะแนนของนักเรียน 3 ห้อง
#ห้องละ 5 คน
#สอบ 4 วิชา
#หาห้องที่มีคะแนนเฉลี่ยสูงสุด
#หานักเรียนที่ได้คะแนนรวมสูงสุดในแต่ละห้อง
#แสดงจำนวนนักเรียนที่สอบผ่านทุกวิชาในแต่ละห้อง

#วิเคราะห์ผลการเรียนของนักเรียน
def analyze_grades(grades):

    num_rooms, num_students, num_subjects = len(grades), len(grades[0]), len(grades[0][0])
    
    # คำนวณคะแนนเฉลี่ยของแต่ละห้อง
    room_averages = [sum(sum(student) for student in room) / (num_students * num_subjects) for room in grades]
    
    # หาห้องที่มีคะแนนเฉลี่ยสูงสุด
    max_avg_room = room_averages.index(max(room_averages))
    
    # หานักเรียนที่ได้คะแนนรวมสูงสุดในแต่ละห้อง
    max_students = [max(room, key=sum) for room in grades]
    
    # นับจำนวนนักเรียนที่สอบผ่านทุกวิชาในแต่ละห้อง (สมมติว่าผ่าน >= 50)
    pass_all_counts = [sum(all(score >= 50 for score in student) for student in room) for room in grades]
    
    return room_averages, max_avg_room, max_students, pass_all_counts

# ข้อมูลคะแนนนักเรียน 
grades = [
    [[84, 90, 75, 85], [65, 85, 92, 78], [72, 78, 80, 82], [95, 88, 90, 92], [70, 75, 80, 85]],
    [[70, 80, 70, 80], [70, 75, 85, 90], [80, 85, 90, 95], [70, 75, 80, 85], [65, 70, 75, 80]],
    [[90, 90, 85, 90], [50, 95, 90, 95], [80, 85, 80, 85], [75, 80, 75, 80], [80, 85, 80, 85]]
]

# วิเคราะห์ผลการเรียน
room_averages, max_avg_room, max_students, pass_all_counts = analyze_grades(grades)

# แสดงผลลัพธ์
print("คะแนนเฉลี่ยของแต่ละห้อง:", room_averages)
print("ห้องที่มีคะแนนเฉลี่ยสูงสุด: ห้องที่", max_avg_room + 1)
print("นักเรียนที่ได้คะแนนรวมสูงสุดในแต่ละห้อง:", max_students)
print("จำนวนนักเรียนที่สอบผ่านทุกวิชาในแต่ละห้อง:", pass_all_counts)