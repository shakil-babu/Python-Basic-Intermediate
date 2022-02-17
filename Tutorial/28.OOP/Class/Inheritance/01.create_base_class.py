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


if __name__ == "__main__":
    v1 = Vehicle("Fusion 110 Ex", "Walton", "Black")
    v2 = Vehicle("Softail Delux", "Harley-Davidson", "Blue")
    v3 = Vehicle("Mustan", "Ford", "Red")

    v1.drive()
    v2.drive()
    v3.drive()

    v1.turn("left")
    v2.turn("right")

    v1.brake()
    v2.brake()
    v3.brake()
