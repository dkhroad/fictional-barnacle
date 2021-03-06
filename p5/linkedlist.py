class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None



class LinkedList(object):
    def __init__(self):
        self.head = None
        self.last = None
        self.current = None

    def add(self,item):
        node = Node(item)
        if self.last:
            self.last.next = node
            self.last = node
        else:
            self.last = node

        if not self.head:
            self.head = self.last


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

        
            
