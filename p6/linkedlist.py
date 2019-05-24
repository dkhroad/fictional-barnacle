class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None



class LinkedList(object):
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def add(self,item):
        node = Node(item)
        self.size += 1
        if self.last:
            self.last.next = node
            self.last = node
        else:
            self.last = node

        if not self.head:
            self.head = self.last

    def size(self):
        return self.size

    def next(self,node):
        while node:
            yield node.value
            node = node.next


    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current:
            value = self.current.value
            self.current = self.current.next
            return value
        else:
            raise StopIteration


        
def union(llist_1,llist_2):
    element_1 = {n for n in llist_1}
    element_2 = {n for n in llist_2}

    llist_u = LinkedList()

    [llist_u.add(el) for el in  element_1.union(element_2)]
    return llist_u


def intersection(llist_1,llist_2):
    element_1 = {n for n in llist_1}
    element_2 = {n for n in llist_2}

    llist_u = LinkedList()

    [llist_u.add(el) for el in  element_1.intersection(element_2)]
    return llist_u
