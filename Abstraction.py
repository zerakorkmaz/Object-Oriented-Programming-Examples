from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def price(self):
        pass
    @abstractmethod
    def status(self):
        pass

class Car(Vehicle):
    def price(self):
        return 300

    def status(self):
        return "Car is available."

class Motorcycle(Vehicle):
    def price(self):
        return 150

    def status(self):
        return "Motorcycle is available."

class Truck(Vehicle):
    def price(self):
        return 500

    def status(self):
        return "Tuck is available."

class RentalProcess:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)

    def show_available_vehicles(self):
        print("\n--- Avaliable Vehicles ---")
        for vehicle in self.vehicles:
            print(f"Price: {vehicle.price()} TL, Status: {vehicle.status()}")

rental_process = RentalProcess()

car = Car()
motorcycle = Motorcycle()
truck = Truck()

rental_process.add_vehicle(car)
rental_process.add_vehicle(motorcycle)
rental_process.add_vehicle(truck)

rental_process.show_available_vehicles()
