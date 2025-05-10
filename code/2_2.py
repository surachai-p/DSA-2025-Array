seat = [
    ["o", "o", "o"],
    ["o", "o", "o"],
    ["o", "o", "o"]
]

for row in seat:
    print(row)

while True:
    f = int(input("กด 1 จอง\nกด 2 ยกเลิกการจอง\nกด 3 แสดงจำนวนที่นั่งว่างทั้งหมด\nกด 4 ออกโปรแกรม\n"))
    if f == 1:
        i, j = map(int, input("เลือกที่นั่ง (แถว คอลัมน์): ").split())
        seat[i][j] = "x"
    elif f ==2:
        i, j = map(int, input("เลือกที่นั่ง (แถว คอลัมน์): ").split())
        seat[i][j] = "o"
    elif f ==3:
        num = 0
        for row in seat:
            num += sum(1 for i in row if "o" in row)
        print(f"จำนวนที่นั่งว่าง: {num}")
    elif f ==4:
        break
    for row in seat:
        print(row)