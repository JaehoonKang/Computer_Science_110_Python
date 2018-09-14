import math
import turtle

def main():
  
  wn = turtle.Screen()
  wn.bgcolor('lightblue')
  
  george = turtle.Turtle()

  wn.setworldcoordinates(0, -1, 360, 1) #set a screen size

  def sine_wave():
    
    for angle in range(360):
      
      y = math.sin(math.radians(angle))
      
      george.goto(angle, y)

  def cosine_wave():
    
    george.up()
    
    george.goto(0,1)
    
    george.down()
    
    for angle in range(360):

      z = math.cos(math.radians(angle))
      
      george.goto(angle,z)
      
  print("Do you want a Sine or Cosine graph?: \n ")

  graph = input("Enter sin or cos: ")

  if graph ==  'sin':
    
    sine_wave()
    
  elif graph == 'cos':
    
    cosine_wave()

      
  wn.exitonclick()
  
main()
