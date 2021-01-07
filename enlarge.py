"""
File: enlarge.py
Tests a function for reducing an image's size.
"""

from images import Image

def enlarge(image, factor):
    """Builds and returns a new image which is smaller
    copy of the argument image, by the factor argument."""
    width = image.getWidth()
    height = image.getHeight()
    new = Image(width * factor, height * factor)
    oldY = 0
    newY = 0
    while oldY < height:
        while newY < (oldY+1)*factor:
            oldX = 0
            newX = 0
            while oldX < width:
                oldP = image.getPixel(oldX, oldY)
                while newX < (oldX+1)*factor:
                    new.setPixel(newX, newY, oldP)
                    newX += 1   
                oldX += 1
            newY += 1
        oldY += 1
    return new

def main(filename = "smokey.gif"):
    image = Image(filename)
    image2 = enlarge(image, 2)
    image2.draw()
    #image3 = shrink(image, 3)

if __name__ == "__main__":
   main()

