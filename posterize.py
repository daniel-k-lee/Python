from images import Image

def posterize(image, color=(0,0,0)):
    whitePixel = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) / 3
            if average < 128:
                image.setPixel(x, y, color)
            else:
                image.setPixel(x, y, whitePixel)
def main():
    filename = input( "Enter the image file name: ")
    red = int(input("Enter the integer from 0 to 255 for red: "))
    green = int(input("Enter the integer from 0 to 255 for green: "))
    blue = int(input("Enter the integer from 0 to 255 for blue: "))
    image=Image(filename)
    posterize(image,(red,green,blue))
    image.draw()
if __name__ == "__main__":
    main()
