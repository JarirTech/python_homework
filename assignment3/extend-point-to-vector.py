import math
# Task 5: Extending a Class

# 1. Create a class called Point. It represents a point in 2d space, with x and y values passed to the __init__() method.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
#  2. It should include methods for equality, string representation, and Euclidian distance to another point.    
    
    
    # metod to check for equality between 2 points
    def __eq__(self, point1):
        return self.x == point1.x and self.y == point1.y
    
    # method for string representation
    def __str__(self):
        print(f'Point at ({self.x}, {self.y})')
        return f'Point at ({self.x}, {self.y})'

    # euclidian distance between 2 points point(x,y) and point1(x,y)

    def ecludian_dist(self, point1): # \(d=\sqrt{(x_{2}-x_{1})^{2}+(y_{2}-y_{1})^{2}}\)
        d = math.sqrt((self.x-point1.x)**2 +(self.x-point1.y)**2)
        return round(d,2)
   
         
# 3.Create a class called Vector which is a subclass of Point and uses the same __init__() method. Add a method in
#  the vector class which overrides the string representation so Vectors print differently than Points. Override 
# the + operator so that it implements vector addition, summing the x and y values and returning a new Vector.

class Vector(Point):

    # vector string representation
    def __str__(self):
        return f'Vector at ({self.x}, {self.y})'
    # vector addition method between to point point(x,y) and point1(x,y)
    def vector_add(self, point1):
        return Vector((self.x + point1.x), (self.y + point1.y) )
        

# 4.Print results which demonstrate all of the classes and methods which have been implemented.

p1 = Point (3,5)
p2 = Point(6, 2)
v1 = Vector(1,4)
v2 = Vector(2,5)
# call __str__
print(p1)


# calling __eq__
print(f'Are {p1} and {p2} equal?: {Point.__eq__(p1,p2)}')

# ecludian distance
print(Point.ecludian_dist(p1, p2))
# calling vector _str_
print(v2)
# adding 2 vectors
new_vect = Vector.vector_add(v1, v2)
print(f'The new {new_vect}')