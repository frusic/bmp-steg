# bmp-steg Main function

import sys

try:
    import PIL
except ImportError:
   sys.exit('Please install Pillow library: https://github.com/python-pillow/Pillow')

try:
    import cryptography
except ImportError:
   sys.exit('Please install Pillow library: https://github.com/python-pillow/Pillow')

try:
   import decode, encode, strip
except ImportError:
   sys.exit('Please ensure all required files are in the folder')

def menu():
    print('-----------------')
    print('Options:')
    print('    1) Encode plaintext into a BMP image')
    print('    2) Decode BMP image to retrieve plaintext')
    print('    3) Strip Least Significant Bytes of BMP image')
    print('    q) Quit')
    print('-----------------')
    get = input('Input: ')
    return call(get)

def call(get):
    if get is '1':
        check = encode.call()
    elif get is '2':
        check = decode.call()
    elif get is '3':
        check = strip.call()
    elif get is 'q':
        sys.exit(0)
    else:
        print('Invalid input')
        check = 0
    print('======================================================')
    return check

if __name__ == '__main__':
    check = 0
    while check is 0:
        check = menu()