"""
File: colorfilter.py
Tests a function for converting a color image to
black and white.
"""

from images import Image

def colorFilter(image, rgbTriple):
    (r, g, b) = rgbTriple
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r1, g1, b1) = image.getPixel(x, y)
            r1 = r1 + r
            if r1 < 0:
                r1 = 0
            if r1 > 255:
                r1 = 255
            g1 = g1 + g
            if g1 < 0:
                g1 = 0
            if g1 > 255:
                g1 = 255
            b1 = b1 + b
            if b1 < 0:
                b1 = 0
            if b1 > 255:
                b1 = 255
            image.setPixel(x, y, (r1, g1, b1))

def lighten(image, amount):
    """Lightens image by amount."""
    colorFilter(image, (amount, amount, amount))
    pass

def darken(image, amount):
    """Darkens image by amount."""
    colorFilter(image, (-amount, -amount, -amount))
    pass

def main(filename = "smokey.gif"):
    #filename = input("Enter the image file name: ")
    image = Image(filename)
    lighten(image, 128)
    #darken(image, 64)
    #colorFilter(image, (255, 0, 0)) #Edit this line to test different functions and perameters.
    image.draw()

if __name__ == "__main__":
   main()

