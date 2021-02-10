# Python program using the turtle module
# Python version = 3.6
# This program makes a pattern using circles
# Author: John Patel

# import Python module
import turtle as t





# create an object (myTurtle) from the Turtle class within the turtle module
myTurtle = t.Turtle()

# define pen color
# allows r, g, b values to be set from 0 to 255
myTurtle.screen.colormode(255)
myTurtle.pencolor((0, 255, 0))

# define screen color
screen = t.Screen()
screen.bgcolor("black")

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


# Draw a sequence of circles
NumberCircles = 30
moveDistance = 10
turnAngle = 20
radius = NumberCircles * 5
angle = 360

for i in range(NumberCircles):
    makeCircle(i * 5, angle)
    myTurtle.left(turnAngle)
    myTurtle.forward(moveDistance)

t.done()
