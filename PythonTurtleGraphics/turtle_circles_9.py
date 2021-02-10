# Python program using the turtle module
# Python version = 3.6
# This program makes a pattern using circles
# Author: John Patel

# import Python module
import turtle as t
import random as rnd

# create an object (myTurtle) from the Turtle class within the turtle module
myTurtle = t.Turtle()
myTurtle.screen.colormode(255)


def makeCircle(r, a):
    """
    The function makes a circle using the circle method
    
    Parameters:
        r: radius of circle
        a: angle/arc extent
        
    Returns:
        none
    """
    myTurtle.circle(r, a)


def thePenColor():
    """
    The function chooses the color of the circle (random color)
    
    Parameters:
        none
        
    Returns:
        none
    """
    red = rnd.randint(0, 255)
    green = rnd.randint(0, 255)
    blue = rnd.randint(0, 255)
    myTurtle.pencolor((red, green, blue))


# Draw a sequence of circles
NumberCircles = 30
moveDistance = 10
turnAngle = 30
radius = NumberCircles * 5
angle = 360

for i in range(NumberCircles):
    thePenColor()
    makeCircle(i * 5, angle)
    myTurtle.forward(i)

t.done()
