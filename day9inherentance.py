class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...")

# 👇 Inherited class
class Car(Vehicle):  # 👈 Car inherits from Vehicle
    def show(self):
        print(f"This is a car of brand {self.brand}")


c1 = Car("BMW")
c1.start()   # 👈 Parent class ka method
c1.show()    # 👈 Child class ka method
