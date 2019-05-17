from collections import deque

class Queue:
    def __init__(self,size=None):
        if size == None:
            self.q = deque()
        else:
            self.q = deque(maxlen=size)
    
    def size(self):
        return self.q.maxlen

    def enq(self,value):
        self.q.appendleft(value)

    def deq(self):
        try:
            return self.q.pop()
        except IndexError:
            return None

