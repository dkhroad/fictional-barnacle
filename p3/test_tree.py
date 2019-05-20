import unittest
from tree import *


class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = Tree('A')
        node_b = Node('B')
        node_b.add_left_child(Node('D'))
        self.tree.get_root().add_left_child(node_b)
        self.tree.get_root().add_right_child(Node('C'))
        pass

    def test_basic(self):
        node_a = self.tree.get_root()
        node_b = node_a.get_left_child()
        self.assertEqual(node_a.value,'A')
        self.assertEqual(node_a.get_left_child().value,'B')
        self.assertEqual(node_a.get_right_child().value,'C')
        self.assertEqual(node_b.get_left_child().value,'D')
        self.assertEqual(node_b.get_right_child(),None)

    def test_pre_order_traversal(self):
        vals= [item for item in self.tree.pre_order_traversal()]
        self.assertEqual(vals,['A','B','D','C'])

    def test_bft(self):
        self.assertEqual(self.tree.bf_traversal(),['A','B','C','D'])
        print(self.tree)


    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
