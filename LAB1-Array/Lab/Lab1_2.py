products = []

def add_product():
    products.append(input("เพิ่มสินค้า: "))
    print("เพิ่มสำเร็จ")

def remove_product():
    p = input("ลบสินค้า: ")
    if p in products:
        products.remove(p)
        print("ลบสำเร็จ")
    else:
        print("ไม่พบสินค้า")

def search_product():
    p = input("ค้นหา: ")
    print(f"{'พบ' if p in products else 'ไม่พบ'} สินค้า")

def show_all_products():
    print("\n".join(products) if products else "ไม่มีสินค้า")

while True:
    print("\n1. เพิ่ม  2. ลบ  3. ค้นหา  4. แสดงทั้งหมด  5. ออก")
    c = input("เลือกเมนู: ")
    if c == "1": add_product()
    elif c == "2": remove_product()
    elif c == "3": search_product()
    elif c == "4": show_all_products()
    elif c == "5": break
    else: print("เมนูไม่ถูกต้อง")