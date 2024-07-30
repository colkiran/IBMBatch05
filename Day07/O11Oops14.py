
class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        print("fun called for get")
        return self.__price

    def set_price(self, val):
        print("fun called for set")
        self.__price = val

    def delete_price(self):
        print("fun called for delete")
        self.__price = 0

    price = property(get_price, set_price, delete_price)

coke = Product(65)
print(coke.price)
coke.price = 85
print(coke.price)
del coke.price
print(coke.price)





