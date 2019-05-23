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
        while p_idx >= 0:
            self.reheapify(p_idx)
            p_idx -= 1

    def extract(self):
        last = None
        last = self.heap_array.pop()

        try:
            root = self.heap_array[0];
            self.heap_array[0] = last
            self.reheapify()
            return root.value
        except IndexError:
            return last.value


    def less_than_or_equal(self,idx1,idx2):
        if idx2 < len(self.heap_array):
            # return True if self.heap_array[idx1].value <= self.heap_array[idx2].value else False
            return True if self.cmp_key(self.heap_array[idx1]) <= self.cmp_key(self.heap_array[idx2]) else False
        else:
            return True

    def swap(self,idx1,idx2):
        # import pdb; pdb.set_trace()
        node = self.heap_array[idx1]
        self.heap_array[idx1] = self.heap_array[idx2]
        self.heap_array[idx2] = node

    def reheapify(self,p_idx=0):
        # import pdb; pdb.set_trace()
        l_idx = (p_idx << 1) +1
        r_idx = l_idx + 1
        size = len(self.heap_array)

            
        while p_idx < size and l_idx < size:
            # pick the child most out of order
            m_idx = self.most_out_of_order_idx(l_idx,r_idx)
            # if r_idx < size:
            #     if self.less_than_or_equal(r_idx,l_idx):
            #         m_idx = r_idx 
            #     else: 
            #         m_idx = l_idx
            # else:
            #     m_idx = l_idx

            if not self.swap_if_needed(p_idx,m_idx):
                break
            # if not self.less_than_or_equal(p_idx,m_idx):
            #     self.swap(p_idx,m_idx)
            # else:
            #     break # we are done

            p_idx = (p_idx << 1) + 1 # go to the next level 
            l_idx = (p_idx << 1) + 1
            r_idx = l_idx + 1

    def heapify_after_insert(self):
        size = len(self.heap_array)
        idx = size - 1
        # import pdb; pdb.set_trace()
        while idx > 0 : 
            parent_idx = (idx -1) >> 1  # parent lives at i-1/2
            if not self.less_than_or_equal(parent_idx,idx):
                self.swap(parent_idx,idx)
            else:
                break
            idx = parent_idx

    def __repr__(self):
        return ",".join([str(self.heap_array[i].value) for i in range(len(self.heap_array))])
        
        


     
