class Node :
    def __init__(self,data):
        self.data = data 
        self.next = None
class Linklist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_n = Node(data) #สร้าง Node ใหม่
        if not self.head: #ถ้า List ว่าง 
            self.head = new_n #ให้ head ชี้ไปที่ Node ใหม่
            return  
        current = self.head # เริ่มที่โหนดแรกของลิสต์
        while current.next: # หาโหนดสุดท้าย
            current = current.next
        current.next = new_n # เชื่อมโหนดใหม่เข้ากับโหนดสุดท้าย

    def prepend(self,data):
        new_node = Node(data) #สร้าง Node ใหม่
        new_node.next = self.head #ให้ Node ใหม่ชี้ไปที่ head เดิม
        self.head = new_node #เปลี่ยน head ให้ชี้มาที่ Node ใหม่

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, key):
        current = self.head
        position = 0
        while current:
            if current.data == key:
                return position
            current = current.next
            position += 1
        return -1

    def count_nodes(llist):
        count = 0
        current = llist.head
        while current:
            count += 1
            current = current.next
        return count
    
    def delete(self, key):
        current = self.head
    
        if current and current.data == key:
         self.head = current.next
         return

        while current and current.next:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next

#Function
#1.append
#2.prepend
#3.display 
#4.search
#5.count_nodes
#6.delete

print("1. เพิ่มข้อมูล 1, 2, 3 ที่ท้าย List")
ll = Linklist()
ll.append (0)
ll.append(1)
ll.append(2)
ll.append(3)
print("ผลลัพธ์:")
ll.display()

print("\n2. เพิ่มข้อมูล 0 ที่หน้า List")
ll.prepend(-1)
ll.prepend(-2)
ll.prepend("ไรวะ")
print("ผลลัพธ์:")
ll.display()

print("\n3. ลบข้อมูล")
ll.delete("ไรวะ")
print("ผลลัพธ์:")
ll.display()

print("\n4. แสดงจำนวน Node ทั้งหมด")
print(f"จำนวน Node ทั้งหมด: {ll.count_nodes()}")