# bmp-steg LSB All channels

from functions import *

def call():
    # Get filenames
    imageName = input('Please enter name of image to be processed: ')
    if imageName.endswith('.bmp'):
        imageName = imageName[:-4]
    fileName = input('Please enter name of text file to be hidden: ')
    if fileName.endswith('.txt'):
        fileName = fileName[:-4]
    
    # Open image
    im = openImage(imageName)
    xy = (0,0)
    size = im.size
    capacity = (size[0] * size[1])*3
    channel = 0

    # Open plaintext
    plaintext = openText(fileName).strip('\r')
    check = False
    while check is False:
        check = encrypt(plaintext.encode('ascii','ignore'))
    ciphertext = check
    tx = txt2Bin(ciphertext)
    if len(tx) > capacity:
        print('More data given than can fit in the image!')
        print('Given',size,'size and',capacity,'capacity and',len(tx),'length')
        im.close()
        return 1

    # Create a copy
    imEdit = im.copy()
    dr = ImageDraw.Draw(imEdit)

    # Edit pixel data accordingly to bit stream
    print('Hiding info...')
    for bit in tx:
        encodeBit(imEdit,dr,bit,xy,channel)
        channel += 1
        if channel > 2:
            xy = incrementCoord(xy,size)
            channel = 0

    # Save to new file
    print('Info hidden, saving edit...')
    imEdit.save(imageName + '_edit.bmp')

    # Calculate image coverage
    cover = len(tx)/capacity * 100
    print('File coverage is ' + str(round(cover,1)) + '%')

    im.close()
    imEdit.close()
    print('Done!')
    return 0

