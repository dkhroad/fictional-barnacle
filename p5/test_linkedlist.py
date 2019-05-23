import linkedlist
import unittest

class TestLinkedList(unittest.TestCase):
    def test_add(self):
        ll = linkedlist.LinkedList()
        ll.add('A')
        ll.add('B')
        self.assertEqual(ll.head.value,'A')


    def test_next(self):
        ll = linkedlist.LinkedList()
        ll.add('A')
        ll.add('B')
        ll.add('C')

        self.assertEqual([v for v in ll.next()],['A','B','C'])




