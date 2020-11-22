import base64
import hashlib
from AESCipher import aes_ecb_encrypt, aes_cbc_encrypt
import AESCipher as A
from PIL import Image
from random import randint

filename_encrypted_ecb = "Encrypted_ecb"
filename_encrypted_cbc= "Encrypted_cbc"
format = "PNG"
key=""
keylen=0

"""
class Encrypter:
    def __init__(self, text,key):
        self.text = text
        self.key =  key
    def encrypt_image(self):
        aes = AESCipher(self.key)
        cipher = aes.encrypt(self.text)
        #message = aes.decrypt(cipher)
        return cipher
"""
def pad(s):
    #return data + b"\x00" * (keylen - len(data) % keylen)
    return s + (16 - len(s) % 16) * chr(16 - len(s) % 16).encode('utf-8')

# Map the image data to RGB
def trans_format_RGB(data):
    #tuple: Immutable, ensure that data is not lost
    red, green, blue = tuple(map(lambda e: [data[i] for i in range(0, len(data)) if i % 3 == e], [0, 1, 2]))
    pixels = tuple(zip(red, green, blue))
    return pixels

def encrypt_image_ecb(filename):
    #Open the bmp picture and convert it to RGB image
    
    im = Image.open(filename)
    #Convert image data into pixel value bytes
    value_vector = im.convert("RGB").tobytes()

    imlength = len(value_vector)
    #for i in range(original):
        #print(data[i])
    #Map the pixel value of the filled and encrypted data
    print(key)
    A.keysize=keylen
    value_encrypt = trans_format_RGB(A.aes_ecb_encrypt(key, pad(value_vector))[:imlength])
    
    
    #for i in range(original):
        #print(new[i])

    #Create a new object, store the corresponding value
    im2 = Image.new(im.mode, im.size)
    im2.putdata(value_encrypt)

    # Save the object as an image in the corresponding format
    im2.save(filename_encrypted_ecb + "." + format, format)
    
def encrypt_image_cbc(filename):
    #Open the bmp picture and convert it to RGB image
    im = Image.open(filename)
    value_vector = im.convert("RGB").tobytes()

    # Convert image data to pixel value bytes
    imlength = len(value_vector)
    A.keysize=keylen
    # Perform pixel value mapping on the filled and encrypted data
    value_encrypt = trans_format_RGB(A.aes_cbc_encrypt(key, pad(value_vector))[:imlength])
    """
    fh = open("cipher.txt", "wb")
    #print(type(A.aes_cbc_encrypt(key, pad(value_vector))))
    fh.write(base64.b64encode(A.aes_cbc_encrypt(key, pad(value_vector))))
    fh.close()"""
    # Create a new object, store the corresponding value
    im2 = Image.new(im.mode, im.size)
    im2.putdata(value_encrypt)

    # Save the object as an image in the corresponding format
    im2.save(filename_encrypted_cbc + "." + format, format)
    
