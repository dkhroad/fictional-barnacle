import blockchain
import unittest
import time

class TestBlock(unittest.TestCase):
    def test_block(self):
        block = blockchain.Block(1558649054,
                                 "Genesis Block",
                                 None,0)
        self.assertEqual(block.hash,"61977ea186232850707dd0c2f14d74f5981ba9cff82c07966608c56d0d101542")



class TestBlockchain(unittest.TestCase):
    def test_add_block(self):
        block = blockchain.Block(1558649054,
                                 "Genesis Block",
                                 None,0)
        bc = blockchain.Blockchain()
        bc.add(block)

        block2 = blockchain.Block(int(time.time()),
                                  "First block",
                                  block.hash,
                                  1)
        bc.add(block2)
                                  
        block3 = blockchain.Block(int(time.time()),
                                  "2nd block",
                                  block2.hash,
                                  2)
        bc.add(block3)

        self.assertEqual(bc.getblock(0).hash,"61977ea186232850707dd0c2f14d74f5981ba9cff82c07966608c56d0d101542")
        self.assertEqual(bc.getblock(1).data,"First block")
        self.assertEqual(bc.getblock(2).data,"2nd block")
        self.assertEqual(bc.getblock(3),None)




