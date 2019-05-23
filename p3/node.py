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

    def is_leaf_node(self):
        return not (self.right or self.left)
