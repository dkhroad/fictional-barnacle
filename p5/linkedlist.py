class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None



class LinkedList(object):
    def __init__(self):
        self.head = None
        self.last = None

    def add(self,item):
        node = Node(item)
        if self.last:
            self.last.next = node
            self.last = node
        else:
            self.last = node

        if not self.head:
            self.head = self.last


    def next(self):
        n = self.head
        while n:
            yield(n.value)
            n = n.next

        
            
