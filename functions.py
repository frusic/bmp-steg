# bmp-steg Helper functions

# Function to open image
def openImage(imageName):
    print("Opening image...")
    try:
        im = Image.open(imageName + ".bmp")
    except:
        print("Image not found!")
        exit()
    return im

# Function to open text
def openText(fileName):
    print("Opening text...")
    try:
        tx = open(fileName + ".txt","r")
    except:
        print("Text file not found!")
        exit()
    hide = tx.read()
    tx.close()
    return hide

# Convert text into bitstream
def txt2Bin(hide,size):
    print("Converting text to binary bits...")
    hide = ''.join([i if ord(i) < 128 else ' ' for i in hide])
    hide = ''.join('{0:08b}'.format(ord(x), 'b') for x in hide)
    if len(hide) > (size[0] * size[1])*3:
        return False
    else:
        return hide

# Function to increment pixel coordinates
def incrementCoord(coord,size):
    if coord[0] < size[0]-1:
        x = coord[0] + 1
        y = coord[1]
    else:
        x = 0
        y = coord[1] + 1
    xy = (x,y)
    return xy

# Function to calculate coverage of the image
def calcCover(xy,size):
    if xy[1] == 0:
        cover = (xy[0]/(size[0]*size[1]))*100
        byte = int(xy[0]*3/8)
        print("Saved", byte ,"bytes of information.")
    else:
        cover = ((size[0]*(xy[1]-1)+xy[0])/(size[0]*size[1]))*100
        byte = int((size[0]*(xy[1]-1)+xy[0])*3/8)
        print("Saved",byte,"bytes of information.")
    print("File coverage is",round(cover,1),"%")

# Function to encode bit into correct channel of given pixel
def encodeBit(im,dr,bit,xy,channel):
    px = im.getpixel(xy)
    if channel == 0:
        if px[channel] == 255:
            px = (px[0]-int(bit),px[1],px[2])
        else:
            px = (px[0]+int(bit),px[1],px[2])
    elif channel == 1:
        if px[channel] == 255:
            px = (px[0],px[1]-int(bit),px[2])
        else:
            px = (px[0],px[1]+int(bit),px[2])
    elif channel == 2:
        if px[channel] == 255:
            px = (px[0],px[1],px[2]-int(bit))
        else:
            px = (px[0],px[1],px[2]+int(bit))
    dr.point(xy, fill=px)
