import sys
sys.path.append('/Users/jeanm/OneDrive/Documents/blockchain_in_python')

from Blockchain.Backend.core.block import Block
from Blockchain.Backend.core.blockheader import BlockHeader
from Blockchain.Backend.util.util import hash256
from Blockchain.Backend.core.database.database import BlockchainDB
import time
import json

ZERO_HASH = '0' * 64
VERSION = 1

class Blockchain:
    def __init__(self):
        #self.chain = []
        self.GenesisBlock()
        
    def write_on_disk(self, block):
        blockchainDB = BlockchainDB()
        blockchainDB.write(block)

    def fetch_last_block(self):
        blockchainDB = BlockchainDB()
        return blockchainDB.lastBlock()
                
    def GenesisBlock(self):
        BlockHeight = 0
        prevBlockHash = ZERO_HASH
        self.addBlock(BlockHeight, prevBlockHash)
        
    def addBlock(self, BlockHeight, prevBlockHash):
        timestamp = int(time.time())
        Transaction = f"Codies Alert sent {BlockHeight} Bitcoins to JM"
        merkleRoot = hash256(Transaction.encode()).hex()
        bits = 'ffff001f'
        blockheader = BlockHeader(VERSION, prevBlockHash, merkleRoot, timestamp, bits)
        blockheader.mine()
        #self.chain.append(Block(BlockHeight, 1, blockheader.__dict__, 1, Transaction).__dict__)
        self.write_on_disk([Block(BlockHeight, 1, blockheader.__dict__, 1, Transaction).__dict__])  # block input needs to be a list
        #print(json.dumps(self.chain, indent = 4))
        
                
    def main(self):
       while True:
           #lastBlock = self.chain[::-1]
           #BlockHeight = lastBlock[0]["Height"] + 1
           #prevBlockHash = lastBlock[0]["BlockHeader"]["blockHash"]
           lastBlock = self.fetch_last_block()
           BlockHeight = lastBlock["Height"] + 1
           prevBlockHash = lastBlock["BlockHeader"]["blockHash"]
           self.addBlock(BlockHeight, prevBlockHash)         
             
if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.main()
    
