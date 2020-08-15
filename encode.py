# bmp-steg LSB All channels

from functions import *

def call():
# Variables
    imageName = input("Please enter name of image to be processed: ")
    if imageName.endswith(".bmp"):
        imageName.replace(".bmp","")
    fileName = input("Please enter name of text file to be hidden: ")
    if imageName.endswith(".txt"):
        imageName.replace(".txt","")
    im = openImage(imageName)
    dr = ImageDraw.Draw(im)
    xy = (0,0)
    size = im.size
    channel = 0
    tx = txt2Bin(openText(fileName),size)
    while tx==False:
        print("More info than can be encoded!")
        tx = txt2Bin(openText(),size)

    # Edit pixel data accordingly to bit stream
    print("Hiding info...")
    for bit in tx:
        encodeBit(im,dr,bit,xy,channel)
        if channel != 2:
            channel += 1
        else:
            xy = incrementCoord(xy,size)
            channel = 0

    # Save to new file
    print("Info hidden, saving edit...")
    im.save(imageName + "_edit.bmp")
    calcCover(xy,size)
    print("Done!")

