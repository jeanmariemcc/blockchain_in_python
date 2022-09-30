import os
import json

class BaseDB:
    def __init__(self):
        self.basepath = 'data' # where to look for blockchain file
        # see inheritance in class BlockchainDB(BaseDB):
        self.filepath = '/'.join((self.basepath, self.filename))
        
    def read(self):
        if not os.path.exists(self.filepath):
            print(f"File {self.filepath} not available")
            return False
        
        with open(self.filepath, 'r') as file:  # read mode
            raw = file.readline()  # the entire file is read in one shot b/c of how it is stored
            
        if len(raw) > 0:
            data = json.loads(raw)  # data will be used in the write block
        else:
            data = [] # this is for the genesis block
        return data
        
    def write(self, item): 
        # needs block as input, passed from the BlockchainDB class
        # problem with append mode, it will write the data, but not separate the object
        # work around is read, concatenate the block object, then write the data 
        data = self.read()
        if data: # if data is returned
            data = data + item  # append new block (item)
        else:  # if empty, it is genesis block
            data = item
            
        with open(self.filepath, "w+") as file:
           file.write(json.dumps(data)) 



class BlockchainDB(BaseDB):
    def __init__(self):
        # to get access to this filename, the BaseDB needed to be inherited
        self.filename = 'blockchain'  
        super().__init__()
        
    def lastBlock(self): # need block height and previous block hash
        data = self.read()
            
        if data:
            return data[-1]  # -1 is last block