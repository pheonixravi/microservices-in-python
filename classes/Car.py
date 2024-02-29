class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)


car = Car("Toyota", "Camry", 2020)
car.display_info()