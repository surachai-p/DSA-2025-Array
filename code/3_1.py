import random

temperatures = [[[random.randint(20, 40) for _ in range(4)] for _ in range(7)] for _ in range(3)]

for layer in temperatures:
    for row in layer:
        print(row)
    print()

city_averages = [sum(sum(day) for day in city) / (4 * 7) for city in temperatures]
print("ค่าเฉลี่ยอุณหภูมิของแต่ละเมือง:", [f"{avg:.3f}" for avg in city_averages])

for city_index, city in enumerate(temperatures):
    max_temp = 0
    max_day, max_time = 0, 0
    for day_index, day in enumerate(city):
        for time_index, temp in enumerate(day):
            if temp > max_temp:
                max_temp = temp
                max_day = day_index
                max_time = time_index
    print(f"เมืองที่ {city_index+1}: อุณหภูมิสูงสุด {max_temp} องศา (วัน {max_day+1}, เวลา {max_time+1})")