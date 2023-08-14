class Phone:
    #constructors
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phone_number):
        print(f"{self.brand} is calling {phone_number}")

    def __str__(self) -> str:
        return f"Brand {self.brand},\nPrice = {self.price}"


iphone = Phone("iPhone X", 15000)
samsung = Phone("Samsung X", 14000)

print(f"Brand = {iphone.brand} and Price = {iphone.price}")
print(f"Brand = {samsung.brand} and Price = {samsung.price}")
iphone.call(9999)


print(iphone)
print(samsung)



class MyClass:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print("Value:", self.value)


# Creating an instance of the class
obj = MyClass(42)

# Calling the instance method using the object
obj.print_value()