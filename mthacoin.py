import hashlib
import json

class Block():
    def __init__(self, nonce, tstamp, transcation_value,prevhash=''):
        self.nonce=nonce
        self.tstamp=tstamp
        self.transcation_value=transcation_value
        self.prevhash=prevhash
        self.hash= self.calcHash()
    def calcHash(self):
        block_string = json.dumps({"nonce":self.nonce,"tstamp":self.tstamp,"transcation_value":self.transcation_value,"prevhash":self.prevhash}, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    def mineBlock(self,diffic):
        while (self.hash[:diffic] != str('').zfill(diffic)):
            self.nonce += 1
            self.hash = self.calcHash()
        print("Block mined: ", self.hash)

    def __str__(self):
        string = "nonce: " + str(self.nonce) + "\n"
        string += "tstamp " + str(self.tstamp) + "\n"
        string += "transcation: " + str(self.transcation_value) + "\n"
        string += "previous hash: " + str(self.prevhash) + "\n"
        string += "current hash: " + str(self.hash) + "\n"

        return string

class BlockChain():
    def __init__(self):
        self.chain = [self.generateGenesisBlock(),]
        self.difficulty = 2
    def generateGenesisBlock(self):
        return Block(0, '10/11/2018', 'Genesis Block')
    def getLastBlock(self):
        return self.chain[-1]
    def addBlock(self, newBlock):
        newBlock.prevhash = self.getLastBlock().hash
        newBlock.mineBlock(self.difficulty)
        self.chain.append(newBlock)
    def isChainVail(self):
        for i in range(1, len(self.chain)):
            prevb  = self.chain[i-1]
            currb = self.chain[i]
            if (currb.hash != currb.calcHash()):
                print("Invalid block")
                return False
            if (currb.prevhash != prevb.hash):
                print("Invalid chain")
                return False
        return True


mthacoin = BlockChain()
mthacoin.addBlock(Block(1,'12/11/2017',100))
mthacoin.addBlock(Block(2,'13/11/2017',10))
mthacoin.addBlock(Block(3,'14/11/2017',150))
for b in mthacoin.chain:
    print(b)
print(mthacoin.isChainVail())