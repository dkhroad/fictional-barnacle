import DoubleLinkedList
class LRU_Cache(object):
    def __init__(self,capacity=5):
        self.cache = DoubleLinkedList.DoubleLinkedList(capacity)
        self.dict = {}

    def get(self,key):
        try:
            node = self.dict[key]
            self.cache.delete(node)
            self.cache.add_to_head(node)
            # print("node.value",node.value)
            return node.value
        except KeyError:
            return -1

    def set(self,key,value):
        deleted=self.cache.delete_tail_if_full()
        if deleted: 
            del self.dict[deleted.key]
        node = DoubleLinkedList.Node(key,value)
        self.dict[key] = node
        self.cache.add_to_head(node)
        

            

            

