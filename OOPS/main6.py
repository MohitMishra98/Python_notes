#del keyword

#used to delete properties or entire object itself

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.acc = True
        self.clutch = True
        print("Car started....")

car = Car()
car.start()

del car.acc
del car