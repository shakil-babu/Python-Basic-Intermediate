class Vehicle:
    """ Base class for all vehicle """

    def __init__(self, name, manufracturer, color):
        self.name = name
        self.manufracturer = manufracturer
        self.color = color

    # drive method
    def drive(self):
        print("Driving", self.manufracturer, self.name)

    # turn method
    def turn(self, direction):
        print("Turning", self.name, "to", direction)

    # brake method
    def brake(self):
        print(self.name, "is stopping!")


# Child class
class Car(Vehicle):
    """Car class"""

    def change_gear(self, gear_name):
        """Method for changing gear"""
        print(self.name, "is changing gear to", gear_name)


if __name__ == "__main__":
    c = Car("Fusion 110 Ex", "Walton", "Black")
    c.drive()
    c.brake()
    c.change_gear("P")
