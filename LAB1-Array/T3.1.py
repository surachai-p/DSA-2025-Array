import numpy as np

# กำหนดขนาดของ array
num_cities = 3
measurements_per_day = 4
num_days = 7

# สร้าง array 3 มิติเพื่อเก็บข้อมูลอุณหภูมิ
temperatures = np.zeros((num_cities, measurements_per_day, num_days))

# กรอกข้อมูลอุณหภูมิ (ตัวอย่าง)
for city in range(num_cities):
    for measurement in range(measurements_per_day):
        for day in range(num_days):
            temperatures[city][measurement][day] = float(input(f"กรอกอุณหภูมิเมืองที่ {city+1} ครั้งที่ {measurement+1} วันที่ {day+1}: "))

# คำนวณค่าเฉลี่ยอุณหภูมิของแต่ละเมือง
average_temps = np.mean(temperatures, axis=(1, 2))
print("ค่าเฉลี่ยอุณหภูมิของแต่ละเมือง:")
for i, avg_temp in enumerate(average_temps):
    print(f"เมืองที่ {i+1}: {avg_temp:.2f} องศา")

# หาวันและเวลาที่อุณหภูมิสูงสุดของแต่ละเมือง
max_indices = np.argmax(temperatures, axis=(1, 2))
for city, index in enumerate(max_indices):
    row, col = divmod(index, measurements_per_day)
    print(f"เมืองที่ {city+1} อุณหภูมิสูงสุด: {temperatures[city][row][col]} องศา")
    print(f"  วันที่: {col+1}, เวลา: {row+1}")