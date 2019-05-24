import hashlib
import linkedlist


class Block:
    def __init__(self,timestamp,data,previous_hash,height):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.height = height
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = f"{self.timestamp}{self.data}{self.previous_hash}{self.height}".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        return f"""
timestamp: {self.timestamp}
data: {self.data}
previous_hash: {self.previous_hash}
self.hash = {self.hash}
"""


class Blockchain(object):
    def __init__(self):
        self.chain = linkedlist.LinkedList()
        self.height = -1

    def current_height(self):
        return height

    def add(self,value):
        self.chain.add(value)
        self.height += 1
        assert(value.height == self.height)


    def getblock(self,height):
        it = iter(self.chain)
        for b in next(it):
            if b.height == height:
                return b

        

    

    
        


