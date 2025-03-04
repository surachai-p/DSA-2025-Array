##ข้อ1.1
##หาค่าเฉลี่ย
scores = [66, 89, 72, 59, 91]
average_score = sum(scores) / len(scores)
print("ค่าเฉลี่ยคือ:", average_score)
##หาคะแนนสูงสุดและต่ำสุด
max_score = max(scores)
print("คะแนนสูงสุดคือ:", max_score)
min_score = min(scores)
print("คะแนนต่ำสุดคือ:", min_score)
##แสดงจำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย
above_average = sum([1 for score in scores if score > average_score])
print("จำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ยคือ:", above_average)

##ข้อ1.2
inventory = []
##เพิ่มสินค้าใหม่
def add_product():
    product_name = input("กรุณากรอกชื่อสินค้า: ")
    quantity = int(input(f"กรุณากรอกจำนวนสินค้าของ '{product_name}': "))
    
    inventory[product_name] = {'quantity': quantity, 'price': price}
    print(f"สินค้าชื่อ '{product_name}' ถูกเพิ่มเรียบร้อย!")
##ลบสินค้าที่หมด
def remove_out_of_stock():
    product_name = input("กรุณากรอกชื่อสินค้าที่ต้องการลบ: ")
    if product_name in inventory:
        if inventory[product_name]['quantity'] == 0:
            del inventory[product_name]
            print(f"สินค้าชื่อ '{product_name}' ถูกลบจากรายการแล้ว!")
        else:
            print(f"สินค้าชื่อ '{product_name}' ยังมีจำนวนอยู่ในสต็อก!")
    else:
        print(f"ไม่พบสินค้าชื่อ '{product_name}' ในระบบ!")
##ค้นหาสินค้า
def search_product():
    product_name = input("กรุณากรอกชื่อสินค้าที่ต้องการค้นหา: ")
    if product_name in inventory:
        print(f"สินค้า '{product_name}' มีรายละเอียดดังนี้:")
        print(f"จำนวน: {inventory[product_name]['quantity']}")
    else:
        print(f"ไม่พบสินค้าชื่อ '{product_name}' ในระบบ!")
##แสดงรายการสินค้าทั้งหมด
def show_all_products():
    if inventory:
        print("\nรายการสินค้าทั้งหมด:")
        for product_name, details in inventory.items():
            print(f"ชื่อสินค้า: {product_name}")
            print(f"จำนวน: {details['quantity']}")
    else:
        print("ยังไม่มีสินค้ารายการใดในระบบ!")
##หลักการการทำงาน
def main():
    while True:
        print("1. เพิ่มสินค้าใหม่")
        print("2. ลบสินค้าที่หมด")
        print("3. ค้นหาสินค้า")
        print("4. แสดงรายการสินค้าทั้งหมด")
        
        choice = input("กรุณาเลือกตัวเลือก (1-4): ")
        
        if choice == '1':
            add_product()
        elif choice == '2':
            remove_out_of_stock()
        elif choice == '3':
            search_product()
        elif choice == '4':
            show_all_products()
if __name__ == "__main__":
    main()

##ข้อ2.1
##เก็บคะแนนสอบ 3 วิชาของนักเรียน 4 คน
students_scores = {
    "นักเรียน 1": [55, 70, 90],
    "นักเรียน 2": [72, 55, 95],
    "นักเรียน 3": [95, 85, 92],
    "นักเรียน 4": [80, 69, 95]
}
def calculate_average(scores):
    return sum(scores) / len(scores)
##คำนวณคะแนนเฉลี่ยของแต่ละวิชา
subjects_scores = list(zip(*students_scores.values()))
averages = [calculate_average(subject_scores) for subject_scores in subjects_scores]
print("คะแนนเฉลี่ยของแต่ละวิชา:")
for i, avg in enumerate(averages):
    print(f"วิชา {i+1}: {avg:.2f}")
##หานักเรียนที่ได้คะแนนรวมสูงสุด
def highest_total_score(students_scores):
    max_score = 0
    top_student = ""
    for student, scores in students_scores.items():
        total_score = sum(scores)
        if total_score > max_score:
            max_score = total_score
            top_student = student
    return top_student, max_score
top_student, top_score = highest_total_score(students_scores)
print(f"\n{top_student} ได้คะแนนรวมสูงสุด: {top_score}")
##แสดงจำนวนนักเรียนที่สอบผ่านแต่ละวิชา (คะแนนผ่าน ≥ 50)
def passed_students_count(students_scores):
    passed_count = [0, 0, 0]
    for scores in students_scores.values():
        for i in range(3):  
            if scores[i] >= 50:
                passed_count[i] += 1
    return passed_count
passed_count = passed_students_count(students_scores)
for i, count in enumerate(passed_count):
    print(f"วิชา {i+1}: {count} คนสอบผ่าน")
    
##ข้อ2.2
##กำหนดแผนผังที่นั่ง(10 แถว x 10 คอลัมน์)
seats = [['ว่าง' for _ in range(10)] for _ in range(10)]
##แสดงแผนผังที่นั่ง
def display_seats():
    print("\nแผนผังที่นั่ง (ว่าง/จอง):")
    for row in seats:
        print("  ".join(row))
    print()
##จองที่นั่ง
def book_seat(row, col):
    if row < 0 or row >= len(seats) or col < 0 or col >= len(seats[0]):
        print("ตำแหน่งที่นั่งไม่ถูกต้อง! กรุณาเลือกที่นั่งในแผนผัง.")
    elif seats[row][col] == 'จอง':
        print("ที่นั่งนี้ถูกจองแล้ว! กรุณาเลือกที่นั่งอื่น.")
    else:
        seats[row][col] = 'จอง'
        print(f"จองที่นั่งที่แถว {row+1}, คอลัมน์ {col+1} เรียบร้อยแล้ว!")
##ยกเลิกการจอง
def cancel_booking(row, col):
    if row < 0 or row >= len(seats) or col < 0 or col >= len(seats[0]):
        print("ตำแหน่งที่นั่งไม่ถูกต้อง! กรุณาเลือกที่นั่งในแผนผัง.")
    elif seats[row][col] == 'ว่าง':
        print("ที่นั่งนี้ยังไม่ได้จอง!")
    else:
        seats[row][col] = 'ว่าง'
        print(f"ยกเลิกการจองที่นั่งที่แถว {row+1}, คอลัมน์ {col+1} เรียบร้อยแล้ว!")
##แสดงจำนวนที่นั่งว่างทั้งหมด
def available_seats():
    available = sum(row.count('ว่าง') for row in seats)
    print(f"จำนวนที่นั่งว่างทั้งหมด: {available} ที่นั่ง")
##หลักการการทำงาน
def menu():
    while True:
        print("1. แสดงแผนผังที่นั่ง")
        print("2. จองที่นั่ง")
        print("3. ยกเลิกการจอง")
        print("4. แสดงจำนวนที่นั่งว่าง")
        
        choice = input("เลือกตัวเลือก (1-4): ")

        if choice == '1':
            display_seats()
        elif choice == '2':
            row = int(input("กรุณากรอกแถวที่นั่ง (1-10): ")) - 1
            col = int(input("กรุณากรอกคอลัมน์ที่นั่ง (1-10): ")) - 1
            book_seat(row, col)
        elif choice == '3':
            row = int(input("กรุณากรอกแถวที่นั่ง (1-10): ")) - 1
            col = int(input("กรุณากรอกคอลัมน์ที่นั่ง (1-10): ")) - 1
            cancel_booking(row, col)
        elif choice == '4':
            available_seats()
menu()

##ข้อ3.1
##กำหนดอุณหภูมิ (3 เมือง,วัด 4 ครั้ง/วัน, 7 วัน)
temperatures = {
    'กรุงเทพ': [
        [30, 32, 31, 33],  
        [31, 32, 30, 33],  
        [32, 33, 31, 34],  
        [30, 31, 32, 34],  
        [31, 32, 32, 33],  
        [32, 33, 30, 34],  
        [33, 34, 32, 35]   
    ],
    'ภูเก็ต': [
        [30, 33, 31, 32],
        [31, 33, 32, 32],
        [32, 32, 31, 31],
        [30, 31, 31, 30],
        [31, 31, 33, 34],
        [31, 33, 33, 34],
        [31, 34, 35, 36]
    ],
    'เชียงใหม่': [
        [28, 29, 30, 32],
        [29, 30, 31, 33],
        [30, 32, 31, 33],
        [29, 31, 30, 32],
        [30, 32, 32, 34],
        [31, 33, 32, 35],
        [32, 34, 33, 36]
    ]
}
##หาค่าเฉลี่ยอุณหภูมิของแต่ละเมือง
def average_temperature(city_temps):
    total_temp = sum(sum(day) for day in city_temps)
    total_measurements = len(city_temps) * len(city_temps[0])##จำนวนการวัดทั้งหมด(7วัน x 4ครั้ง)
    return total_temp / total_measurements
##หาวันและเวลาที่อุณหภูมิสูงที่สุด
def highest_temperature_day_time(city_temps):
    max_temp = float('-inf')  
    max_day = max_time = -1
    
    for day_index, day in enumerate(city_temps):
        for time_index, temp in enumerate(day):
            if temp > max_temp:
                max_temp = temp
                max_day = day_index + 1  ##วันเริ่มจาก1
                max_time = time_index + 1  ##เวลาที่วัดเริ่มจาก1   
    return max_temp, max_day, max_time
for city, temps in temperatures.items():
    avg_temp = average_temperature(temps)
    max_temp, max_day, max_time = highest_temperature_day_time(temps)
    
    print(f"\nเมือง: {city}")
    print(f"ค่าเฉลี่ยอุณหภูมิ: {avg_temp:.2f}°C")
    print(f"อุณหภูมิสูงที่สุด: {max_temp}°C (วัน {max_day}, เวลา {max_time}:00)")
    
##ข้อ3.2
##คะแนนของนักเรียน(3 ห้องเรียน, 5 คน, 4 วิชา)
scores = {
    'ห้อง 1': [
        [80, 69, 88, 85],  
        [70, 72, 85, 75],  
        [85, 78, 62, 90],  
        [78, 82, 98, 84],  
        [92, 85, 88, 94]   
    ],
    'ห้อง 2': [
        [60, 68, 79, 65],  
        [55, 70, 79, 58],  
        [65, 89, 75, 72],  
        [80, 79, 95, 88],  
        [85, 80, 96, 88]   
    ],
    'ห้อง 3': [
        [90, 90, 75, 88],  
        [85, 86, 88, 82],  
        [88, 79, 90, 90],  
        [92, 84, 95, 93],  
        [80, 95, 90, 88]   
    ]
}
##หาคะแนนเฉลี่ยของแต่ละห้อง
def average_score_of_class(class_scores):
    total_score = sum(sum(student_scores) for student_scores in class_scores)  
    total_subjects = len(class_scores) * len(class_scores[0])  #การวัดทั้งหมด(5 นักเรียน x 4 วิชา)
    return total_score / total_subjects
##หานักเรียนที่ได้คะแนนรวมสูงสุดในแต่ละห้อง
def highest_total_score_student(class_scores):
    highest_total = -1
    highest_student = -1
    for student_index, student_scores in enumerate(class_scores):
        total_score = sum(student_scores)
        if total_score > highest_total:
            highest_total = total_score
            highest_student = student_index + 1  
    return highest_student, highest_total
##หานักเรียนที่สอบผ่านทุกวิชาในแต่ละห้อง
def passing_students(class_scores, passing_score=50):
    passing_count = 0
    for student_scores in class_scores:
        if all(score >= passing_score for score in student_scores):  
            passing_count += 1
    return passing_count
##วิเคราะห์ผลการเรียน
highest_avg_score = -1
highest_avg_class = ""
for class_name, class_scores in scores.items():
    ##คะแนนเฉลี่ยของแต่ละห้อง
    avg_score = average_score_of_class(class_scores)
    ##หานักเรียนที่ได้คะแนนรวมสูงสุดในแต่ละห้อง
    highest_student, highest_total = highest_total_score_student(class_scores)
    ##หานักเรียนที่สอบผ่านทุกวิชา
    passing_count = passing_students(class_scores)
    
    print(f"\n{class_name}:")
    print(f"คะแนนเฉลี่ยของห้อง: {avg_score:.2f}")
    print(f"นักเรียนที่ได้คะแนนรวมสูงสุด: นักเรียนที่ {highest_student} คะแนนรวม {highest_total}")
    print(f"จำนวนนักเรียนที่สอบผ่านทุกวิชา: {passing_count} คน")
##หาห้องที่มีคะแนนเฉลี่ยสูงสุด
    if avg_score > highest_avg_score:
        highest_avg_score = avg_score
        highest_avg_class = class_name
print(f"\nห้องที่มีคะแนนเฉลี่ยสูงสุดคือ: {highest_avg_class} ({highest_avg_score:.2f})") 