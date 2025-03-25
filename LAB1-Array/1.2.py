

products = []


def add_product():
    name = input("กรุณาป้อนชื่อสินค้า: ")
    quantity = int(input("กรุณาป้อนจำนวนสินค้า: "))
    price = float(input("กรุณาป้อนราคาสินค้า: "))
    
    
    product = {
        "name": name,
        "quantity": quantity,
        "price": price
    }
    products.append(product)
    print(f"สินค้า '{name}' ถูกเพิ่มเรียบร้อยแล้ว")


def remove_out_of_stock():
    global products
    
    new_products = []
    for product in products:
        if product["quantity"] > 0:
            new_products.append(product)
    products = new_products
    print("สินค้าที่หมดได้ถูกลบออกจากรายการแล้ว")


def search_product():
    name = input("กรุณาป้อนชื่อสินค้าที่ต้องการค้นหา: ")
    found_products = []
    for product in products:
        if name.lower() in product["name"].lower():
            found_products.append(product)
    
    if found_products:
        for product in found_products:
            print(f"ชื่อสินค้า: {product['name']}, จำนวน: {product['quantity']}, ราคา: {product['price']}")
    else:
        print(f"ไม่พบสินค้าที่ชื่อ '{name}'")


def show_all_products():
    if products:
        for product in products:
            print(f"ชื่อสินค้า: {product['name']}, จำนวน: {product['quantity']}, ราคา: {product['price']}")
    else:
        print("ไม่มีสินค้าในร้าน")


def main():
    while True:
        print("\nเมนูหลัก:")
        print("1. เพิ่มสินค้าใหม่")
        print("2. ลบสินค้าที่หมด")
        print("3. ค้นหาสินค้า")
        print("4. แสดงรายการสินค้าทั้งหมด")
        print("5. ออกจากโปรแกรม")
        
        choice = input("กรุณาเลือกตัวเลือก (1-5): ")
        
        if choice == '1':
            add_product()
        elif choice == '2':
            remove_out_of_stock()
        elif choice == '3':
            search_product()
        elif choice == '4':
            show_all_products()
        elif choice == '5':
            print("ออกจากโปรแกรม")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาเลือกใหม่")


main()

