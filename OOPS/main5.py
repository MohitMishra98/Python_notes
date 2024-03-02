#Abstraction

#Hiding the implementation details of a class and only showing the essential features to the user

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

#we hided the non essential part of starting a car and showed the user only car start button




#Encapsulation

#Wrapping all the data and functions into a single unit (object)

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

#we encapsulated all the data(attributes) and functions(such as start) into a object called "car"
