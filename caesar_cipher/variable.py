# file to store variables
class CaesarCipher():
    def __init__(self,drift):
        # Construction for Caesar cipher with the given integer drift
        self._clockwise = ''.join([chr(ord('a') +((x + drift)%26)) for x in range(26)])
        self._anticlockwise = ''.join([chr(ord('a')+((x - drift+26)%26)) for x in range(26)])
    
    def _encryptChar(self,plainchar):
        plainchar = plainchar.lower()
        return self._convert(plainchar,self._clockwise)

    def _decryptChar(self,cipherchar):
        cipherchar = cipherchar.lower()
        return self._convert(cipherchar,self._anticlockwise)

    def _reset(self):
        l = CaesarCipher(1)

    def _convert(self,userinput,lock):
        msg = list(userinput)
        for d in range(len(msg)):
            if(msg[d].islower()):
                x = ord(msg[d]) - ord('a')
                msg[d] = lock[x]
        return ''.join(msg)
    
