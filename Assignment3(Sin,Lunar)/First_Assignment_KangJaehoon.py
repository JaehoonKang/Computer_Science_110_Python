
'''
Kang Jaehoon
jkang36@binghamton.edu
917-724-6430
C60
Assignment 3-1
'''

'''
ANALYSIS

RESTATE the problem

  Draw a Sine, Cosine, or Log graph after an input from a user

OUTPUT to monitor

  Action: Drawing of Sine, Cosine, or Log curve

INPUT from keyboard

  graph (string): input("Enter <sin>, <cos>, or <log>: ")

  Input value: "sin", "cos", or "log"
  
GIVENS:

  Sine Graph, Cos Graph, Log(base 2):
  
  math.sin(), math.cos(), math.radians, math.log2()
    
PROCESSING:

  Import required modules: math, turtle

  After explaining a purpose of a program,

  For x-axis and y-axis, create two turtles:
  
    x_axis = turtle.Turtle()
  
    y_axis = turtle.Turtle()
    
  Create a turtle:

    fred.turtle.Turtle()

  Get input value (either sin, cos, or log):
  
    graph = input("Enter <sin>, <cos>, or <log>: ")

  Upon input above, Use a multiway decision statement (if/elif/else):

  Using necessary functions:

    math.sin(), math.radiants(), math.cos(), math.log2()

  Draw a curve, using a turtle:
  
    turtle.goto()

'''
# IMPORTS

import math
import turtle

# DESIGN

def main():

  wn = turtle.Screen()
  
  wn.bgcolor('lightblue')

  wn.setworldcoordinates(0, -1, 360, 1)

  # Create turtle
  
  fred = turtle.Turtle()

  # Decide color of turtle
  
  fred.color('red')

  # For a purpose of drawing x-axis, y-axis
  
  x_axis = turtle.Turtle()
  
  y_axis = turtle.Turtle()

  # Tell user purpose of program
  
  print("This program draws a sin, cos, or log wave as requested by user \n")

  print("Would you like to draw a sin,cos or log curve? \n")

  # Decide which curve a user draws
  
  graph = input("Enter <sin>, <cos>, or <log>: ")

  # Draw x-axis
  
  x_axis.goto(360,0)

  # When a user chooses a SINE curve
  
  if graph == 'sin':

    # Draw y-axis to set a different screen size for y-axis
    
    y_axis.goto(0,1)
    
    y_axis.goto(0,-1)

    # Set a value range from 0 to 360 since it is a sin curve

    for x in range(360):

      # Using math.sin function in python, convert number in a range to sine
      
      sin = math.sin(math.radians(x))

      # With converted range, draw a sine graph using the turtle
      
      fred.goto(x, sin)

  # When a user chooses a COSINE curve

  elif graph == "cos":

    # Draw y-axis to set a different screen size for y-axis
    
    y_axis.goto(0,1)
    
    y_axis.goto(0,-1)

    # Move turtle (fred) to a starting point (0,1)
    
    fred.up()
    
    fred.goto(0,1)

    fred.down()

    # Set a value range from 0 to 360 since it is a cos curve
    
    for y in range(360):

      # Using math.cos function, convert number in a range to cosine
      
      cos = math.cos(math.radians(y))

      # With converted range, draw a cosine graph using the turtle
      
      fred.goto(y,cos)

  # When a user chooses a LOG curve
      
  elif graph == "log":

    # Set a different screen size for viewing

    wn.setworldcoordinates(0, -100, 360, 140)

    y_axis.goto(0,100)
    
    y_axis.goto(0,-100)

    # Set a value range from 1 to 360 since it is a log curve
    
    for z in range(1,360):

      # Using math.log2 function in python, convert number in a range to log
      
      log =  math.log2(z)

      # With converted range, draw a log graph using the turtle
      
      fred.goto(z,10 * (log))

  # Print out an error message
  # if they ask for something other then sine, cosine, or log 

  else:

    print("ERROR: You need to type between sin, cos, and log \n")

    print("Please run the program again or hit F5")
      
  wn.exitonclick()
  
main()




