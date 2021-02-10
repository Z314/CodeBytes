# Python program using the turtle module
# Python version = 3.6
# This program makes a pattern using circles
# Author: John Patel

# import Python module
import turtle as t 

# create an object (myTurtle) from the Turtle class within the turtle module
myTurtle = t.Turtle()

# size of circle/arc
radius = 50
angle = 360  # 360 is a full circle


def makeCircle():
    """
    The function makes a circle (radius, degrees) using the circle method
    
    Parameters:
        none
        
    Returns:
        none
    """
    myTurtle.circle(radius, angle)


# Draw a sequence of circles
NumberCircles = 30
moveDistance = 10
turnAngle = 20
for i in range(NumberCircles):
    makeCircle()
    myTurtle.left(turnAngle)
    myTurtle.forward(moveDistance)

t.done()
