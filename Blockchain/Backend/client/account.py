import sys
sys.path.append('/Users/jeanm/OneDrive/Documents/blockchain_in_python')
from Blockchain.Backend.core.EllepticCurve.EllepticCurve import Sha256Point
import secrets  # required to import the private key

class account:
    def createKeys(self):
        # Secp256k1 Curve Generator Points"
        Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
        Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
        
        G = Sha256Point(Gx, Gy)
        
        # create private key
        privateKey = secrets.randbits(256)
        #print(f"Private Key is {privateKey}")
        
if __name__ == '__main__':
    acct = account()
    acct.createKeys()
        
