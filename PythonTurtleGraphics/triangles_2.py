# Python program using the turtle module
# Python version = 3.6
# A pattern using only triangles
# Author: John Patel

# import Python modules
import turtle as t
import random as rnd
import math as m
import numpy as np
from math import pi

# set screen window size (x, y)
screen = t.Screen()
screen.screensize(10000 , 10000)
    
# create an object (myTurtle) from the Turtle class within the turtle module
myTurtle = t.Turtle()
# allows r, g, b values to be set from 0 to 255
myTurtle.screen.colormode(255)
    
# set the speed (1 to 10)
myTurtle.speed(10) 


def main():
    """
    The function creates a pattern using triangles
    
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
        triangle(i, 60, 15)
        myTurtle.end_fill()
        myTurtle.penup()
        myTurtle.right(70)
        myTurtle.forward(20)
        myTurtle.pendown()


def triangle(first_length, angle_a, second_length):
    """
    The function makes a triangle.
    
    Parameters:
        first_length: One side Length length of triangle
        angle_a: One angle of triangle
        second_length: Second side Length length of triangle
        
    Returns:
        none
    """    
    myposition = myTurtle.pos()
    myTurtle.forward(first_length)
    myTurtle.left(angle_a)
    myTurtle.forward(second_length)
    myTurtle.goto(myposition)

      
main()
t.done()
