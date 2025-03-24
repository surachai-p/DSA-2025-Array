# สร้าง List สำหรับเก็บรายชื่อสินค้า
products = []

# ฟังก์ชันเพิ่มสินค้าใหม่
def add_product():
    product = input("กรุณากรอกชื่อสินค้าที่ต้องการเพิ่ม: ")
    products.append(product)
    print(f"เพิ่มสินค้า '{product}' เรียบร้อยแล้ว\n")

# ฟังก์ชันลบสินค้าที่หมด
def remove_product():
    product = input("กรุณากรอกชื่อสินค้าที่ต้องการลบ: ")
    if product in products:
        products.remove(product)
        print(f"ลบสินค้า '{product}' เรียบร้อยแล้ว\n")
    else:
        print(f"ไม่พบสินค้า '{product}' ในรายการ\n")

# ฟังก์ชันค้นหาสินค้า
def search_product():
    product = input("กรุณากรอกชื่อสินค้าที่ต้องการค้นหา: ")
    if product in products:
        print(f"พบสินค้า '{product}' ในรายการ\n")
    else:
        print(f"ไม่พบสินค้า '{product}' ในรายการ\n")

# ฟังก์ชันแสดงรายการสินค้าทั้งหมด
def show_products():
    if products:
        print("รายการสินค้าทั้งหมด:")
        for idx, product in enumerate(products, 1):
            print(f"{idx}. {product}")
        print()
    else:
        print("ไม่มีสินค้าในร้านขณะนี้\n")

# เมนูหลัก
while True:
    print("=== ร้านค้าจัดการสินค้า ===")
    print("1. เพิ่มสินค้าใหม่")
    print("2. ลบสินค้าที่หมด")
    print("3. ค้นหาสินค้า")
    print("4. แสดงรายการสินค้าทั้งหมด")
    print("5. ออกจากโปรแกรม")
    
    choice = input("กรุณาเลือกเมนู (1-5): ")
    print()
    
    if choice == "1":
        add_product()
    elif choice == "2":
        remove_product()
    elif choice == "3":
        search_product()
    elif choice == "4":
        show_products()
    elif choice == "5":
        print("ออกจากโปรแกรมเรียบร้อยแล้ว")
        break
    else:
        print("กรุณาเลือกเมนูให้ถูกต้อง (1-5)\n")