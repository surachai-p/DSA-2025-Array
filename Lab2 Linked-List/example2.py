# สร้าง Node class
class Node:
    def __init__(self, data):
        self.data = data  # ข้อมูลที่เก็บใน Node
        self.next = None  # ตัวชี้ไปยัง Node ถัดไป
        self.prev = None  # ตัวชี้ไปยัง Node ก่อนหน้า

# สร้าง Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # ตัวชี้ไปยัง Node แรก
        self.tail = None  # ตัวชี้ไปยัง Node สุดท้าย

    # ฟังก์ชันเพื่อเพิ่ม Node ที่ท้ายของรายการ
    def append(self, data):
        new_node = Node(data)  # สร้าง Node ใหม่
        if self.tail is None:  # ถ้ารายการว่าง
            self.head = new_node  # ให้ head ชี้ไปยัง Node ใหม่
            self.tail = new_node  # ให้ tail ชี้ไปยัง Node ใหม่
        else:
            self.tail.next = new_node  # ให้ Node สุดท้ายชี้ไปยัง Node ใหม่
            new_node.prev = self.tail  # ให้ Node ใหม่ชี้กลับไปยัง Node สุดท้าย
            self.tail = new_node  # ให้ tail ชี้ไปยัง Node ใหม่

    # ฟังก์ชันเพื่อแสดงข้อมูลทั้งหมดใน Doubly Linked List
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> " if current.next else "")
            current = current.next
        print()  # เพื่อให้แสดงผลในบรรทัดใหม่

    # ฟังก์ชันเพื่อเพิ่ม Node ที่ตำแหน่งแรก
    def prepend(self, data):
        new_node = Node(data)  # สร้าง Node ใหม่
        if self.head is None:  # ถ้ารายการว่าง
            self.head = new_node  # ให้ head ชี้ไปยัง Node ใหม่
            self.tail = new_node  # ให้ tail ชี้ไปยัง Node ใหม่
        else:
            new_node.next = self.head  # ให้ Node ใหม่ชี้ไปยัง Node แรก
            self.head.prev = new_node  # ให้ Node แรกชี้กลับไปยัง Node ใหม่
            self.head = new_node  # ให้ head ชี้ไปยัง Node ใหม่

    # ฟังก์ชันเพื่อลบ Node ที่ท้ายรายการ
    def delete_tail(self):
        if self.tail is None:  # ถ้ารายการว่าง
            print("The list is empty!")
            return
        if self.head == self.tail:  # ถ้ามี Node เดียว
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev  # ให้ tail ชี้ไปยัง Node ก่อนหน้า
            self.tail.next = None  # ทำให้ตัวชี้ next ของ Node ล่าสุดเป็น None

    # ฟังก์ชันเพื่อลบ Node ที่ตำแหน่งแรก
    def delete_head(self):
        if self.head is None:  # ถ้ารายการว่าง
            print("The list is empty!")
            return
        if self.head == self.tail:  # ถ้ามี Node เดียว
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next  # ให้ head ชี้ไปยัง Node ถัดไป
            self.head.prev = None  # ทำให้ตัวชี้ prev ของ Node แรกเป็น None

    # ฟังก์ชันเพื่อค้นหา Node ที่มีค่าตรงกับที่กำหนด
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

# ทดสอบการใช้งาน
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)

print("Doubly Linked List:")
dll.display()

dll.prepend(5)
print("After prepending 5:")
dll.display()

dll.delete_tail()
print("After deleting tail:")
dll.display()

dll.delete_head()
print("After deleting head:")
dll.display()

# ค้นหาค่าภายในรายการ
if dll.search(20):
    print("20 is in the list.")
else:
    print("20 is not in the list.")