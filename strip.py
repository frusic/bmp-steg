# bmp-steg LSB Stripper

from functions import *

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
    return case[argument]

def call():
    # Get filename
    imageName = input('Please enter name of image to be processed: ')
    if imageName.endswith('.bmp'):
        imageName = imageName[:-4]

    # Open image
    im = openImage(imageName)
    xy = (0,0)
    size = im.size
    area = size[0]*size[1]

    # Create a copy
    imEdit = im.copy()
    dr = ImageDraw.Draw(imEdit)

    # Strip last 2 bits of each channel
    print('Stripping last 2 bits of each channel')
    for i in range(area):
        px = imEdit.getpixel(xy)
        px = switch(parse(px[0]) + parse(px[1]) + parse(px[2]))
        dr.point(xy, fill=px)
        xy = incrementCoord(xy,size)
    imEdit.save(imageName + '_strip.bmp')

    im.close()
    imEdit.close()
    print('Done!')
    return 0