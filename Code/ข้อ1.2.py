# สร้างรายการสินค้าของร้าน
inventory = {}

# เพิ่มสินค้าใหม่
def add_product():
    name = input("ชื่อสินค้า: ")
    qty = int(input("จำนวน: "))
    price = float(input("ราคา: "))
    inventory[name] = {'quantity': qty, 'price': price}
    print(f"เพิ่ม {name} จำนวน {qty} ชิ้น ราคา {price:.2f} บาท")

# ลบสินค้าที่หมด
def remove_out_of_stock():
    for name in list(inventory.keys()):
        if inventory[name]['quantity'] == 0:
            del inventory[name]
            print(f"ลบ {name} เนื่องจากสินค้าหมด")

# ค้นหาสินค้า
def search_product():
    name = input("ค้นหาสินค้า: ")
    if name in inventory:
        print(f"{name}: {inventory[name]['quantity']} ชิ้น, {inventory[name]['price']:.2f} บาท")
    else:
        print(f"ไม่พบ {name}")

# แสดงสินค้าทั้งหมด
def show_all_products():
    if not inventory:
        print("ไม่มีสินค้า")
    else:
        print("รายการสินค้า:")
        for name, details in inventory.items():
            print(f"{name}: {details['quantity']} ชิ้น, {details['price']:.2f} บาท")

# เมนูหลัก
def menu():
    options = {
        '1': add_product,
        '2': remove_out_of_stock,
        '3': search_product,
        '4': show_all_products
    }
    while True:
        print("\n1.เพิ่มสินค้า\n2.ลบสินค้าที่หมด\n3.ค้นหา\n4.แสดงทั้งหมด\n5.ออก")
        choice = input("เลือกเมนู: ")
        if choice == '5':
            print("ออกจากโปรแกรม")
            break
        elif choice in options:
            options[choice]()
        else:
            print("เลือกไม่ถูกต้อง")

# เรียกเมนู
menu()
