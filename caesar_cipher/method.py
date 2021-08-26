# file for methods and import variables
from variable import *

class IEncryptMethod():
    def _encryptChar(self,plainchar):
        pass

    def _decryptChar(self,cipherchar):
        pass

    def _reset(self,l,res):
        pass
    
    def _convert(self,userinput,lock):
        pass

l = CaesarCipher(3)
met = input("Please choose '1' to Decode or '2' to Encode a message:\n")
msg = input("Please enter a message:\n")
plain = l._decryptChar(msg)
cipher = l._encryptChar(msg)
res = l._reset()

if met == "1":
    print('Your decryted word is:', plain)
elif met == "2":
    print('Your encrypted word is:', cipher)
else:
    print('Caesar Cipher has been reset to the value:', res)