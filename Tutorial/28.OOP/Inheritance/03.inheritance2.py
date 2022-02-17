class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    # drive method

    def drive(self):
        print("Driving ", self.name)

    # turn method
    def turn(self, direction):
        print("Turning", self.name, "To", direction)

    # brake method
    def brake(self):
        print(self.name, "is stopping!")


# inherit Vehicle class
class Car(Vehicle):
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
        self.year = 2007
        print("A new car has been created called", self.name)
        print("Invented was -", self.year)

    def change_gear(self, gear_name):
        print(self.name, "is changing gear to", gear_name)


if __name__ == "__main__":
    c = Car("Toyota", "red", "$299999")
    c.change_gear("L")
