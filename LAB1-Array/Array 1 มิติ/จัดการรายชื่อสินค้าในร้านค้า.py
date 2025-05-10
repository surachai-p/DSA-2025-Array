
products = []
def add(name):
    products.append(name)
    print(f"เพิ่มสินค้า: {name}")

def remove(name):
    if name in products:
        products.remove(name)
        print(f"ลบสินค้า: {name}")
    else:
        print(f"สินค้า {name} ไม่อยู่ในรายการ")

def search(name):
    if name in products:
        print(f"พบสินค้า: {name}")
    else:
        print(f"ไม่พบสินค้า: {name}")

def show():
    if products:
        print("รายการสินค้า:")
        for product in products:
            print(f"- {product}")
    else:
        print("ไม่มีสินค้าภายในร้าน")

add("แป้ง")
add("น้ำตาล")
remove("น้ำตาล")
search("แป้ง")
add("กระบอกไม้ไผ่")
show()
