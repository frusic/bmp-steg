# bmp-steg decode

from functions import incrementCoord, openImage

# Function to decode binary
def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

def call():
    # Variables
    imageName = input("Please enter name of original image: ")
    if imageName.endswith(".bmp"):
        imageName.replace(".bmp","")
    imOrig = openImage(imageName)
    imageName = input("Please enter name of modified image: ")
    if imageName.endswith(".bmp"):
        imageName.replace(".bmp","")
    imEdit = openImage(imageName)
    xy = (0,0)
    size = imOrig.size
    length = (size[0]*size[1])*3
    channel = 0
    bitData = ""

    for i in range(length):
        # Check for changes
        if (imOrig.getpixel(xy)[channel] != imEdit.getpixel(xy)[channel]):
            bitData += "1"
        else:
            bitData += "0"
        # Check channel
        if channel != 2:
            channel += 1
        else:
            xy = incrementCoord(xy,size)
            channel = 0

    hide = decode_binary_string(bitData)
    hide = hide.replace("\x00","")
    fileName = input("Please enter file name to save data to: ")
    if fileName.endswith(".txt"):
        fileName.replace(".txt","")
    tx = open(fileName + ".txt","w")
    tx.write(hide)
    tx.close()
