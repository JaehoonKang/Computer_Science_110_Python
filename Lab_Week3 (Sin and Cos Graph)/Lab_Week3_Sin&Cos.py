import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

fred = turtle.Turtle()

#your code here

graph = input("Do you want a Sine graph or Cosine graph?: ")

if graph == 'Sine':
    
  for x in range(0,360):
    sin = 50 * math.sin(math.radians(x))
    fred.goto(x, sin)

else:
    
  for y in range(0,360):
    cos = 50 * math.cos(math.radians(y))
    fred.goto(y,cos)

    
wn.exitonclick()
