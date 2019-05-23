import unittest
from huffman import *

    
class TestHuffEncDec(unittest.TestCase):
    def setUp(self):
        self.huffencdec = HuffEncDec()
        self.data1 = [(5,1),(7,2),(10,3),(15,4),(20,5),(45,6)]
        self.data2 = 'ABRACADABRA'

    def test_get_freq(self):

        self.assertEqual(self.huffencdec._get_freq("This is a test"),[(1, 'T'),
                                                                      (1, 'h'),
                                                                      (2, 'i'),
                                                                      (3, 's'),
                                                                      (3, ' '),
                                                                      (1, 'a'),
                                                                      (2, 't'),
                                                                      (1, 'e')])
        q = [node.value for node in self.huffencdec.pqueue.heap_array]
        self.assertEqual(q,[(1, 'T'),(1, 'h'),(1, 'a'),(1, 'e'),(3, ' '),(2, 'i'),(2, 't'),(3, 's')])


    def test_build_huffman_tree_root(self):
        t = self.huffencdec.build_huffman_tree_node(self.data1[0],self.data1[1],None)
        self.assertEqual(t.get_root().value,(12,"1-2"))

        
    def test_build_part_huffman_tree(self):
        self.huffencdec = HuffEncDec()
        self.huffencdec.pqueue.insert(self.data1)
        n1 = self.huffencdec.pqueue.extract()
        n2 = self.huffencdec.pqueue.extract()
        t = self.huffencdec.build_huffman_tree_node(self.data1[0],self.data1[1],None)
        self.huffencdec.pqueue.insert(t.get_root())
        self.assertEqual(t.get_root().value,(12,'1-2'))
        n1 = self.huffencdec.pqueue.extract()
        n2 = self.huffencdec.pqueue.extract()
        
        t = self.huffencdec.build_huffman_tree_node(n1,n2,t)
        r = t.get_root()
        self.assertEqual(r.value,(22,'3-1-2'))
        self.assertEqual(r.get_left_child().value,(10,3))
        rc = r.get_right_child() 
        rcr = rc.get_right_child()
        rcl = rc.get_left_child()

        self.assertEqual(rc.value,(12,'1-2'))
        self.assertEqual(rcr.value,(7,2))

    def test_build_complete_huffman_tree(self):
        self.huffencdec = HuffEncDec()
        self.huffencdec.pqueue.insert(self.data1)
        t = self.huffencdec.build_huffman_tree()
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
        self.huffencdec = HuffEncDec()
        self.huffencdec.pqueue.insert(self.data1)
        self.huffencdec.build_huffman_tree()
        self.huffencdec.build_encodings()
        self.assertEqual(self.huffencdec.encodings,{6: '0',
                                                    3: '100',
                                                    1: '1010', 
                                                    2: '1011',
                                                    4: '110',
                                                    5: '111'})


    def test_encode_tree(self):
        self.huffencdec = HuffEncDec()
        self.huffencdec.pqueue.insert(self.data1)
        t = self.huffencdec.build_huffman_tree()
        # 00001000 0 1 00000110 0 0 1 00000011 0 1 00000001 1 00000010 0 1 00000100 1 00000101
        #    8           6               3            1          2            4         5 
        self.assertEqual(self.huffencdec.encode_tree(),
              "0000100001000001100010000001101000000011000000100100000100100000101"
              )

    def test_decode_tree(self):
        self.huffencdec = HuffEncDec()
        self.huffencdec.pqueue.insert(self.data1)
        t = self.huffencdec.build_huffman_tree()
        encoded_tree = self.huffencdec.encode_tree()
        self.assertEqual(len(encoded_tree),67)

        decoded_tree = self.huffencdec.decode_tree(encoded_tree)
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
        self.huffencdec = HuffEncDec(self.data2)
        hufftree = self.huffencdec.build_huffman_tree()
        encodings = self.huffencdec.build_encodings()

        self.assertEqual(encodings,
                         {'A': '0', 'R': '10', 'B': '110', 'C': '1110', 'D': '1111'})


        encoded_data = self.huffencdec.encode_data(self.data2)
        self.assertEqual(encoded_data,"0000101101101001110011110110100")
        encoded_tree = self.huffencdec.encode_tree()
        decoded_tree = HuffEncDec().decode_tree(encoded_tree)
        decoded_data = self.huffencdec.decode_data(encoded_data,decoded_tree)
        self.assertEqual(self.data2,decoded_data)


    def tearDown(self):
        pass


class Testhuffman_encoding_decoding(unittest.TestCase):

    def test_1(self):
        data = "The quick fox jumped over the lazy dog"
        encoded_data,encoded_tree = huffman_encoding(data)
        self.assertEqual(huffman_decoding(encoded_data,encoded_tree),
                         data)
        

    def test_2(self):
        data = "What is the time complexity of the Python built-in sorted function?"
        encoded_data,encoded_tree = huffman_encoding(data)
        self.assertEqual(huffman_decoding(encoded_data,encoded_tree),data)

    def test_3(self):
        data = "ABRACADABRA"
        encoded_data,encoded_tree = huffman_encoding(data)
        self.assertEqual(huffman_decoding(encoded_data,encoded_tree),data)
    def test_4(self):
        data = "A"
        encoded_data,encoded_tree = huffman_encoding(data)
        self.assertEqual(huffman_decoding(encoded_data,encoded_tree),data)
        data = "AB"
        encoded_data,encoded_tree = huffman_encoding(data)
        self.assertEqual(huffman_decoding(encoded_data,encoded_tree),data)

if __name__ == "__main__":
    unittest.main()
