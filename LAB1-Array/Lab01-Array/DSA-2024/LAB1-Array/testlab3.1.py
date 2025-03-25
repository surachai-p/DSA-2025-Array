##จงเขียนโปรแกรมจัดการข้อมูลอุณหภูมิ:
#เก็บอุณหภูมิของ 3 เมือง
#วัด 4 ครั้งต่อวัน
#เป็นเวลา 7 วัน
#หาค่าเฉลี่ยอุณหภูมิของแต่ละเมือง
#หาวันและเวลาที่อุณหภูมิสูงที่สุดของแต่ละเมือง

import random
#คำนวณค่าเฉลี่ยอุณหภูมิของแต่ละเมือง
def calculate_average_temperature(temperature_data):
    averages = []
    for city_data in temperature_data:
        total_temp = 0
        count = 0
        for day in city_data:
            for temp in day:
                total_temp += temp
                count += 1
        averages.append(total_temp / count)
    return averages

#หาวันและเวลาที่อุณหภูมิสูงสุดของแต่ละเมือง
def find_max_temperature_day_and_time(temperature_data):
    max_temps, max_days, max_times = [], [], []
    for city_data in temperature_data:
        max_temp = float('-inf')
        for day_index, day in enumerate(city_data):
            for time_index, temp in enumerate(day):
                if temp > max_temp:
                    max_temp = temp
                    max_day = day_index
                    max_time = time_index
        max_temps.append(max_temp)
        max_days.append(max_day)
        max_times.append(max_time)
    return max_temps, max_days, max_times

# กำหนดข้อมูลอุณหภูมิของ 3 เมือง
cities = ["เมือง A", "เมือง B", "เมือง C"]
days = 7  # จำนวนวันที่บันทึก
times_per_day = 4  # จำนวนครั้งในการวัดอุณหภูมิต่อวัน

# สร้างข้อมูลแบบสุ่มอุณหภูมิ 3 เมือง(7 วัน x 4 เวลา)
temperature_data = [[[random.uniform(30, 70) for _ in range(times_per_day)] for _ in range(days)] for _ in range(3)]

# คำนวณค่าเฉลี่ยอุณหภูมิ
averages = calculate_average_temperature(temperature_data)

# หาวันและเวลาที่อุณหภูมิสูงสุด
max_temps, max_days, max_times = find_max_temperature_day_and_time(temperature_data)

for i, city in enumerate(cities):
    print(f"\n{city}:")
    print(f"  ค่าเฉลี่ยอุณหภูมิ: {averages[i]:.2f} °C")
    print(f"  อุณหภูมิสูงสุด: {max_temps[i]:.2f} °C")
    print(f"  วันที่ที่มีอุณหภูมิสูงสุด: วันที่ {max_days[i] + 1}")
    print(f"  เวลาที่มีอุณหภูมิสูงสุด: เวลา {max_times[i] + 1} น.")