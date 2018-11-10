import point

class Point:
    # Point class for representing and manipulating x,y coordinates. 

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)


class Rectangle:
    # Rectangle class using Point, width and height

    def __init__(self, initP, initW, initH):
        self.__location = initP
        self.__width = initW
        self.__height = initH
    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height
    def str(self):
        return "%d %d"%(self.__width,self.__height)
    def area(self):
        return self.__width * self.__height
    def perimeter(self):
        return (self.__width + self.__height) *2
    def transpose(self):
        temp = self.__width
        self.__width = self.__height
        self.__height = temp
        
def main():
  loc = Point(4, 5)
  r = Rectangle(loc, 6, 5)

  print(r.getWidth())
  print(r.getHeight())
  print(r.str())
  print(r.area())
  print(r.perimeter())


main()
    
    
