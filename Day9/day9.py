# - Extend Car into an ElectricCar subclass with battery capacity
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def display_info(self):
        return f"{super().display_info()} with {self.battery_capacity} kWh battery"
# Example usage
if __name__ == "__main__":
    car1 = Car("Toyota", "Camry", 2020)
    car2 = ElectricCar("Tesla", "Model S", 2021, 100)

    print(car1.display_info())
    print(car2.display_info())