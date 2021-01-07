"""
File: cicle.py
Tests a function for converting a color image to
black and white.
"""

from turtle import Turtle
t = Turtle()

def drawCircle(t, x, y, radius):
    t.up()
    t.goto(x, y-radius)
    t.down()
    t.setheading(0)
    for count in range(120):
        t.forward(2.0*3.14*radius/120.0)
        t.left(3)
  

def main():
    print("Draw a cicle ")
    drawCircle(t, 50, 75, 100)


if __name__ == "__main__":
   main()
