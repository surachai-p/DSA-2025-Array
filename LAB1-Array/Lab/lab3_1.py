# ข้อมูลอุณหภูมิ (3 เมือง, 4 ครั้งต่อวัน, 7 วัน)
temperatures = {
    "เมือง1": [
        [30, 32, 34, 33],  # วัน 1
        [29, 31, 33, 32],  # วัน 2
        [28, 30, 32, 31],  # วัน 3
        [31, 33, 35, 34],  # วัน 4
        [29, 30, 32, 31],  # วัน 5
        [30, 32, 33, 34],  # วัน 6
        [31, 33, 34, 32]   # วัน 7
    ],
    "เมือง2": [
        [25, 26, 27, 28],  # วัน 1
        [24, 25, 27, 28],  # วัน 2
        [23, 25, 26, 27],  # วัน 3
        [26, 27, 28, 29],  # วัน 4
        [24, 25, 26, 27],  # วัน 5
        [25, 26, 27, 28],  # วัน 6
        [24, 25, 26, 27]   # วัน 7
    ],
    "เมือง3": [
        [22, 24, 25, 26],  # วัน 1
        [21, 23, 25, 26],  # วัน 2
        [20, 22, 24, 25],  # วัน 3
        [23, 24, 26, 27],  # วัน 4
        [22, 23, 24, 25],  # วัน 5
        [21, 23, 24, 26],  # วัน 6
        [22, 23, 25, 27]   # วัน 7
    ]
}

# ฟังก์ชันหาค่าเฉลี่ยอุณหภูมิของเมือง
def calculate_average(city_temps):
    total = 0
    count = 0
    for day in city_temps:
        total += sum(day)
        count += len(day)
    return total / count

# ฟังก์ชันหาวันและเวลาที่อุณหภูมิสูงที่สุดของเมือง
def find_max_temperature_day_and_time(city_temps):
    max_temp = float('-inf')
    max_day = -1
    max_time = -1
    for day_index, day in enumerate(city_temps):
        for time_index, temp in enumerate(day):
            if temp > max_temp:
                max_temp = temp
                max_day = day_index + 1  # วันเริ่มต้นที่ 1
                max_time = time_index + 1  # เวลาวัดเริ่มต้นที่ 1
    return max_temp, max_day, max_time

# แสดงผลลัพธ์
for city, city_temps in temperatures.items():
    # ค่าเฉลี่ยอุณหภูมิ
    avg_temp = calculate_average(city_temps)
    # วันและเวลาที่อุณหภูมิสูงที่สุด
    max_temp, max_day, max_time = find_max_temperature_day_and_time(city_temps)
    
    print(f"{city}:")
    print(f"  ค่าเฉลี่ยอุณหภูมิ: {avg_temp:.2f}°C")
    print(f"  อุณหภูมิสูงที่สุด: {max_temp}°C ที่วันที่ {max_day}, เวลาที่ {max_time}")
    print()
