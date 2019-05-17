import queue
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def add_left_child(self, node):
        self.left = node

    def add_right_child(self, node):
        self.right = node

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

class Tree:
    def __init__(self,value=None):
        if value is not None:
            if isinstance(value,Node):
                self.root = value
            else:
                self.root= Node(value)

    def set_root(self,value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def _pre_order_traversal(self,node):
        yield(node.value)
        if node.has_left_child():
            for nleft in self._pre_order_traversal(node.get_left_child()):
                yield(nleft)
        if node.has_right_child():
            for nright in self._pre_order_traversal(node.get_right_child()):
                yield(nright)


    def pre_order_traversal(self):
        return self._pre_order_traversal(self.root) 

    def _bft(self,node): 
        visit = list()
        q = queue.Queue()

        while node is not None:
            visit.append(node.value)
            if node.has_left_child():
                q.enq(node.get_left_child())
            if node.has_right_child():
                q.enq(node.get_right_child())
            node = q.deq()

        return visit

    def bf_traversal(self):
        return self._bft(self.root)








