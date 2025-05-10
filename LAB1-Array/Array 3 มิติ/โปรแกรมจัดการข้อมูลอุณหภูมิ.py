
import random

temperatures = [
    [[random.randint(20, 40) for _ in range(4)] for _ in range(7)] for _ in range(3)
]

average_temps = [sum(sum(day) for day in city) / (7 * 4) for city in temperatures]

highest_temp_info = []
for city in temperatures:
    max_temp = max(max(day) for day in city)
    for day_idx, day in enumerate(city):
        if max_temp in day:
            time_idx = day.index(max_temp)
            highest_temp_info.append((max_temp, day_idx + 1, time_idx + 1))
            break

for city_idx, (avg, (temp, day, time)) in enumerate(zip(average_temps, highest_temp_info)):
    print(f"เมือง {city_idx + 1}:")
    print(f"  ค่าเฉลี่ยอุณหภูมิ: {avg:.2f}°C")
    print(f"  อุณหภูมิสูงสุด: {temp}°C (วันที่ {day}, เวลา {time})")
