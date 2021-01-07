"""
File: displayfiles.py
Tests a function for reducing an image's size.
"""

import os

def displayFiles(pathname):
    if os.path.isdir(pathname):
        print("Directory name: " + pathname)
        files = os.listdir(pathname)
        for f in files:
            displayFiles(os.path.join(pathname, f))
    else:
        print("File name: " + pathname)
        with open(pathname, 'r') as f:
            print(f.read())


def main(filename = "c:/Personal/Daniel/python/Sharpen-Image-master"):
    displayFiles(filename)

if __name__ == "__main__":
   main()

