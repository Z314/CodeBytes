# Python program using the turtle module
# Python version = 3.6
# Functions to make common 2D shapes. Import them as required.
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
myTurtle.screen.colormode(255)
    
# set the speed (1 to 10)
myTurtle.speed(10) 

 
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
    
    
def rightTriangle(base, height):
    """
    The function makes a right angled triangle
    
    Parameters:
        base: base length of triangle
        height: height of triangle, measured from base
        
    Returns:
        none
    """    
    myposition = myTurtle.pos()
    myTurtle.forward(base)
    myTurtle.left(90)
    myTurtle.forward(height)
    myTurtle.goto(myposition)
    

def rhombus(length_a, angle):
    """
    The function makes a rhombus (diamond)
    
    Parameters:
        length_a: sideLength length a (all sides are the same length)
        angle: one internal angle of rhombus (between 0 and 180 degrees)
        
    Returns:
        none
    """    
    myposition = myTurtle.pos()
    myTurtle.setheading(0)
    myTurtle.forward(length_a)
    myTurtle.left(180 - angle)
    myTurtle.forward(length_a)
    myTurtle.setheading(180)
    myTurtle.forward(length_a)
    myTurtle.goto(myposition) 
    
    
def parallelogram(length_a, length_b, angle):
    """
    The function makes a Parallelogram
    
    Parameters:
        length_a: sideLength length a 
        length_b: sideLength length b
        angle: one angle
        
    Returns:
        none
    """    
    myposition = myTurtle.pos()
    myTurtle.setheading(0)
    myTurtle.forward(length_a)
    myTurtle.left(angle)
    myTurtle.forward(length_b)
    myTurtle.setheading(180)
    myTurtle.forward(length_a)
    myTurtle.goto(myposition)    
    

def square2():
    """
    The function makes a square. A pop up GUI displays for user to enter data.
    
    Parameters:
        none
                
    Returns:
        none
    """
    leng = myTurtle.screen.textinput("Side length", "Enter sideLength length of square")   
    myposition = myTurtle.pos()
    myTurtle.forward(float(leng))
    myTurtle.left(90)
    myTurtle.forward(float(leng))
    myTurtle.left(90)
    myTurtle.forward(float(leng))
    myTurtle.left(90)
    myTurtle.goto(myposition) 


def square(sideLength):
    """
    The function makes a square
    
    Parameters:
        sideLength: side length of square
                
    Returns:
        none
    """
    myposition = myTurtle.pos()
    myTurtle.forward(sideLength)
    myTurtle.left(90)
    myTurtle.forward(sideLength)
    myTurtle.left(90)
    myTurtle.forward(sideLength)
    myTurtle.left(90)
    myTurtle.goto(myposition)

    
def rectangle(length_a, length_b):
    """
    The function makes a rectangle
    
    Parameters:
        length_a: side length of rectangle
        length_b: side length of rectangle
                
    Returns:
        none
    """
    myposition = myTurtle.pos()
    myTurtle.forward(length_a)
    myTurtle.left(90)
    myTurtle.forward(length_b)
    myTurtle.left(90)
    myTurtle.forward(length_a)
    myTurtle.left(90)
    myTurtle.goto(myposition)

    
def circle(radius):
    """
    The function makes a circle
    
    Parameters:
        radius: radius of circle
                
    Returns:
        none
    """
    myTurtle.circle(radius)

    
def semiCircle(radius):
    """
    The function makes a semi circle
    
    Parameters:
        radius: radius of semi circle
                
    Returns:
        none
    """
    myTurtle.circle(radius, 180)

    
def ellipse(a, b):
    """
    The function makes a ellipse
    
    Parameters:
        a: width = 2a
        b: height = 2b
                
    Returns:
        none
    """
    for t in np.linspace(0, 2 * pi, 200):
        x = a * m.cos(t)
        y = b * m.sin(t)
        if t == 0:
            myTurtle.penup()
            myTurtle.goto(x, y)
            myTurtle.pendown()
        else:
            myTurtle.goto(x, y)


def pentagon(radius):
    """
    The function makes a pentagon
    
    Parameters:
        radius: radius of a circle inscribed
                
    Returns:
        none
    """
    myTurtle.circle(radius, 360, 5)

    
def hexagon(radius):
    """
    The function makes a hexagon
    
    Parameters:
        radius: radius of a circle inscribed
                
    Returns:
        none
    """
    myTurtle.circle(radius, 360, 6)


def heptagon(radius):
    """
    The function makes a hexagon
    
    Parameters:
        radius: radius of a circle inscribed
                
    Returns:
        none
    """
    myTurtle.circle(radius, 360, 7)

    
def octagon(radius):
    """
    The function makes a octagon
    
    Parameters:
        radius: radius of a circle inscribed
                
    Returns:
        none
    """
    myTurtle.circle(radius, 360, 8)

    
def nonagon(radius):
    """
    The function makes a Nonagon
    
    Parameters:
        radius: radius of a circle inscribed
                
    Returns:
        none
    """
    myTurtle.circle(radius, 360, 9)

    
def decagon(radius):
    """
    The function makes a Decagon
    
    Parameters:
        radius: radius of a circle inscribed
                
    Returns:
        none
    """
    myTurtle.circle(radius, 360, 10)

