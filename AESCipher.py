import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import random
import string

keysize=0
"""
class AESCipher(object):

    def __init__(self, key): 
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')
        #return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        #print("25")
        #print(type(s))
        #print(type((self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)))
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs).encode('utf-8')

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
"""
   
def key_generator(size = keysize, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

# CBC encryption
def aes_cbc_encrypt(key, data, mode=AES.MODE_CBC):
    #IV is a random value
    print(keysize)
    IV = key_generator(keysize)
    #print(key)
    aes = AES.new(key.encode("utf8"), mode, IV.encode("utf8"))
    new_data = aes.encrypt(data)
    return new_data

# ECB encryption
def aes_ecb_encrypt(key, data, mode=AES.MODE_ECB):
    #The default mode is ECB encryption
    aes = AES.new(key.encode("utf8"), mode)
    new_data = aes.encrypt(data)
    return new_data

def unpad(s):
        return s[:-ord(s[len(s)-1:])]
    
def aes_cbc_decrypt(key, data, mode=AES.MODE_CBC):
    #The default mode is ECB encryption
    aes = AES.new(key.encode("utf8"), mode)
    new_data = unpad(aes.decrypt(data[16:]))
    #print(type(new_data), new_data)
    return new_data

def aes_ecb_decrypt(key, data, mode=AES.MODE_ECB):
    #The default mode is ECB encryption
    aes = AES.new(key.encode("utf8"), mode)
    new_data = unpad(aes.decrypt(data[16:]))
    return new_data
