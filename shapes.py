#Shape
class Shape:
    def __init__(self, name):
        self.name = name 
    
    def show(self):
        print(f"This is a {self.name}.")

    def perimeter(self):
        pass 

    def area(self):
        pass 

class Circle(Shape):
    
    def __init__(self, radius):
        super().__init__("circle") 
        self.radius = radius 
    
    def perimeter(self):
        return 2 * 3.14 * self.radius 
    
    def area(self):
        return 3.14 * self.radius ** 2 

class Triangle(Shape):
    def __init__(self, a, b, c, h):
        super().__init__("triangle") 
        self.a = a
        self.b = b 
        self.c = c 
        self.h = h 
   
    def perimeter(self):
        return self.a + self.b + self.c 
    
    def area(self):
        return 0.5 * self.b * self.h

class Square(Shape):
  
    def __init__(self, side):
        super().__init__("square")
        self.side = side
    
    def perimeter(self):
        return 4 * self.side 
    
    def area(self):
        return self.side ** 2

class Rectangle(Shape):
    
    def __init__(self, length, width):
        super().__init__("rectangle") 
        self.length = length 
        self.width = width 
    
    def perimeter(self):
        return 2 * (self.length + self.width) 
    
    def area(self):
        return self.length * self.width 

c = Circle(5) 
c.show()
print(f"Perimeter of the circle is {c.perimeter()}") 
print(f"Area of the circle is {c.area()}") 

t = Triangle(3, 4, 5, 2.4) 
t.show()
print(f"Perimeter of the triangle is {t.perimeter()}") 
print(f"Area of the triangle is {t.area()}") 

s = Square(6) 
s.show()
print(f"Perimeter of the square is {s.perimeter()}")
print(f"Area of the square is {s.area()}")

r = Rectangle(8, 3)
r.show() 
print(f"Perimeter of the rectangle is {r.perimeter()}") 
print(f"Area of the rectangle is {r.area()}") 
