# Create a Car class with attributes and a display method
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def display(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")
        print(f"Car Color: {self.color}")
# Create a list of Car objects and display their details
cars = [
    Car("Toyota", "Camry", 2020, "Blue"),
    Car("Honda", "Civic", 2019, "Red"),
    Car("Ford", "Mustang", 2021, "Black")
]
for car in cars:
    car.display()
    print()