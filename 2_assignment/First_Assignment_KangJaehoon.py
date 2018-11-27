'''
Kang Jaehoon
jkang36@binghamton.edu
917-724-6430
C60
Assignment 2-1 (Turtle Racing)

'''

import turtle              # 1.  import the modules
import random

def main():
    
    wn = turtle.Screen()       # 2.  Create a screen
    wn.bgcolor('lightblue')

    lance = turtle.Turtle()    # 3.  Create two turtles
    andy = turtle.Turtle()
    lance.color('red')
    andy.color('blue')
    lance.shape('turtle')
    andy.shape('turtle')

    andy.up()                  # 4.  Move the turtles to their starting point
    lance.up()
    andy.goto(-100,20)
    lance.goto(-100,-20)

    # your code goes here
    
    c = random.randrange(0,25)

    '''
    The first way to use a single call to forward for each turtle
    a = random.randrange(0,150)
    b = random.randrange(0,150)

    andy.forward(a)
    andy.goto(-100,20)

    lance.forward(b)
    lance.goto(-100,-20)

    The problem here is that a turtle moves once with a random number assigned.

    '''

    '''
    The second way to create a for loop using a random number 

    a = random.randrange(0,150)
    b = random.randrange(0,150)
    
    for x in range(a):
        andy.forward(x)
        
    for y in range(b):
        lance.forward(y)

    The problem here is that two turtles do not move simultaneously
    And it requires two for loops
        
    '''

    # The third way to create a single for loop

    for z in range(c):
        a = random.randrange(0,50)
        andy.forward(a)
        b = random.randrange(0,50)
        lance.forward(b)
  

    wn.exitonclick()
    
main()


