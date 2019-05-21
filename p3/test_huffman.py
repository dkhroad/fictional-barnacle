import unittest
from huffman import *

    
class TestHuffEncDec(unittest.TestCase):
    def setUp(self):
        self.huffencdec = HuffEncDec()
        self.data1 = [(5,1),(7,2),(10,3),(15,4),(20,5),(45,6)]
        self.data2 = 'ABRACADABRA'

    def test_get_freq(self):
        self.assertEqual(self.huffencdec._get_freq("This is a test"),
        [(1, 'T'), (1, 'h'), (1, 'a'), (1, 'e'),
         (2, 'i'), (2, 't'), (3, 's'),(3, ' ')])

    def test_build_huffman_tree_root(self):
        t = self.huffencdec.build_huffman_tree_node(self.data1[0],self.data1[1],None)
        self.assertEqual(t.get_root().value,(12,"1-2"))

    def test_add_to_list(self):
        newlist = self.huffencdec.add_to_freq_list(self.data1,(12,'1-2'))
        self.assertEqual(newlist,
                         [(10, 3), (12, '1-2'), (15, 4), (20, 5), (45, 6)])
        
    def test_build_part_huffman_tree(self):
        print(self.huffencdec)
        t = self.huffencdec.build_huffman_tree_node(self.data1[0],self.data1[1],None)
        self.assertEqual(t.get_root().value,(12,'1-2'))
        newlist = self.huffencdec.add_to_freq_list(self.data1,(12,'1-2'))
        self.assertEqual(newlist,
                         [(10, 3), (12, '1-2'), (15, 4), (20, 5), (45, 6)])
        t = self.huffencdec.build_huffman_tree_node(newlist[0],newlist[1],t)
        r = t.get_root()
        self.assertEqual(r.value,(22,'3-1-2'))
        self.assertEqual(r.get_left_child().value,(10,3))
        rc = r.get_right_child() 
        rcr = rc.get_right_child()
        rcl = rc.get_left_child()

        self.assertEqual(rc.value,(12,'1-2'))
        self.assertEqual(rcr.value,(7,2))

    def test_build_complete_huffman_tree(self):
        t = self.huffencdec.build_huffman_tree(self.data1)
        # print(t)
        r = t.get_root()
        
        self.assertEqual(r.value,(102,'6-3-1-2-4-5'))
        rl = r.get_left_child()
        rr = r.get_right_child()
        self.assertEqual(rl.value,(45,6))
        self.assertEqual(rl.get_left_child(),None)
        self.assertEqual(rl.get_right_child(),None)
        self.assertEqual(rr.value,(57,'3-1-2-4-5'))
        rrl = rr.get_left_child()
        rrr = rr.get_right_child()
        self.assertEqual(rrl.value,(22,'3-1-2'))
        self.assertEqual(rrr.value,(35,'4-5'))


    def test_encoding(self):
        t = self.huffencdec.build_huffman_tree(self.data1)
        self.huffencdec.build_encodings()
        # print(self.huffencdec.encodings)
        self.assertEqual(self.huffencdec.encodings,{6: '0',
                                                    3: '100',
                                                    1: '1010', 
                                                    2: '1011',
                                                    4: '110',
                                                    5: '111'})

    def test_trim_tree(self):
        t = self.huffencdec.build_huffman_tree(self.data1)
        self.huffencdec.trim()
        print(self.huffencdec.tree)
        pass

    def test_encode_tree(self):
        t = self.huffencdec.build_huffman_tree(self.data1)
        # 00001000 0 1 00000110 0 0 1 00000011 0 1 00000001 1 00000010 0 1 00000100 1 00000101
        #    8           6               3            1          2            4         5 
        self.assertEqual(self.huffencdec.encode_tree(),
              "0000100001000001100010000001101000000011000000100100000100100000101"
              )

    def test_decode_tree(self):
        t = self.huffencdec.build_huffman_tree(self.data1)
        encoded_tree = self.huffencdec.encode_tree()
        self.assertEqual(len(encoded_tree),67)

        decoded_tree = self.huffencdec.decode_tree(encoded_tree)
        print(decoded_tree)
        root = decoded_tree.get_root()
        self.assertEqual(root.get_left_child().value,6)
        self.assertEqual(root
                         .get_right_child()
                         .get_left_child()
                         .get_left_child().value,3)
        self.assertEqual(root
                         .get_right_child()
                         .get_left_child()
                         .get_right_child()
                         .get_left_child().value,1)
        self.assertEqual(root
                         .get_right_child()
                         .get_left_child()
                         .get_right_child()
                         .get_right_child().value,2)
        self.assertEqual(root
                         .get_right_child()
                         .get_right_child()
                         .get_left_child().value,4)
        self.assertEqual(root
                         .get_right_child()
                         .get_right_child()
                         .get_right_child().value,5)






    def test_huffman_encoding(self):
        freqlist = self.huffencdec._get_freq(self.data2)
        self.assertEqual(freqlist,
                         [(1, 'C'), (1, 'D'), (2, 'B'), (2, 'R'), (5, 'A')])
        hufftree = self.huffencdec.build_huffman_tree(freqlist)

        encodings = self.huffencdec.build_encodings()
        self.assertEqual(encodings,
                         {'A': '0', 'C': '100', 'D': '101', 'B': '110', 'R': '111'})


        encoded_data = self.huffencdec.encode_data(self.data2)
        # 0 110 111 0 100 0 101 0 110 111 0
        # A  B   R  A  C  A  D  A  B   R  A
        self.assertEqual(encoded_data,"0000101101101110100010101101110")
        encoded_tree = self.huffencdec.encode_tree()
        decoded_tree = HuffEncDec().decode_tree(encoded_tree)
        decoded_data = self.huffencdec.decode_data(encoded_data,decoded_tree)
        print("decoded_data",decoded_data)
        self.assertEqual(self.data2,decoded_data)


    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
