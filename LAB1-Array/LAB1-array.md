# ใบงานการทดลอง: การใช้งาน Array ในภาษา Python
## วัตถุประสงค์
1. เพื่อเรียนรู้การสร้างและใช้งาน Array 1 มิติ
2. เพื่อเรียนรู้การสร้างและใช้งาน Array 2 มิติ
3. เพื่อเรียนรู้การสร้างและใช้งาน Array 3 มิติ
4. เพื่อฝึกการประยุกต์ใช้ Array ในการแก้ปัญหาต่างๆ

## อุปกรณ์ที่ใช้
1. เครื่องคอมพิวเตอร์
2. Python 3.x
3. Text Editor หรือ IDE ที่ใช้เขียน Python

## การทดลองที่ 1: Array 1 มิติ
### ขั้นตอนการทดลอง

#### 1.1 การสร้างและแสดงผล Array
```python
# วิธีที่ 1: สร้าง Array แบบกำหนดค่าเริ่มต้น
numbers = [1, 2, 3, 4, 5]
print("Array 1:", numbers)

# วิธีที่ 2: สร้าง Array ว่าง
empty_array = []
print("Array ว่าง:", empty_array)

# วิธีที่ 3: สร้าง Array ด้วย list comprehension
squares = [x**2 for x in range(5)]
print("Array กำลังสอง:", squares)
```

#### 1.2 การเข้าถึงและแก้ไขข้อมูล
```python
fruits = ["แอปเปิล", "กล้วย", "ส้ม", "มะม่วง", "องุ่น"]

# การเข้าถึงข้อมูล
print("ผลไม้ชิ้นแรก:", fruits[0])
print("ผลไม้ชิ้นสุดท้าย:", fruits[-1])
print("ผลไม้ชิ้นที่ 2-4:", fruits[1:4])

# การแก้ไขข้อมูล
fruits[1] = "สตรอเบอร์รี่"
print("Array หลังการแก้ไข:", fruits)
```

#### 1.3 การดำเนินการพื้นฐาน
```python
numbers = [1, 2, 3, 4, 5]

# การเพิ่มข้อมูล
numbers.append(6)
print("หลังจาก append:", numbers)

numbers.insert(0, 0)
print("หลังจาก insert:", numbers)

# การลบข้อมูล
numbers.pop()
print("หลังจาก pop:", numbers)

numbers.remove(3)
print("หลังจาก remove 3:", numbers)

# การค้นหาข้อมูล
print("ตำแหน่งของ 4:", numbers.index(4))
print("จำนวน 2 ในarray:", numbers.count(2))
```

### แบบฝึกหัดที่ 1: Array 1 มิติ

#### 1. จงเขียนโปรแกรมสร้าง Array เก็บคะแนนสอบของนักเรียน 5 คน และ:
   - หาค่าเฉลี่ย
   - หาคะแนนสูงสุดและต่ำสุด
   - แสดงจำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย
#### Run
![Screenshot 2024-12-10 125756](https://github.com/user-attachments/assets/dfc4891c-0c95-4913-947b-b37a6cc26699)

#### 2. สร้างโปรแกรมจัดการรายชื่อสินค้าในร้านค้า โดยมีฟังก์ชัน:
   - เพิ่มสินค้าใหม่
   - ลบสินค้าที่หมด
   - ค้นหาสินค้า
   - แสดงรายการสินค้าทั้งหมด
#### Run
![Screenshot 2024-12-10 130631](https://github.com/user-attachments/assets/581a10f3-a086-4cd5-a347-86acda8c7c8d)

## การทดลองที่ 2: Array 2 มิติ
### ขั้นตอนการทดลอง

#### 2.1 การสร้างและแสดงผล Array 2 มิติ
```python
# วิธีที่ 1: สร้างแบบกำหนดค่าโดยตรง
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# วิธีที่ 2: สร้างด้วย list comprehension
matrix2 = [[i+j for j in range(3)] for i in range(3)]

# การแสดงผล
print("Matrix 1:")
for row in matrix:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)
```

#### 2.2 การเข้าถึงและแก้ไขข้อมูล
```python
# การเข้าถึงข้อมูล
print("ข้อมูลแถวที่ 1:", matrix[0])
print("ข้อมูลแถวที่ 2 คอลัมน์ที่ 3:", matrix[1][2])

# การแก้ไขข้อมูล
matrix[1][1] = 10
print("\nMatrix หลังการแก้ไข:")
for row in matrix:
    print(row)

# การแก้ไขทั้งแถว
matrix[0] = [10, 20, 30]
print("\nMatrix หลังการแก้ไขทั้งแถว:")
for row in matrix:
    print(row)
```

#### 2.3 การดำเนินการพื้นฐาน
```python
# การหาผลรวมแต่ละแถว
row_sums = [sum(row) for row in matrix]
print("ผลรวมแต่ละแถว:", row_sums)

# การหาผลรวมแต่ละคอลัมน์
col_sums = [sum(col) for col in zip(*matrix)]
print("ผลรวมแต่ละคอลัมน์:", col_sums)

# การสลับแถว
matrix[0], matrix[1] = matrix[1], matrix[0]
print("\nMatrix หลังการสลับแถว:")
for row in matrix:
    print(row)
```

### แบบฝึกหัดที่ 2: Array 2 มิติ

#### 1. จงเขียนโปรแกรมจัดการคะแนนสอบ:
   - เก็บคะแนนสอบ 3 วิชาของนักเรียน 4 คน
   - คำนวณคะแนนเฉลี่ยของแต่ละวิชา
   - หานักเรียนที่ได้คะแนนรวมสูงสุด
   - แสดงจำนวนนักเรียนที่สอบผ่านแต่ละวิชา (คะแนนผ่าน ≥ 50)
#### Run
![Screenshot 2024-12-10 131513](https://github.com/user-attachments/assets/ace15dc9-564f-47eb-ae72-8cd2df6495eb)

#### 2. สร้างโปรแกรมจัดการที่นั่งในโรงภาพยนตร์:
   - แสดงแผนผังที่นั่ง (ว่าง/จอง)
   - จองที่นั่ง
   - ยกเลิกการจอง
   - แสดงจำนวนที่นั่งว่างทั้งหมด
#### Run
![Screenshot 2024-12-10 132502](https://github.com/user-attachments/assets/e84ab86e-d9e8-485d-8461-acbfb7c759f6)
![Screenshot 2024-12-10 132514](https://github.com/user-attachments/assets/f8e23ce8-0859-4912-b89d-6654ad3405f3)

## การทดลองที่ 3: Array 3 มิติ
### ขั้นตอนการทดลอง

#### 3.1 การสร้างและแสดงผล Array 3 มิติ
```python
# วิธีที่ 1: สร้างแบบกำหนดค่าโดยตรง
cube = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

# วิธีที่ 2: สร้างด้วย list comprehension
cube2 = [[[k+j+i for k in range(2)] for j in range(2)] for i in range(2)]

# การแสดงผล
print("Cube 1:")
for layer in cube:
    for row in layer:
        print(row)
    print()
```

#### 3.2 การเข้าถึงและแก้ไขข้อมูล
```python
# การเข้าถึงข้อมูล
print("ข้อมูลชั้นที่ 1:", cube[0])
print("ข้อมูลชั้นที่ 1 แถวที่ 2:", cube[0][1])
print("ข้อมูลที่ตำแหน่ง [0][1][0]:", cube[0][1][0])

# การแก้ไขข้อมูล
cube[0][0][0] = 10
print("\nCube หลังการแก้ไข:")
for layer in cube:
    for row in layer:
        print(row)
    print()
```

### แบบฝึกหัดที่ 3: Array 3 มิติ

#### 1. จงเขียนโปรแกรมจัดการข้อมูลอุณหภูมิ:
   - เก็บอุณหภูมิของ 3 เมือง
   - วัด 4 ครั้งต่อวัน
   - เป็นเวลา 7 วัน
   - หาค่าเฉลี่ยอุณหภูมิของแต่ละเมือง
   - หาวันและเวลาที่อุณหภูมิสูงที่สุดของแต่ละเมือง
#### Run
![Screenshot 2024-12-10 134955](https://github.com/user-attachments/assets/bc319b7e-e442-4820-b3df-4411aeddacbc)
![Screenshot 2024-12-10 135019](https://github.com/user-attachments/assets/a3f31a8c-4c6e-46df-80c9-2cacb9b13d16)
![Screenshot 2024-12-10 135034](https://github.com/user-attachments/assets/04f16de2-f3d4-4a5c-bff8-919c17ad93f2)
![Screenshot 2024-12-10 135043](https://github.com/user-attachments/assets/da854a82-0eb5-4f29-abc0-5da64e260ef9)

#### 2. เขียนโปรแกรมวิเคราะห์ผลการเรียน:
   - เก็บคะแนนของนักเรียน 3 ห้อง
   - ห้องละ 5 คน
   - สอบ 4 วิชา
   - หาห้องที่มีคะแนนเฉลี่ยสูงสุด
   - หานักเรียนที่ได้คะแนนรวมสูงสุดในแต่ละห้อง
   - แสดงจำนวนนักเรียนที่สอบผ่านทุกวิชาในแต่ละห้อง
#### Run
![Screenshot 2024-12-10 140400](https://github.com/user-attachments/assets/0e67a690-981f-4b96-9be4-3e51dc88ab9e)
![Screenshot 2024-12-10 140417](https://github.com/user-attachments/assets/930a3875-c7dc-44ed-973d-6bba2573cf7b)
![Screenshot 2024-12-10 140345](https://github.com/user-attachments/assets/ce582ad0-d826-40a3-87df-388b0377486f)

## การส่งงาน
1. ส่งไฟล์ .py ที่มีโค้ดการทดลอง
2. แสดงผลลัพธ์การทำงานของโปรแกรมในแต่ละการทดลอง


