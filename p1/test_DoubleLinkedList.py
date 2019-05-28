from  DoubleLinkedList import *
import unittest

class TestDoubleLinkedList(unittest.TestCase):
    def test_add_to_head(self):
        ll = DoubleLinkedList(3)
        n = Node(3,5)
        ll.add_to_head(n)
        self.assertEqual( ll.head.key , n.key)
        self.assertEqual( ll.head.value , n.value)
        self.assertEqual( ll.tail.key , n.key)
        self.assertEqual( ll.tail.value , n.value)

        n2 = Node('a',1)
        ll.add_to_head(n2)
        self.assertEqual( ll.head.key , n2.key)
        self.assertEqual( ll.head.value , n2.value)
        self.assertEqual( ll.tail.key , n.key)
        self.assertEqual( ll.tail.value , n.value)

        # print(ll)

        ll.delete(n)
        self.assertEqual( ll.head.key , n2.key)
        self.assertEqual( ll.head.value , n2.value)
        self.assertEqual( ll.tail.key , n2.key)
        self.assertEqual( ll.tail.value , n2.value)

        n3 = Node('b',2)
        ll.add_to_head(n3)
        self.assertEqual( ll.head.key , n3.key)
        self.assertEqual( ll.head.value , n3.value)
        self.assertEqual( ll.tail.key , n2.key)
        self.assertEqual( ll.tail.value , n2.value)
        print(ll)

        n4 = Node('c',3)
        ll.add_to_head(n4)
        n5 = Node('d',4)
        ll.add_to_head(n5)
        print(ll)

        self.assertEqual( ll.head.key , n4.key)
        self.assertEqual( ll.head.value , n4.value)
        self.assertEqual( ll.tail.key , n2.key)
        self.assertEqual( ll.tail.value , n2.value)
        self.assertEqual( ll.count , 3)
        ll.delete(n4)

        self.assertEqual( ll.head.key , n3.key)
        self.assertEqual( ll.head.value , n3.value)
        self.assertEqual( ll.tail.key , n2.key)
        self.assertEqual( ll.tail.value , n2.value)
        self.assertEqual( ll.count , 2)


