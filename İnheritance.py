#Kalıtım (Inheritance), bir sınıfın başka bir sınıftan özellikleri ve metodları miras almasını sağlar.
# Bizi kod tekrarı yapmaktan kurtarır.

class Vehicle:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

class Car(Vehicle):
    def __init__(self, brand, model, speed, color, doors):
        super().__init__(brand, model, speed)
        self.color = color
        self.doors = doors

    def show(self):
        return (f"Car: {self.brand} {self.model} "
                f"{self.color} {self.doors}-doors {self.speed}")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, speed, bike_type):
        super().__init__(brand, model, speed)
        self.type = bike_type

    def show(self):
        return (f"Motorcycle: {self.brand} {self.model} "
                f"{self.type} {self.speed}")

car = Car("Toyota", "Corolla", "180 km/h", "Red", 4)
bike = Motorcycle("Honda", "CBR 1000RR", "280 km/h", "Sport")

print(car.show())
print(bike.show())

#Burada Car ve Motorcycle sınıfları Vehicle sınıfından kalıtım alır.