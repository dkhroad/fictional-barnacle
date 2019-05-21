import tree
import schema

class HuffEncDec:
    def __init__(self):
        self.nodedict = {}
        self.tree = tree.Tree()
        self.encodings = {}
        self.freqlist = None

    def _get_tree_node(self,key):
        return self.nodedict[key]

    def _get_freq(self,letters):
        freqdict = {}
        for c in letters:
            if c in freqdict:
                freqdict[c] += 1
            else:
                freqdict[c] = 1

        tuples = [(v, k) for k, v in freqdict.items()]
        tuples.sort(key=lambda item: item[0])
        self.freqlist =  tuples
        return tuples

    def build_huffman_tree_node(self,tuple_left,tuple_right,hufftree):

        new_tuple = (tuple_left[0]+tuple_right[0],str(tuple_left[1]) + '-' + str(tuple_right[1]))
        node = tree.Node(new_tuple)
        self.nodedict[new_tuple] = node
       
        try:
            tuple_left_node = self._get_tree_node(tuple_left)
            node.add_left_child(tuple_left_node)
        except KeyError:
            tuple_left_node = tree.Node(tuple_left)
            self.nodedict[tuple_left] = tuple_left_node
            node.add_left_child(tuple_left_node)

        try:
            tuple_right_node = self._get_tree_node(tuple_right)
            node.add_right_child(tuple_right_node)
        except KeyError:
            tuple_right_node = tree.Node(tuple_right)
            self.nodedict[tuple_right] = tuple_right_node
            node.add_right_child(tuple_right_node)

        if hufftree:
            hufftree.set_root(node)
        else:
            hufftree = tree.Tree(node)
        return hufftree

    def build_huffman_tree(self,freqlist=None):
        if not freqlist:
            freqlist = self.freqlist

        hufftree = None
        while len(freqlist) > 1:
            hufftree = self.build_huffman_tree_node(freqlist[0],freqlist[1],hufftree)
            freqlist = self.add_to_freq_list(freqlist,hufftree.get_root().value)

        assert freqlist[0] == hufftree.get_root().value
        self.tree = hufftree
        return hufftree


    def add_to_freq_list(self,tuples,this,sort=True):
        tuples = tuples[2:] # this is not very optimal
        tuples.append(this)
        if sort:
            tuples.sort(key = lambda item: item[0])
        return tuples


    def build_encodings(self):
        """
        builds encoding for each character in the tree, and 
        stores it in self.encoding dictionary
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
        # make sure we have a tree
        assert self.tree.get_root() != None
        encoded_data = "".join([self.encodings[c] for c in data])
        # prefix the encoded data with number of chars in the data
        data_len = bin(len(data))[2:].zfill(schema.BITS_PER_VALUE)
        return data_len + encoded_data

    def _encode_node_value(self,node):
        if isinstance(node.value[1],str):
            v = ord(node.value[1])
        else:
            v = node.value[1]

        return bin(v)[2:].zfill(schema.BITS_PER_VALUE)

    def encode_tree(self):
        def _encode_tree(node):
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
        def _read_bits():    
            # import pdb; pdb.set_trace()
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
        print("root: ",root.value)
        self.tree = tree.Tree(root)
        return self.tree
        

    def decode_data(self,encoded_data,decoded_tree=None):

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
    huffencdec = HuffEncDec() 
    huffencdec._get_freq(data)
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
