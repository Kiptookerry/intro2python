class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
            print("Driving around")


class Plane:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def move(self):
            print("Flying around")


class Motorbike:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        print("Riding around")


# instance of our class
car = Car("Volkswagen", "Golf GTI")
plane = Plane("Boeing", "737")
bike = Motorbike("Kawasaki", "Ninja650")

for i in (car, plane, bike):
    i.move()
