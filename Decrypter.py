import base64
import hashlib
import AESCipher as A
from PIL import Image
from random import randint
import sys
from io import BytesIO

key=""
format = "PNG"
"""
class Decrypter:
    def __init__(self, cipher):
        self.cipher = cipher
    def decrypt_image(self,k):
        #key = self.get_key_from_image()
        key = k
        cipher = self.cipher
        aes = AESCipher(key)
        base64_decoded = aes.decrypt(cipher)
        #print(type(base64_decoded))
        fh = open("decryptedImage.png", "wb")
        fh.write(base64.b64decode(base64_decoded))
        #fh.write(base64_decoded.decode('base64'))
        fh.close() 
        return (base64.b64decode(base64_decoded))
       
def trans_format_RBG(data):
    #tuple: Immutable, ensure that data is not lost
    red, green, blue = tuple(map(lambda e: [data[i] for i in range(0, len(data)) if i % 3 == e], [0, 1, 2]))
    pixels = tuple(zip(red, blue, green))
    return pixels

def trans_format_BGR(data):
    #tuple: Immutable, ensure that data is not lost
    red, green, blue = tuple(map(lambda e: [data[i] for i in range(0, len(data)) if i % 3 == e], [0, 1, 2]))
    pixels = tuple(zip(blue, green, red))
    return pixels
""" 
def trans_format_BRG(data):
    #tuple: Immutable, ensure that data is not lost
    red, green, blue = tuple(map(lambda e: [data[i] for i in range(0, len(data)) if i % 3 == e], [0, 1, 2]))
    pixels = tuple(zip(blue,red, green))
    return pixels
"""
def trans_format_GRB(data):
    #tuple: Immutable, ensure that data is not lost
    red, green, blue = tuple(map(lambda e: [data[i] for i in range(0, len(data)) if i % 3 == e], [0, 1, 2]))
    pixels = tuple(zip(green,red, blue))
    return pixels

def trans_format_GBR(data):
    #tuple: Immutable, ensure that data is not lost
    red, green, blue = tuple(map(lambda e: [data[i] for i in range(0, len(data)) if i % 3 == e], [0, 1, 2]))
    pixels = tuple(zip( green,blue,red))
    return pixels
"""
def decrypt_image_cbc(filename):
    #Open the bmp picture and convert it to RGB image
    
    im = Image.open(filename)
    #Convert image data into pixel value bytes
    value_vector = im.convert("RGB").tobytes()

    imlength = len(value_vector)
    #for i in range(original):
        #print(data[i])
    #Map the pixel value of the filled and encrypted data
    #value_decrypt = trans_format_RGB(A.aes_cbc_decrypt(key, value_vector))
    #value_decrypt2 = trans_format_RBG(A.aes_cbc_decrypt(key, value_vector))  
    #value_decrypt3 = trans_format_BGR(A.aes_cbc_decrypt(key, value_vector))  
    value_decrypt4 = trans_format_BRG(A.aes_cbc_decrypt(key, value_vector)[:imlength])  
    #value_decrypt5 = trans_format_GRB(A.aes_cbc_decrypt(key, value_vector))  
    #value_decrypt6 = trans_format_GBR(A.aes_cbc_decrypt(key, value_vector))      
    #fh = open("decryptedImage.png", "wb")
    #fh.write(value_decrypt.encode('utf-8'))
    #for i in range(original):
        #print(new[i])
    im=Image.new(im.mode, im.size)
    im.putdata(value_decrypt4)
    im.save("decryptfile3" + "." + format, format)
    #Create a new object, store the corresponding value
    """
    im.putdata(value_decrypt2)
    im.save("decryptfile1" + "." + format, format)
    im.putdata(value_decrypt3)
    im.save("decryptfile2" + "." + format, format)
    im.putdata(value_decrypt4)
    im.save("decryptfile3" + "." + format, format)
    im.putdata(value_decrypt5)
    im.save("decryptfile4" + "." + format, format)
    im.putdata(value_decrypt6)
    im.save("decryptfile5" + "." + format, format)
    """
def decrypt_image_ecb(filename):

    
    im = Image.open(filename)
   
    value_vector = im.convert("RGB").tobytes()
    imlength = len(value_vector)

    value_decrypt4 = trans_format_BRG(A.aes_ecb_decrypt(key, value_vector)[:imlength])  
  
    im=Image.new(im.mode, im.size)
    im.putdata(value_decrypt4)
    im.save("decryptfile4" + "." + format, format)
