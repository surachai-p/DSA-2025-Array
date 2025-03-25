
temperatures = [[[30, 32, 31, 33], [29, 31, 30, 32], [28, 30, 29, 31], [27, 29, 28, 30], 
                 [26, 28, 27, 29], [25, 27, 26, 28], [24, 26, 25, 27]],  # เมือง 1
                [[32, 34, 33, 35], [31, 33, 32, 34], [30, 32, 31, 33], [29, 31, 30, 32], 
                 [28, 30, 29, 31], [27, 29, 28, 30], [26, 28, 27, 29]],  # เมือง 2
                [[25, 27, 26, 28], [24, 26, 25, 27], [23, 25, 24, 26], [22, 24, 23, 25], 
                 [21, 23, 22, 24], [20, 22, 21, 23], [19, 21, 20, 22]]]  # เมือง 3


averages = [sum(sum(day) for day in city) / (7 * 4) for city in temperatures]
print("ค่าเฉลี่ยอุณหภูมิของแต่ละเมือง:", averages)


for i, city in enumerate(temperatures):
    max_temp = max(max(day) for day in city)
    max_day, max_time = next((d+1, t+1) for d, day in enumerate(city) for t, temp in enumerate(day) if temp == max_temp)
    print(f"เมือง {i+1}: อุณหภูมิสูงสุด {max_temp} ที่วัน {max_day} เวลา {max_time}")
