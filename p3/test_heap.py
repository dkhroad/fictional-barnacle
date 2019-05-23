import unittest
from heap import *


class TestHeap(unittest.TestCase):
    def test_insert_array(self):
        items = [17, 15, 10, 19, 20, 25, 22, 7, 12, 9] 
        heap = Heap()
        heap.insert(items)
        print(heap)
        self.assertEqual(heap.extract(),7)
        self.assertEqual(heap.extract(),9)
        self.assertEqual(heap.extract(),10)
        self.assertEqual(heap.extract(),12)
        self.assertEqual(heap.extract(),15)
        self.assertEqual(heap.extract(),17)
        self.assertEqual(heap.extract(),19)
        self.assertEqual(heap.extract(),20)
        self.assertEqual(heap.extract(),22)
        self.assertEqual(heap.extract(),25)
        with self.assertRaises(IndexError):
            heap.extract()

    def test_insert(self):
        items = [17, 15, 10, 19, 20, 25, 22, 7, 12, 9] 
        heap = Heap()
        heap.insert(17)
        self.assertEqual(heap.heap_array[0].value, 17)
        heap.insert(15)
        self.assertEqual(heap.heap_array[0].value, 15)
        self.assertEqual(heap.heap_array[1].value, 17)
        heap.insert(10)
        self.assertEqual(heap.heap_array[0].value, 10)
        self.assertEqual(heap.heap_array[1].value, 17)
        self.assertEqual(heap.heap_array[2].value, 15)
        heap.insert(19)
        self.assertEqual(heap.heap_array[0].value, 10)
        self.assertEqual(heap.heap_array[1].value, 17)
        self.assertEqual(heap.heap_array[2].value, 15)
        self.assertEqual(heap.heap_array[3].value, 19)
        heap.insert(20)
        self.assertEqual(heap.heap_array[4].value, 20)
        heap.insert(25)
        self.assertEqual(heap.heap_array[5].value, 25)
        heap.insert(22)
        self.assertEqual(heap.heap_array[6].value, 22)
        # import pdb; pdb.set_trace()
        heap.insert(7)
        self.assertEqual(heap.heap_array[7].value, 19)
        heap.insert(12)
        self.assertEqual(heap.heap_array[8].value, 17)
        heap.insert(9)
        self.assertEqual(heap.heap_array[9].value, 20)
        print(heap)
        

    def test_extract(self):
        items = [17, 15, 10, 19, 20, 25, 22, 7, 12, 9] 
        heap = Heap()
        for i in range(len(items)):
            heap.insert(items[i])
        print(heap)

        self.assertEqual(heap.extract(),7)
        self.assertEqual(heap.extract(),9)
        self.assertEqual(heap.extract(),10)
        self.assertEqual(heap.extract(),12)
        self.assertEqual(heap.extract(),15)
        self.assertEqual(heap.extract(),17)
        self.assertEqual(heap.extract(),19)
        self.assertEqual(heap.extract(),20)
        self.assertEqual(heap.extract(),22)
        self.assertEqual(heap.extract(),25)
        with self.assertRaises(IndexError):
            heap.extract()

        
    def test_extract_tuples(self):
        items = [(45,6),(20,5),(5,1),(15,4),(7,2),(10,3)]
        heap = Heap(key=lambda v: v.value[0])
        for i in range(len(items)):
            heap.insert(items[i])
        print(heap)
        self.assertEqual(heap.extract(),(5,1))
        self.assertEqual(heap.extract(),(7,2))
        self.assertEqual(heap.extract(),(10,3))
        self.assertEqual(heap.extract(),(15,4))
        self.assertEqual(heap.extract(),(20,5))
        self.assertEqual(heap.extract(),(45,6))
        
