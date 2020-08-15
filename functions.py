# bmp-steg Helper functions

from cryptography.fernet import Fernet
from PIL import Image, ImageDraw
import sys, zlib

PIXELMAX = 255

# Function to open image
def openImage(imageName):
    print('Opening image...')
    ext = imageName + '.bmp'
    try:
        im = Image.open(ext)
    except:
        print('Image not found!')
        sys.exit()
    return im

# Function to open text
def openText(fileName):
    print('Opening text...')
    ext = fileName + '.txt'
    try:
        tx = open(ext,'r')
    except:
        print('Text file not found!')
        sys.exit()
    hide = tx.read()
    tx.close()
    return hide

# Convert text into bitstream
def txt2Bin(text):
    print('Converting text to binary bits...')
    bitstream = ''.join(bin(int(char))[2:].zfill(8) for char in text)
    return bitstream

# Convert bitstream to text
def bin2Txt(bitstream):
    print('Converting binary bits to text...')
    text = b''
    for i in range(0, len(bitstream), 8):
        text += chr(int(bitstream[i:i+8],2)).encode('ascii','ignore')
    return text

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

# Function to encode bit into correct channel of given pixel
def encodeBit(im,dr,bit,xy,channel):
    px = im.getpixel(xy)
    # Red channel
    if channel == 0:
        if px[channel] == PIXELMAX:
            px = (px[0]-int(bit),px[1],px[2])
        else:
            px = (px[0]+int(bit),px[1],px[2])
    # Blue channel
    elif channel == 1:
        if px[channel] == PIXELMAX:
            px = (px[0],px[1]-int(bit),px[2])
        else:
            px = (px[0],px[1]+int(bit),px[2])
    # Green channel
    elif channel == 2:
        if px[channel] == PIXELMAX:
            px = (px[0],px[1],px[2]-int(bit))
        else:
            px = (px[0],px[1],px[2]+int(bit))
    dr.point(xy, fill=px)

# Function to encrypt plaintext if desired
def encrypt(plaintext):
    flag = input('Do you want to encrypt the message with a key? (y/n): ')
    if (flag is not 'y') and (flag is not 'n'):
        print('Please enter \'y\' or \'n\'')
        return False
    elif flag is 'y':
        key = Fernet.generate_key()
        print('Your key is: ' + key.decode())
        f = Fernet(key)
        ciphertext = f.encrypt(plaintext)
        return ciphertext
    elif flag is 'n':
        return plaintext

# Function to decrypt plaintext if encrypted
def decrypt(ciphertext):
    flag = input('Are the contents encryped? (y/n): ')
    if (flag is not 'y') and (flag is not 'n'):
        print('Please enter \'y\' or \'n\'')
        return False
    elif flag is 'y':
        key = input('Enter the key: ')
        print('Your key is: ' + key)
        f = Fernet(key)
        plaintext = f.decrypt(ciphertext)
        return plaintext
    elif flag is 'n':
        return ciphertext