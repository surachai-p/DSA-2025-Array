# รายชื่อเมือง
cities = ["กรุงเทพฯ", "เชียงใหม่", "ภูเก็ต"]

# ช่วงเวลาในแต่ละวัน
times = ["เช้า", "เที่ยง", "บ่าย", "เย็น"]

# สร้างข้อมูลอุณหภูมิ [เมือง][วัน][เวลา]
import random

temperatures = [[[random.randint(20, 40) for _ in range(4)] for _ in range(7)] for _ in range(3)]

# หาค่าเฉลี่ยอุณหภูมิของแต่ละเมือง
for city_index, city in enumerate(cities):
    total_temp = 0
    count = 0
    for day in range(7):
        for time in range(4):
            total_temp += temperatures[city_index][day][time]
            count += 1
    avg_temp = total_temp / count
    print(f"เมือง {city} มีอุณหภูมิเฉลี่ย {avg_temp:.2f} องศา")

print()

# หาวันและเวลาที่อุณหภูมิสูงที่สุดของแต่ละเมือง
for city_index, city in enumerate(cities):
    max_temp = -999
    max_day = -1
    max_time = -1
    for day in range(7):
        for time in range(4):
            temp = temperatures[city_index][day][time]
            if temp > max_temp:
                max_temp = temp
                max_day = day
                max_time = time
    print(f"เมือง {city} มีอุณหภูมิสูงสุด {max_temp} องศา ในวัน {max_day+1} ช่วง {times[max_time]}")

print()

# แสดงข้อมูลอุณหภูมิทั้งหมด (optional)
for city_index, city in enumerate(cities):
    print(f"\nข้อมูลอุณหภูมิของเมือง {city}:")
    for day in range(7):
        temps_in_day = ", ".join(f"{times[time]}: {temperatures[city_index][day][time]}°C" for time in range(4))
        print(f"  วัน {day+1}: {temps_in_day}")
