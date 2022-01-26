#Geometry: The Circle2D class
from math import pi, sqrt
import turtle as your_mom

class Circle2D:
    def __init__(self,x = 0, y = 0, r = 0,color="white"):
        self.__x = x
        self.__y = y
        self.__r = r
        your_mom.penup ()
        your_mom.goto (x*20, (y*20)-(r*20))
        your_mom.fillcolor(color)
        your_mom.pendown()
        your_mom.begin_fill()
        your_mom.circle (r*20)
        your_mom.end_fill ()
        your_mom.penup()
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,value):
        self.__x = value

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y=value    

    @property
    def r(self):
        return self.__r
    
    @r.setter
    def r(self, value):
        self.__r=value  

    def get_area(self):
        return pi*self.__r**2
    
    def get_perimiter(self):
        return 2*pi*self.__r
    
    def contains_point(self, x, y):
        if sqrt((self.__x-x)**2+(self.__y-y)**2)<=self.__r:
            return True
        else:
            return False
    
    def contains(self, other):
        if sqrt((self.__x-other.__x)**2+(self.__y-other.__y)**2)<=(self.__r-other.__r):
            return True
        else:
            return False
    
    def overlaps(self,other):
        if sqrt((self.__x-other.__x)**2+(self.__y-other.__y)**2)<=(self.__r+other.__r):
            return True
        else:
            return False
    
    def contains_another(self, other):
        if sqrt((other.__x-self.__x)**2+(other.__y-self.__y)**2)<=(other.__r-self.__r):
            return True
        else:
            return False
    
    def __lt__(self, other):
        if self.get_area() < other.get_area():
            return True
        else:
            return False


    def __cmp__(self, other):
        return self.get_area() / other.get_area()

    def __le__(self, other):
        if self.get_area() <= other.get_area():
            return True
        else:
            return False
    
    def __eq__(self, other):
        if self.get_area() == other.get_area():
            return True
        else:
            return False

    def __ne__(self, other):
        if self.get_area() != other.get_area():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.get_area() > other.get_area():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.get_area() >= other.get_area():
            return True
        else:
            return False

ball1 = Circle2D(x=0,y=0, r=4,color="red")
ball2 = Circle2D(1, 2, 1,"blue")
your_mom.mainloop()

print(f"Area of Ball1 is: {ball1.get_area()}")
print(f"Area of Ball2 is: {ball2.get_area()}")

print(f"Perimiter of Ball1 is: {ball1.get_perimiter()}")
print(f"Perimiter of Ball2 is: {ball2.get_perimiter()}")

print(f"Ball1 contains point (2, 3) is: {ball1.contains_point(2, 3)}")
print(f"Ball 1 contains Ball2 is: {ball1.contains(ball2)}")
print(f"Ball1 and Ball2 overlaps is: {ball1.overlaps(ball2)}")
print(f"Ball2 is contained within Ball1 is: {ball2.contains_another(ball1)}")

print(ball1 < ball2)
print(ball1 == ball2)
print(ball1 > ball2)
print(ball1 <= ball2)
print(ball1 != ball2)
print(ball1 >= ball2)






