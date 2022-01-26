class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def start(self):
        print("Staring the engine!")


car = Car("Toyota", "White")
print(car.name)
print(car.color)
car.start()
