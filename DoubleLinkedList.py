class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList(object):
    def __init__(self,size=5):
        self.capacity = size
        self.head = None
        self.tail = None
        self.count = 0

    def add_to_head(self,node):
        if self.is_full():
            print("Warning: max capacity reached.")
            return

        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node
        self.count += 1

    def is_full(self):
        return self.count >= self.capacity

    def delete(self,node):
        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if node == self.head:
            self.head = node.next

        if node == self.tail:
            self.tail = node.prev

        self.count -= 1

    def delete_tail_if_full(self):
        if self.count == self.capacity:
            self.delete(self.tail)
            return self.tail
        return None

    def _p(self):
        s = "\n-----------------\n"
        n = self.head;
        while n:
            s = s + f"{n.key}:{n.value}"
            s = s + "\n----------------\n"
            n = n.next

        return s

    def __str__(self):
        return self._p()
        
    def ___repr__(self):
        return self._p()
