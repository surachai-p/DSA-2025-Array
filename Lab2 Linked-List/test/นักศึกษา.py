class Node:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.next = None


class StudentLinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, student_id, name, grade):
        """เพิ่มข้อมูลนักศึกษา"""
        new_node = Node(student_id, name, grade)
        if not self.head or self.head.student_id > student_id:  # เพิ่มที่หัวหากรหัสเล็กกว่า
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next and current.next.student_id < student_id:  # หาโหนดก่อนตำแหน่งที่เหมาะสม
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_student(self, student_id):
        """ลบข้อมูลนักศึกษาตามรหัส"""
        current = self.head
        if not current:  # ลิสต์ว่าง
            print(f"ไม่มีนักศึกษาที่มีรหัส {student_id}")
            return
        if current.student_id == student_id:  # ลบที่หัวลิสต์
            self.head = current.next
            print(f"ลบนักศึกษารหัส {student_id} สำเร็จ")
            return
        while current.next and current.next.student_id != student_id:  # หาโหนดก่อนนักศึกษาที่ต้องการลบ
            current = current.next
        if current.next:  # พบโหนดที่ต้องการลบ
            current.next = current.next.next
            print(f"ลบนักศึกษารหัส {student_id} สำเร็จ")
        else:  # ไม่พบรหัสนักศึกษา
            print(f"ไม่มีนักศึกษาที่มีรหัส {student_id}")

    def search_student(self, student_id):
        """ค้นหานักศึกษาตามรหัส"""
        current = self.head
        while current:
            if current.student_id == student_id:
                print(f"รหัส: {current.student_id}, ชื่อ: {current.name}, เกรด: {current.grade}")
                return
            current = current.next
        print(f"ไม่มีนักศึกษาที่มีรหัส {student_id}")

    def display_students(self):
        """แสดงรายชื่อนักศึกษาทั้งหมด"""
        if not self.head:
            print("ไม่มีข้อมูลนักศึกษา")
            return
        print("รายชื่อนักศึกษา:")
        current = self.head
        while current:
            print(f"รหัส: {current.student_id}, ชื่อ: {current.name}, เกรด: {current.grade}")
            current = current.next


# การใช้งาน
students = StudentLinkedList()

# เพิ่มข้อมูลนักศึกษา
students.add_student(101, "เอมมิเน้น", "A")
students.add_student(103, "ดิดดี้", "B")
students.add_student(102, "จัสตินบีเบอร์", "C")

# แสดงรายชื่อนักศึกษาทั้งหมด
students.display_students()

# ค้นหานักศึกษา
print("\nค้นหานักศึกษารหัส 102:")
students.search_student(102)

# ลบนักศึกษา
print("\nลบนักศึกษารหัส 101:")
students.delete_student(101)

# แสดงรายชื่อนักศึกษาหลังลบ
print("\nรายชื่อนักศึกษาหลังลบ:")
students.display_students()
