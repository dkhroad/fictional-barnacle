import hashlib
import linkedlist


class Block:
    def __init__(self,timestamp,data,previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.calc_hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = f"{self.timestamp}{self.data}{self.previous_hash}".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


# class Blockchain(linkedlist.LinkedList):
#     def __init__(self):
#         super()
#         self.height = -1


#     def add(self,value):
#         super().add(value)
#         self.height += 1


#     def getblock(height):

        

    

    
        


