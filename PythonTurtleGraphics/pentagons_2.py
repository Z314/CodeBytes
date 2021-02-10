# Python program using the turtle module
# Python version = 3.6
# A pattern using only pentagons
# Author: John Patel

# import Python modules
import turtle as t
import random as rnd
import math as m
import numpy as np
from math import pi

# set screen window size (x, y)
screen = t.Screen()
screen.screensize(2000 , 1000)
    
# create an object (myTurtle) from the Turtle class within the turtle module
myTurtle = t.Turtle()
# allows r, g, b values to be set from 0 to 255
myTurtle.screen.colormode(255)
    
# set the speed (1 to 10)
myTurtle.speed(10) 


def main():
    """
    The function creates a pattern using pentagons
    
    Parameters:
        none
        
    Returns:
        none
    """
    for i in range(200):
        red = rnd.randint(0, 255)
        green = rnd.randint(0, 255)
        blue = rnd.randint(0, 255)
        myTurtle.color("black", (red, green, blue))
        myTurtle.begin_fill()
        pentagon(100)
        myTurtle.end_fill()
        myTurtle.right(90)
        myTurtle.forward(50)


def pentagon(radius):
    """
    The function makes a pentagon. The circle function is called
    with parameters: radius, arc extent, steps (number of sides)
    
    Parameters:
        radius: radius of a circle inscribed
                
    Returns:
        none
    """
    myTurtle.circle(radius, 360, 5)

      
main()
t.done()
