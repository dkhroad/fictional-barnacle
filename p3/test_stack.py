from stack import *
import unittest

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_basic(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(),2)
        self.assertEqual(self.stack.pop(),2)
        self.assertEqual(self.stack.pop(),1)


    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()