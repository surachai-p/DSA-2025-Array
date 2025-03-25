class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"ชื่อสินค้า: {self.name}, จำนวน: {self.quantity}, ราคา: {self.price} บาท"


class Store:
    def __init__(self):
        self.products = []

    def add_product(self, name, quantity, price):
        """ฟังก์ชันเพิ่มสินค้าใหม่"""
        product = Product(name, quantity, price)
        self.products.append(product)
        print(f"เพิ่มสินค้า '{name}' เรียบร้อยแล้ว")

    def remove_out_of_stock(self):
        """ฟังก์ชันลบสินค้าที่หมด"""
        initial_count = len(self.products)
        self.products = [product for product in self.products if product.quantity > 0]
        removed_count = initial_count - len(self.products)
        print(f"ลบสินค้าที่หมดไป {removed_count} รายการ")

    def search_product(self, name):
        """ฟังก์ชันค้นหาสินค้า"""
        found_products = [product for product in self.products if name.lower() in product.name.lower()]
        if found_products:
            print("ผลการค้นหาสินค้า:")
            for product in found_products:
                print(product)
        else:
            print("ไม่พบสินค้าที่ค้นหา")

    def display_all_products(self):
        """ฟังก์ชันแสดงรายการสินค้าทั้งหมด"""
        if not self.products:
            print("ไม่มีสินค้าในร้านค้า")
        else:
            print("รายการสินค้าทั้งหมด:")
            for product in self.products:
                print(product)


# สร้างวัตถุร้านค้า
store = Store()

# ตัวอย่างการใช้ฟังก์ชันต่างๆ
store.add_product("กระเป๋า", 10, 500)
store.add_product("รองเท้า", 0, 1200)
store.add_product("เสื้อยืด", 5, 250)

# แสดงรายการสินค้าทั้งหมด
store.display_all_products()

# ลบสินค้าที่หมด
store.remove_out_of_stock()

# ค้นหาสินค้า
store.search_product("กระเป๋า")
store.search_product("รองเท้า")

# แสดงรายการสินค้าหลังจากลบ
store.display_all_products()