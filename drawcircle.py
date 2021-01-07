#To draw anything in the Turtle window import the Turtle module
from turtle import Turtle
#import math module to use pi
from math import pi
def drawCircle(turtle, x, y, radius):
    #pick up the Turtle and do not draw any line
    turtle.up()
    turtle.goto(0, 0)
    turtle.goto(x, y)
    #Move the turtle to (x, y) coordinates position
    turtle.goto(x, y-radius)
    #pick up the turtle and draw the line. 
    turtle.down()
 # calculate the distance according to the given problem statement
 #move the turtle point with 120 times of distance
    distance = 2.0 * pi * (radius / 120.0 )   
    print( distance)
    for i in range( 1, 121):      
        turtle.left(3)
        turtle.forward(distance)  
#define a function to draw a specified circle from the given problem statement
def main(): 
 #create a new Turtle object(Turtle()) and assign to an object 'turtle'.
 turtle = Turtle()
 drawCircle(turtle,50, 75, 100)
if __name__ == "__main__":
    main()

     
