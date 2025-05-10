product = ["apple", "water", "phone"]
while True:
    f = int(input("กด 1 เพื่อเพิ่มสินค้า\nกด 2 เพื่อลบสินค้า\nกด 3 เพื่อค้นหาสินค้า\nกด 4 เพื่อแสดงรายการสินค้า\nกด 5 เพื่อออกจากโปรแกรม\n"))
    if f == 1:
        a = input("สินค้าที่ต้องการจะเพิ่ม ")
        product.append(a)
    elif f ==2:
        b = input("สินค้าที่ต้องการจะลบ ")
        product.remove(b)
    elif f ==3:
        c = input("สินค้าที่ต้องการค้นหา ")
        print(product.count(c))
    elif f ==4:
        print(product)
    elif f ==5:
        break