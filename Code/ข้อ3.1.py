# กำหนดข้อมูลอุณหภูมิ (ให้ผู้ใช้กรอกข้อมูล)
temperatures = {}

def input_temperatures():
    print("กรุณากรอกอุณหภูมิสำหรับ 3 เมือง (วันอาทิตย์-จันทร์, 4 ครั้งต่อวัน):")
    days_of_week = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
    
    for city in ["เมือง A", "เมือง B", "เมือง C"]:
        print(f"\n{city}:")
        days = []
        for day in days_of_week:
            print(f"  {day}:")
            times = [float(input(f"    เวลา {time}: ")) for time in ["06:00", "10:00", "14:00", "18:00"]]
            days.append(times)
        temperatures[city] = days

# คำนวณค่าเฉลี่ยอุณหภูมิของแต่ละเมือง
def calculate_averages():
    print("\nค่าเฉลี่ยอุณหภูมิของแต่ละเมือง:")
    for city, days in temperatures.items():
        avg = sum(sum(day) for day in days) / (len(days) * 4)
        print(f"{city}: {avg:.2f} °C")

# หาวันและเวลาที่อุณหภูมิสูงที่สุดของแต่ละเมือง
def find_highest_temperature():
    print("\nวันและเวลาที่อุณหภูมิสูงที่สุดของแต่ละเมือง:")
    for city, days in temperatures.items():
        max_temp, max_day, max_time = -float('inf'), 0, 0
        days_of_week = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
        for day_index, day in enumerate(days):
            for time_index, temp in enumerate(day):
                if temp > max_temp:
                    max_temp = temp
                    max_day, max_time = day_index, time_index
        print(f"{city}: สูงสุด {max_temp} °C ({days_of_week[max_day]}, เวลา {['06:00', '10:00', '14:00', '18:00'][max_time]})")

# เมนูหลัก
def menu():
    input_temperatures()
    while True:
        print("\n--- ระบบจัดการข้อมูลอุณหภูมิ ---")
        print("1. แสดงค่าเฉลี่ยอุณหภูมิของแต่ละเมือง")
        print("2. แสดงวันและเวลาที่อุณหภูมิสูงที่สุดของแต่ละเมือง")
        print("3. ออกจากโปรแกรม")
        
        choice = input("กรุณาเลือกเมนู (1-3): ")
        if choice == '1':
            calculate_averages()
        elif choice == '2':
            find_highest_temperature()
        elif choice == '3':
            print("ออกจากโปรแกรม")
            break
        else:
            print("เลือกเมนูไม่ถูกต้อง กรุณาเลือกใหม่")

# เรียกใช้งานเมนูหลัก
menu()

