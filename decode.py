# bmp-steg decode

from functions import *

def call():
    # Get filenames
    imageName1 = input('Please enter name of original image: ')
    if imageName1.endswith('.bmp'):
        imageName1 = imageName1[:-4]
    imageName2 = input('Please enter name of modified image: ')
    if imageName2.endswith('.bmp'):
        imageName2 = imageName2[:-4]
    
    # Open images
    imOrig = openImage(imageName1)
    imEdit = openImage(imageName2)
    xy = (0,0)
    size = imOrig.size
    capacity = (size[0] * size[1])*3
    channel = 0
    bitData = ''

    # Iterate through entire image
    print('Extracting info...')
    count = 0
    for i in range(capacity):
        # Check for changes
        if (imOrig.getpixel(xy)[channel] != imEdit.getpixel(xy)[channel]):
            bitData += '1'
            count = 0
        else:
            bitData += '0'
            count += 1
            if count is 8:
                break
        # Iterate channel
        channel += 1
        if channel > 2:
            xy = incrementCoord(xy,size)
            channel = 0
    
    print('Converting to text...')
    pad = len(bitData) % 8
    bitData += pad * '0'

    ciphertext = bin2Txt(bitData)
    ciphertext = ciphertext.strip(b'\x00')
    check = False
    try:
        while check is False:
            check = decrypt(ciphertext).decode()
    except:
        print('Failed to decrypt')
        imOrig.close()
        imEdit.close()
        return 1
    
    plaintext = check
    fileName = input('Please enter file name to save data to: ')
    if fileName.endswith('.txt'):
        fileName = fileName[:-4]
    tx = open(fileName + '.txt','w')
    tx.write(plaintext)
    tx.close()

    imOrig.close()
    imEdit.close()
    print('Done!')
    return 0
