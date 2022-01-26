# instantiate
class Car:
    name = ""
    color = ""

    def start(self):
        print("starting the engine!")


# create a Car object / instantiate
car = Car()
car.name = "Toyota"
print(car.name)

car.start()
