# ใบงานการทดลอง: การใช้งาน Array ในภาษา Python
## วัตถุประสงค์
##1. เพื่อเรียนรู้การสร้างและใช้งาน Array 1 มิติ
##2. เพื่อเรียนรู้การสร้างและใช้งาน Array 2 มิติ
##3. เพื่อเรียนรู้การสร้างและใช้งาน Array 3 มิติ
##4. เพื่อฝึกการประยุกต์ใช้ Array ในการแก้ปัญหาต่างๆ

## อุปกรณ์ที่ใช้
##1. เครื่องคอมพิวเตอร์
##2. Python 3.x
##3. Text Editor หรือ IDE ที่ใช้เขียน Python

## การทดลองที่ 1: Array 1 มิติ
### ขั้นตอนการทดลอง

#### 1.1 การสร้างและแสดงผล Array
# วิธีที่ 1: สร้าง Array แบบกำหนดค่าเริ่มต้น
numbers = [1, 2, 3, 4, 5]
print("Array 1:", numbers)

# วิธีที่ 2: สร้าง Array ว่าง
empty_array = []
print("Array ว่าง:", empty_array)

# วิธีที่ 3: สร้าง Array ด้วย list comprehension
squares = [x**2 for x in range(5)]
print("Array กำลังสอง:", squares)

#### 1.2 การเข้าถึงและแก้ไขข้อมูล
fruits = ["แอปเปิล", "กล้วย", "ส้ม", "มะม่วง", "องุ่น"]

# การเข้าถึงข้อมูล
print("ผลไม้ชิ้นแรก:", fruits[0])
print("ผลไม้ชิ้นสุดท้าย:", fruits[-1])
print("ผลไม้ชิ้นที่ 2-4:", fruits[1:4])

# การแก้ไขข้อมูล
fruits[1] = "สตรอเบอร์รี่"
print("Array หลังการแก้ไข:", fruits)

#### 1.3 การดำเนินการพื้นฐาน
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

