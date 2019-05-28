from node import *

class Heap:
    def __init__(self,value=None,key=None):
        self.root = self.create_node_from_value_if_needed(value) 
        self.heap_array = list()
        if key:
            self.cmp_key = key
        else:
            self.cmp_key = lambda k: k.value

    def create_node_from_value_if_needed(self,value):
        if value: 
            if not isinstance(value,Node):
                value = Node(value)

        return value

    def insert(self,value):
        """
        In order to achieve a more efficient time complexity, 
        if value is a list of elements to insert in the heap,
        the heapify process is done only once after all elements are addded 
        to the internal array instead of doing heapify operation 
        after each insert.

        Therefore, when inserting a list of items into the heap, the
        time complexity is O(n) where n is the number of element in the 
        heap. 

        Time complexity of adding a single element is O(log n)
        """
        if isinstance(value,list):
            nodes = [self.create_node_from_value_if_needed(v) for v in value]
            [self.heap_array.append(n) for n in nodes]
            self.heapify(len(self.heap_array)>>1)
        else:
            value = self.create_node_from_value_if_needed(value)
            self.heap_array.append(value)
            self.heapify_after_insert()


    def most_out_of_order_idx(self,l_idx,r_idx):
        if r_idx < len(self.heap_array):
            return l_idx if self.less_than_or_equal(l_idx,r_idx) else r_idx
        else:
            return l_idx

    def swap_if_needed(self,m_idx,l_idx):
        if l_idx < len(self.heap_array):
            if not self.less_than_or_equal(m_idx,l_idx):
                self.swap(m_idx,l_idx)
                return True
        return False


    def heapify(self,p_idx):
        """
        helper method to repeatedly build a binary heap for a root 
        node at index i in the heap array, where index i: p_idx <= i <=0 
        
        Time Complexity: O(n * log n) 
        
        wher n is the total number of elements in the heap.

        If p_idx is < (n/2 -1), the tigher time analysis reveals 
        that time complexity is O(n)
        """
        while p_idx >= 0:
            self.reheapify(p_idx)
            p_idx -= 1

    def extract(self):
        """
        extract the element from the top of the heap.
        and reheapify 

        Time complexity: O(log n)
        """
        last = None
        last = self.heap_array.pop()

        try:
            root = self.heap_array[0];
            self.heap_array[0] = last
            self.reheapify()
            return root
        except IndexError:
            return last


    def less_than_or_equal(self,idx1,idx2):
        if idx2 < len(self.heap_array):
            # return True if self.heap_array[idx1].value <= self.heap_array[idx2].value else False
            return True if self.cmp_key(self.heap_array[idx1]) <= self.cmp_key(self.heap_array[idx2]) else False
        else:
            return True

    def swap(self,idx1,idx2):
        node = self.heap_array[idx1]
        self.heap_array[idx1] = self.heap_array[idx2]
        self.heap_array[idx2] = node


    def reheapify(self,p_idx=0):
        """
        rebuild the binary heap starting from index p_idx

        Time complexity: O(log n)
        """
        l_idx = (p_idx << 1) +1
        r_idx = l_idx + 1
        size = len(self.heap_array)
            
        while p_idx < size and l_idx < size:
            # pick the child most out of order
            m_idx = self.most_out_of_order_idx(l_idx,r_idx)

            if not self.swap_if_needed(p_idx,m_idx):
                break

            p_idx = (p_idx << 1) + 1 # go to the next level 
            l_idx = (p_idx << 1) + 1
            r_idx = l_idx + 1

    def heapify_after_insert(self):
        """
        the last inserted element in the heap array might violate the 
        heap. Start at the bottom most level and fix the heap by 
        moving each level up until no swap is required.

        Time complexity: O(log n)
        """
        size = len(self.heap_array)
        idx = size - 1
        while idx > 0 : 
            parent_idx = (idx -1) >> 1  # parent lives at i-1/2
            if not self.less_than_or_equal(parent_idx,idx):
                self.swap(parent_idx,idx)
            else:
                break
            idx = parent_idx

    def __repr__(self):
        return ",".join([str(self.heap_array[i].value) for i in range(len(self.heap_array))])
        
        


     
