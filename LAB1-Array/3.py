# ข้อ 1: โปรแกรมจัดการข้อมูลอุณหภูมิ

def climate_data():
    cities = 3
    days = 7
    times_per_day = 4
    
    temperatures = []
    for i in range(cities):
        print(f"\nกรอกข้อมูลอุณหภูมิสำหรับเมือง {i+1}:")
        city_temp = []
        for j in range(days):
            daily_temps = [float(input(f"  วัน {j+1} เวลา {k+1}: ")) for k in range(times_per_day)]
            city_temp.append(daily_temps)
        temperatures.append(city_temp)
    
    # คำนวณค่าเฉลี่ยของแต่ละเมือง
    avg_temps = [sum(sum(day) for day in city) / (days * times_per_day) for city in temperatures]
    print(f"ค่าเฉลี่ยอุณหภูมิของแต่ละเมือง: {avg_temps}")
    
    # หาเวลาที่ร้อนที่สุดและเย็นที่สุดในแต่ละเมือง
    for i, city in enumerate(temperatures):
        all_temps = [(temp, d, t) for d, day in enumerate(city) for t, temp in enumerate(day)]
        max_temp, max_day, max_time = max(all_temps)
        min_temp, min_day, min_time = min(all_temps)
        print(f"เมือง {i+1}: อุณหภูมิสูงสุด {max_temp} °C (วัน {max_day+1} เวลา {max_time+1}), ต่ำสุด {min_temp} °C (วัน {min_day+1} เวลา {min_time+1})")

# ข้อ 2: โปรแกรมจัดการคลังสินค้า

def warehouse_management():
    warehouses = 3
    floors = 4
    slots = 5
    
    stock = [[[int(input(f"คลัง {w+1} ชั้น {f+1} ช่อง {s+1}: ")) for s in range(slots)] for f in range(floors)] for w in range(warehouses)]
    
    # หาคลังที่มีสินค้ามากที่สุด
    total_stock = [sum(sum(floor) for floor in warehouse) for warehouse in stock]
    max_stock_warehouse = total_stock.index(max(total_stock)) + 1
    print(f"คลังที่มีสินค้ามากที่สุดคือ คลัง {max_stock_warehouse}")
    
    # หาตำแหน่งที่ว่าง (สินค้า = 0)
    empty_positions = [(w+1, f+1, s+1) for w in range(warehouses) for f in range(floors) for s in range(slots) if stock[w][f][s] == 0]
    print(f"ตำแหน่งที่ว่าง: {empty_positions}")

# ข้อ 3: โปรแกรมวิเคราะห์ผลการเรียน

def student_performance():
    rooms = 3
    students = 5
    subjects = 4
    
    scores = [[[int(input(f"ห้อง {r+1} นักเรียน {s+1} วิชา {sub+1}: ")) for sub in range(subjects)] for s in range(students)] for r in range(rooms)]
    
    # หาห้องที่มีค่าเฉลี่ยสูงสุด
    avg_scores = [sum(sum(student) for student in room) / (students * subjects) for room in scores]
    best_room = avg_scores.index(max(avg_scores)) + 1
    print(f"ห้องที่มีค่าเฉลี่ยสูงสุดคือ ห้อง {best_room}")
    
    # หานักเรียนที่คะแนนรวมสูงสุดในแต่ละห้อง
    for r, room in enumerate(scores):
        total_scores = [sum(student) for student in room]
        best_student = total_scores.index(max(total_scores)) + 1
        print(f"ห้อง {r+1}: นักเรียนที่คะแนนรวมสูงสุดคือคนที่ {best_student}")
    
    # นับนักเรียนที่ผ่านทุกวิชาในแต่ละห้อง (คะแนนผ่าน >= 50)
    pass_counts = [sum(1 for student in room if all(sub >= 50 for sub in student)) for room in scores]
    print(f"จำนวนนักเรียนที่สอบผ่านทุกวิชาในแต่ละห้อง: {pass_counts}")

# climate_data()  # ใช้เมื่อต้องการรันโปรแกรมข้อมูลอุณหภูมิ
# warehouse_management()  # ใช้เมื่อต้องการรันโปรแกรมคลังสินค้า
# student_performance()  # ใช้เมื่อต้องการรันโปรแกรมผลการเรียน