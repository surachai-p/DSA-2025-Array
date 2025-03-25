##สร้างโปรแกรมจัดการรายชื่อสินค้าในร้านค้า โดยมีฟังก์ชัน:
#เพิ่มสินค้าใหม่
#ลบสินค้าที่หมด
#ค้นหาสินค้า
#แสดงรายการสินค้าทั้งหมด

products = {}  # สร้าง dictionary เพื่อเก็บข้อมูลสินค้า (ชื่อ: จำนวน)
#เพิ่มสินค้า
def add_product(name,number):
    products[name] = number
    print(f"เพิ่มสินค้า {name} จำนวน {number} เรียบร้อยแล้ว")
#ลบสอนค้า
def remove_empty_products():
    global products
    products = {k: v for k, v in products.items() if v > 0}
    print("ลบสินค้าที่หมดแล้ว")
#ค้นหาสินค้า
def search_product(name):
    if name in products:
        print(f"สินค้า {name} มีจำนวน {products[name]} ชิ้น")
    else:
        print(f"ไม่พบสินค้า {name}")
#แสดงรายการสินค้า
def show_all_products():
    if products:
        print("รายการสินค้าทั้งหมด:")
        for name,number in products.items():
            print(f"- {name}: {number} ชิ้น")
    else:
        print("ไม่มีสินค้าในรายการ")