from queue import *
import unittest

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = Queue(5)
        
    def test_basic(self):
        self.assertEqual(self.q.size(),5)
        self.q.enq(1)
        self.q.enq(2)
        self.q.enq(3)
        self.q.enq(4)
        self.q.enq(5)
        self.q.enq(6)
        self.assertEqual(self.q.deq(),2)
        self.assertEqual(self.q.deq(),3)
        self.assertEqual(self.q.deq(),4)
        self.assertEqual(self.q.deq(),5)
        self.assertEqual(self.q.deq(),6)
        with self.assertRaises(IndexError):
            self.q.deq()
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
