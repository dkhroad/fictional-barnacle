class Stack:
    def __init__(self):
        self.stack = []

    def push(self,value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)
