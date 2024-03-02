#WAP to Define a Circle class to create a circle with radius r using the constructor. 
#Define an Area() method of the class which calculates the area of the circle. 
#Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

class Circle:
    def __init__(self,radius):
        self.radius = radius
        print("circle created with radius : ",self.radius)
    
    def area(self):
        return (22/7)*(self.radius*self.radius)
    
    def perimeter(self):
        return 2*(22/7)*self.radius


circle1 = Circle(99)
print("Area of circle 1 is : ",circle1.area())
print("Perimeter of circle 1 is : ",circle1.perimeter())

circle2 = Circle(100)
print("Area of circle 2 is : ",circle2.area())
print("Perimeter of circle 2 is : ",circle2.perimeter())