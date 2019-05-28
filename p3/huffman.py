import tree
import heap as pqueue
import schema


class HuffEncDec:
    def __init__(self,data=None):
        """
        Creates frequency list of all the characters in the data.
        and from that creates a priorityQ of (frequency,letter) 
        tuple. 

        Complexity: O(n), where n is the number of characters in the
        given data. 
        """

        self.nodedict = {}
        self.tree = tree.Tree()
        self.encodings = {}
        self.pqueue = pqueue.Heap(key=lambda n: n.value[0])
        if data:
            self._build_pq(data)

    def _get_tree_node(self,key):
        return self.nodedict[key]

    def _build_pq(self,letters):
        """
        internal function to create a priorityQ based 
        on the frequency of the letters

        Time Complexity: O(n), where n is the number of letters

        The time complexity of adding a list of nodes is O(n) instead of 
        O(n log n). This is achieved by heapifying the priorityQ only 
        after all elements have been added to the priorityQ's internal array
        instead of heapifying after each insert. See methods `insert` and
        `heapify` in heap.py for more details
        """
        freqdict = {}
        for c in letters:
            if c in freqdict:
                freqdict[c] += 1
            else:
                freqdict[c] = 1

        freqlist = [(v, k) for k, v in freqdict.items()]
        self.pqueue.insert(freqlist)

    def build_huffman_tree_node(self,tuple_left,tuple_right,hufftree):
        """
        constructs a huffman (binary) tree node for the two tuples provided
        in arguments `tuple_left` and `tuple_right`. These are the 
        frequency tuples in the form (frequency, letter). The binary
        tree nodes are stored in a hashmap (python dictionary) with 
        a unique key that is constucted based on frequencies of their
        children. This helps is in constructing the huffman tree properly
        by linking nodes of an already existing tree.

        After constructing the nodes for the tuples provided. A new node
        with the value equal to the sum of the frequencies  
        in the tuple_left and tuple_right arguments is created and binary
        tree is constructed with this node as a parent node

        Finally, the create node is added as the root of the tree provided
        as the 3rd argument.

        Time complexity: The average worst case time complexity is O(1) 
        
        """

        def freq(node):
            """
            helper function to get the frequency from the value tuple
            """
            return node.value[0]

        new_tuple = (freq(tuple_left) + freq(tuple_right),None)
        node = tree.Node(new_tuple)
       
        node.add_left_child(tuple_left)
        node.add_right_child(tuple_right)

        if hufftree:
            hufftree.set_root(node)
        else:
            hufftree = tree.Tree(node)
        return hufftree

    def build_huffman_tree(self):
        """
        Builds a complete huffman tree (internally a binary tree) 
        based on the elements (letter frequencies) in the priorityQ using
        the following algorithm:

        1. Extract the top two elements (nodes contains letters with
           the highest frequencies. 
        2. Build a tree node for these top two elements. 
        3  Insert a frequency tuple corresponding to the tree node created
           back into the priorityQ. 


        Time Complexity: O(n log n) where n is the number of elements in 
        the priorityq

        While iterating over the priorityQ, there 2 extractions and 
        1 inserts each with the time complexity of O(log n).
        where n is the number of elements (tree nodes containing 
        frequencies of letters) in the priorityQ. Therefore the overall
        time complexity is O(n * 3 log n). Ignoring constants
        and lower order terms, the time complexity is O(n log n)
        """

        hufftree = None
        try: 
            n1 = self.pqueue.extract()
        except IndexError:
            n1 = None

        try:
            n2 = self.pqueue.extract()
        except IndexError:
            n2 = None

        try:
            while n1 and n2:
                hufftree = self.build_huffman_tree_node(n1,n2,hufftree)
                self.pqueue.insert(hufftree.get_root())
                n1 = self.pqueue.extract()
                n2 = self.pqueue.extract()
        except IndexError:
            pass

        if not hufftree:
            hufftree = tree.Tree(n1)

        
        self.tree = hufftree
        return hufftree


    def build_encodings(self):
        """
        builds encoding for each character in the tree, and 
        stores it in self.encoding dictionary

        Time complexity: O(log n)
        where n is the number of elements in the encoding tree
        """

        def _encode(node,encoding):
            if node.is_leaf_node():
                self.encodings[node.value[1]] = "".join(encoding)

            if node.has_left_child():
                encoding.append("0")
                _encode(node.get_left_child(),encoding)
                encoding.pop()

            if node.has_right_child():
                encoding.append("1")
                _encode(node.get_right_child(),encoding)
                encoding.pop()

        _encode(self.tree.get_root(),[])
        return self.encodings

    def encode_data(self,data=None):
        """
        encodes the data by looking up its encoding in the self.encodings
        dictionary

        Time complexity: O(n), where n is the number of chars/symbols in the
        data. 

        Note that that worst case time complexity to look up encodings for 
        each character is O(m), where m is the size of encodings hashmap. 
        For practical purposes, m << n. Therefore, we are ignoring the
        hashtable look up complexity. 
        """
        # make sure we have a tree
        assert self.tree.get_root() != None
        encoded_data = "".join([self.encodings[c] for c in data])
        # prefix the encoded data with number of chars in the data
        data_len = bin(len(data))[2:].zfill(schema.BITS_PER_VALUE)
        return data_len + encoded_data


    def _encode_node_value(self,node):
        """
        encode the value of a node into the number of bits specified in the
        schema.
        """
        if isinstance(node.value[1],str):
            v = ord(node.value[1])
        else:
            v = node.value[1]

        return bin(v)[2:].zfill(schema.BITS_PER_VALUE)

    def encode_tree(self):
        """
        returns a string repesenting the huffman tree encoding
        
        encoding is done as per schema specified in schema.py
        The encoding schema grammer can be described as:

        <header_bits>(<leaf_node> | non_leaf_node>)* 
        <non_leaf_node> :  schema.NON_LEAF_NODE 
        <leaf_node> : schema.LEAF_NODE<+>schema.BITS_PER_VALUE
        <+>         : ''

        Time complexity: O(log n) where n is the number of elements in the tree
        """
        def _encode_tree(node):
            """
            helper function generator that lazily encode each tree node
            """
            if node.is_leaf_node():
                yield(f"{schema.LEAF_NODE}{self._encode_node_value(node)}")
            else:
                yield(f"{schema.NON_LEAF_NODE}")

            if node.has_left_child():
                for nleft in _encode_tree(node.get_left_child()):
                    yield(nleft)
            if node.has_right_child():
                for nright in _encode_tree(node.get_right_child()):
                    yield(nright)

        s1 = bin(schema.BITS_PER_VALUE)[2:].zfill(schema.HEADER_BITS)
        s2 = "".join([bit for bit in _encode_tree(self.tree.get_root())])
        return f"{s1}{s2}"

    def decode_tree(self,encoded_tree):
        """
        construct a huffman tree from the encoded and serialized bitstream
        Time complexity: O(m) where m is the number of symbols/chars used in the tree
        """
        def _read_bits():    
            """
            helper generator function that lazily iterate over the encoded
            huffman tree bitstream to return a single encoded leaf or non leaf node 
            """
             
            yield encoded_tree[:schema.HEADER_BITS]

            current_idx = schema.HEADER_BITS
            end = len(encoded_tree[current_idx:])

            while current_idx < end:
                yield encoded_tree[current_idx]
                current_idx += 1
                if encoded_tree[current_idx-1] == str(schema.LEAF_NODE):
                    yield encoded_tree[current_idx:current_idx+schema.BITS_PER_VALUE]
                    current_idx += schema.BITS_PER_VALUE
                        

        def _makeTree(bitstream):
            """
            recursively construct a huffman tree from the encoding bit stream
            based on the schema specified in schema.py

            Time Complexity: O(m) where m is the no of individual unique chars
            used in the data. Note that indivdual number of chars are typically much
            smaller than total no of chars encoded or decoded. For example, the
            value of m will be 127 to decode any size of ascii data.
            """
            try:
                b = next(bitstream)
                if b == str(schema.LEAF_NODE):
                    n = next(bitstream)
                    return tree.Node(int(n,2))

                nodeleft = _makeTree(bitstream)
                noderight = _makeTree(bitstream)
                if noderight == None:
                    return  nodeleft

                node = tree.Node('*')
                node.add_left_child(nodeleft)
                node.add_right_child(noderight)
                return node
            except StopIteration:
                return None


        root = _makeTree(_read_bits())
        self.tree = tree.Tree(root)

        return self.tree
        

    def decode_data(self,encoded_data,decoded_tree=None):
        """
        decodes the huffman encoded data based schema specifed in schema.py
        Time complexity: O(n) where n are the number of chars in the encoded
        data 
        """
        if not decoded_tree:
             decoded_tree = self.tree

        data_len = int(encoded_data[:schema.BITS_PER_VALUE],2) 
        idx = schema.BITS_PER_VALUE
        encoded_data = encoded_data[schema.BITS_PER_VALUE:]
        idx = 0
        data = list()

        for i in range(data_len):
            node = decoded_tree.get_root()
            while not node.is_leaf_node():
                next_bit = int(encoded_data[idx])
                idx += 1
                if next_bit:
                    node = node.get_right_child()
                else:
                    node = node.get_left_child()
            assert node.is_leaf_node() == True
            data.append(chr(node.value))

        return "".join(data)



def huffman_encoding(data):
    huffencdec = HuffEncDec(data) 
    huffencdec.build_huffman_tree()
    huffencdec.build_encodings()
    encoded_data = huffencdec.encode_data(data)
    encoded_tree = huffencdec.encode_tree()
    return (encoded_data,encoded_tree)

def huffman_decoding(encoded_data,encoded_tree):
    huffencdec = HuffEncDec()
    huffencdec.decode_tree(encoded_tree)
    data = huffencdec.decode_data(encoded_data)
    return data


if __name__ == "__main__":
    encoded_data,encoded_tree = huffman_encoding("The bird is the word")
    data = huffman_decoding(encoded_data,encoded_tree)
    print(data)
