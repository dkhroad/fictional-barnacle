import unittest
from huffman import *

class TestHuffEncDec(unittest.TestCase):
    def setUp(self):
        self.data1 = [(5,1),(7,2),(10,3),(15,4),(20,5),(45,6)]

    def test_get_freq(self):
        self.assertEqual(HuffEncDec()._get_freq("This is a test"),
        [(1, 'T'), (1, 'h'), (1, 'a'), (1, 'e'),
         (2, 'i'), (2, 't'), (3, 's'),(3, ' ')])

    def test_build_huffman_tree(self):
        t = HuffEncDec().build_huffman_tree(self.data1[0],self.data1[1],None)
        self.assertEqual(t.get_root().value,(12,None))

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
