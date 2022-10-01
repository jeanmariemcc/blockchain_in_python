import sys
sys.path.append('/Users/jeanm/OneDrive/Documents/blockchain_in_python')
from Blockchain.Backend.core.EllepticCurve.EllepticCurve import Sha256Point
from Blockchain.Backend.util.util import hash160, hash256
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
        
        #create uncompressed public key
        unCompressedPublicKey = privateKey * G
        xpoint = unCompressedPublicKey.x
        ypoint = unCompressedPublicKey.y
        
        if ypoint.num % 2 == 0:
            compressesKey = b'\x02' + xpoint.num.to_bytes(32, 'big')
        else:
            compressesKey = b'\x03' + xpoint.num.to_bytes(32, 'big')
        hsh160 = hash160(compressesKey)
        # prefix for Mainnet
        main_prefix = b'\0x00'
        
        newAddr = main_prefix + hsh160
        
        # Checksum
        checksum = hash256(newAddr)[:4]  # first 4 characters
        
        newAddr = newAddr + checksum
        BASE58_ALPHABET = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        
        count = 0
        
        for c in newAddr: # looking for leading zeroes
            if c== 0:
                count += 1
            else:
                break
            
        num = int.from_bytes(newAddr, 'big')
        prefix = '1' * count # convert number of leading zeroes to '1'
        
        result = ''
        
        while num > 0:
            num, mod = divmod(num, 58)
            result = BASE58_ALPHABET[mod] + result
            
        PublicAddress = prefix + result
        
        print(f"Private Key {privateKey}")
        print(f"Public Key {PublicAddress}")

        
if __name__ == '__main__':
    acct = account()
    acct.createKeys()
        
