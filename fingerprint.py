import hashlib
import time
from pyfingerprint.pyfingerprint import pyfingerprint

class fingerprint(object):
    def __init__(self):
        self.error = None
        self.positionNumber = 0
        try:
            self.f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
            if ( self.f.verifyPassword() == False ):
                raise ValueError('The given fingerprint sensor password is wrong!')
        except Exception as e:
            print('The fingerprint sensor could not be initialized!')
            print('Exception message: ' + str(e))
            exit(1)

    def readFingerprint(self, buff=0x01):
        while ( self.f.readImage() == False ):
            pass
        self.f.convertImage(buff)
        self.result = self.f.searchTemplate()
        
    def searchFingerprint(self):
        try:
            self.readFingerprint()
            self.positionNumber = self.result[0]
            if ( self.positionNumber <= -1 ): raise Exception('No match found')
        except Exception as e:
            self.error(str(e))
        
        return self.error, self.positionNumber

    def enrollFingerprint(self):
        try:
            self.readFingerprint() # First Finger
            self.positionNumber = self.result[0]
            if ( self.positionNumber >= 0 ): raise Exception('Fingerprint already exists')
            time.sleep(2)
            self.readFingerprint(0x02) # Second Finger
            if ( self.f.compareCharacteristics() == 0 ): raise Exception('Fingers do not match')
            
            #Save Fingerprint
            self.f.createTemplate()
            self.positionNumber = self.f.storeTemplate()

        except Exception as e:
            self.error = str(e)

        return self.error, self.positionNumber

