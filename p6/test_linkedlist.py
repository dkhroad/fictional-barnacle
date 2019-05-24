import unittest
import linkedlist

class TestLinkedList(unittest.TestCase):
    def test_union(self):
        llist_1 = linkedlist.LinkedList()
        llist_2 = linkedlist.LinkedList()
        for n in llist_1:
            print(n)

        element_1 = [3,2,4,35,6,65,6,4,3,21]
        element_2 = [6,32,4,9,6,1,11,21,1]

        [llist_1.add(i) for i in element_1]
        [llist_2.add(i) for i in element_2]


        llist_u = linkedlist.union(llist_1,llist_2)
        s = set(element_1).union(set(element_2))
        self.assertEqual({n for n in llist_u},s)


    def test_intersection(self):
        llist_1 = linkedlist.LinkedList()
        llist_2 = linkedlist.LinkedList()

        element_1 = [3,2,4,35,6,65,6,4,3,23] 
        element_2 = [1,7,8,9,11,21,1] 

        intersection = set(element_1).intersection(set(element_2))

        [llist_1.add(i) for i in element_1]
        [llist_2.add(i) for i in element_2]

        llist_i = linkedlist.intersection(llist_1,llist_2)

        self.assertEqual({el for el in llist_i},intersection)

