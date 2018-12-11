from point import *
import math

DOUBLE = 2
SQUARED = 2

# Models a rectangle at Point(x,y) with width and height
class Rectangle:
  # --------------------------------------------------------------------------
  # Constructor

  # param position (Point)
  # param width (int)
  # param height (int)
  def __init__(self, position = Point(0, 0), width = 10, height = 5):
    self.__position = position  # lower left corner point
    self.__width = width
    self.__height = height
                  
  # --------------------------------------------------------------------------
  # Accessors

  # return position(Point)
  def get_position(self):
    return self.__position

  # return width (int)
  def get_width(self):
    return self.__width

  # return height (int)
  def get_height(self):
    return self.__height

  # return area (int)
  def compute_area(self):
    return self.__width * self.__height

  # return perimeter (int)
  def compute_perimeter(self):
    return DOUBLE * self.__width + DOUBLE * self.__height
  
  # --------------------------------------------------------------------------
  # Mutators

  # Assume that left corner point remains fixed
  def transpose(self):
    temp = self.__width
    self.__width = self.__height
    self.__height = temp
  
  # --------------------------------------------------------------------------
  # to_string()

  def __str__(self):
    return \
      "Rectangle with lower left corner at %s with width %d and height %d" % \
      (self.__position, self.__width, self.__height)
  
# ----------------------------------------------------------------------------


def main():
  print("Test toString() on rect1, rect2 and point at origin:")
  rect0 = Rectangle()
  print('here')
  print(rect0)
  print('here')
  rect1 = Rectangle(Point(3, 5), 5, 3)
  print(rect1)
  rect2 = Rectangle(Point(0, 0), 10, 5)
  print(rect2)
  print(Point(0,0))
  print("Test accessors on  rect1:")
  print(rect1.get_position())
  print(rect1.get_width())
  print(rect1.get_height())
  print(rect1.compute_area())
  print(rect1.compute_perimeter())

  rect1._Rectangle__width = 10
  print(rect1)
  print(DOUBLE)
          
main()
