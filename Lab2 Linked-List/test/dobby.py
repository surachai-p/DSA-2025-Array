
# Initialise the Node
class Node:
    def __init__(self, data):
        self.item = data
        self.next = None #address ไปยังด้านหน้า
        self.prev = None #address ไปยังด้านหลัง

class doublyLinkedList:
    def __init__(self):
        self.start_node = None

    def InsertToEmptyList(self, data):
        if self.start_node is None:  #ตรวจสอบว่าลิสต์ว่างเปล่าหรือไม่
            new_node = Node(data) #สร้างโหนดใหม่
            self.start_node = new_node #กำหนดให้โหนดใหม่นี้เป็นโหนดเริ่มต้น
        else:
            print("The list is empty") # แจ้งเตือนหากลิสต์ไม่ว่างเปล่า

    def InsertToEnd(self, data): #การเพิ่มข้อมูลในตำแหน่งท้าย
        if self.start_node is None: #ตรวจสอบว่าลิสต์ว่างเปล่าหรือไม่
            new_node = Node(data)#สร้างโหนดใหม่
            self.start_node = new_node #กำหนดให้โหนดใหม่นี้เป็นโหนดเริ่มต้น
            return
        n = self.start_node

        while n.next is not None: #เดินทางไปยังโหนดถัดไปทีละขั้น
            n = n.next #ลูปจะหยุดเมื่อถึงโหนดสุดท้าย ซึ่งมีค่าเป็น None
        new_node = Node(data) #สร้างโหนดใหม่พร้อมข้อมูลที่ต้องการเพิ่ม
        n.next = new_node #เชื่อมโหนดสุดท้ายเข้ากับโหนดใหม่ทางด้าน next
        new_node.prev = n #เชื่อมโหนดใหม่กลับมายังโหนดสุดท้ายทางด้าน prev

    def InsertBefore(self, target_data, new_data):
        if self.start_node is None:
            print("The list is empty")
            return
        # ค้นหาโหนดที่มีค่าเท่ากับ target_data
        n = self.start_node
        while n is not None:
            if n.item == target_data:
                break
            n = n.next
    
        if n is None:
            print(f"Node with data {target_data} not found")
            return

        # สร้างโหนดใหม่
        new_node = Node(new_data)
        new_node.next = n
        new_node.prev = n.prev

        if n.prev is not None:# ปรับลิงก์ของโหนดก่อนหน้า (ถ้ามี)
            n.prev.next = new_node
        else:
            self.start_node = new_node
        n.prev = new_node# ปรับลิงก์ของโหนดปัจจุบัน


    # การลบข้อมูลจากจุดเริ่มต้น
    def DeleteAtStart(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next #เปลี่ยนจุดเริ่มต้น (start_node) ไปยังโหนดถัดไป (self.start_node.next)
        self.start_prev = None; #ตั้งค่า prev ของโหนดใหม่ให้เป็น None (ยกเลิกการเชื่อมโยงกับโหนดที่ถูกลบ)
    
    # การลบข้อมูลจากจุดท้าย Delete the elements from the end
    def delete_at_end(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.start_node.next is None:
            self.start_node = None #ใช้เมื่อลิสต์มีโหนดเดียว เพื่อทำให้ start_node ไม่ชี้ไปยังโหนดใด ๆ อีก
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None  #ยกเลิกการเชื่อมโยงจากโหนดก่อนหน้ามายังโหนดสุดท้าย


    def Display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Element is: ", n.item)
                n = n.next
        print("\n")
        
# สร้าง Doubly Linked List
dll = doublyLinkedList()

# เพิ่มข้อมูลในลิสต์ว่างเปล่า
dll.InsertToEmptyList(1)

# เพิ่มข้อมูลที่ปลายลิสต์
dll.InsertToEnd(2)
dll.InsertToEnd(3)

# เพิ่มข้อมูลก่อนโหนด
dll.InsertBefore(1, 0)
print("List after inserting 0 before 1:")
dll.Display()

# แสดงข้อมูลในลิสต์
print("List after insertion:")
dll.Display()

# ลบข้อมูลที่จุดเริ่มต้น
dll.DeleteAtStart()
print("List after deleting at start:")
dll.Display()

# ลบข้อมูลที่ปลายลิสต์
dll.delete_at_end()
print("List after deleting at end:")
dll.Display()
