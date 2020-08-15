# bmp-steg LSB Stripper

from functions import openImage, incrementCoord

# Function grabs last 2 bits
def parse(px):
    lsbMask = (1 << 2) - 1
    return (lsbMask & px)

# Switch, case implementation
def switch(argument):
    case = {
        0: (0,0,0),
        1: (28,28,28),
        2: (56,56,56),
        3: (84,84,84),
        4: (112,112,112),
        5: (140,140,140),
        6: (168,168,168),
        7: (195,195,195),
        8: (224,224,224),
        9: (255,255,255)
    }
    return case.get(argument, "Invalid input")

def call():
    # Variables
    imageName = input("Please enter name of image to be processed: ")
    if imageName.endswith(".bmp"):
        imageName.replace(".bmp","")
    im = openImage(imageName)
    dr = ImageDraw.Draw(im)
    xy = (0,0)
    size = im.size
    length = size[0]*size[1]

    # Edit pixel data accordingly to bit stream
    print("Stripping last 2 bits of each channel")
    for i in range(length):
        px = im.getpixel(xy)
        px = switch(parse(px[0]) + parse(px[1]) + parse(px[2]))
        dr.point(xy, fill=px)
        xy = incrementCoord(xy,size)
    im.save(imageName + "_strip.bmp")
    print("Done!")