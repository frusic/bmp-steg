# bmp-steg

## Description
bmp-steg is a very basic steganography tool used to hide plaintext into a BMP image.
bmp-steg supports 24 bit depth BMP images and symmetric encryption of the plaintext.

## Requirements
Requires Pillow library by Alex Clark and Contributors
https://github.com/python-pillow/Pillow

Requires Cryptography library by Python Cryptographic Authority
https://github.com/pyca/cryptography

## Use
Open main.py with python3:
```py
    python3 main.py
```
There is a text interface that allows encoding info to an image, decoding info from one original and one modified image, and stripping the LSB from an image.

## Demonstration
Here we have an image of a city:
![image](https://i.imgur.com/VtNXDMT.png)

After encoding 500 paragraphs of Lorem ipsum:
![image_edit](https://i.imgur.com/bsB8t3s.png)

LSB Strip of image without steganography:
![LSB Strip of image](https://i.imgur.com/XXvNzAG.png)

LSB Strip of image with steganography:
![LSB Strip of image_edit](https://i.imgur.com/EPQN8UY.png)
