import tree
import schema

class HuffEncDec:
    def __init__(self):
        self.nodedict = {}
        self.tree = tree.Tree()
        self.encodings = {}

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
        self.tuples =  tuples
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

    def build_huffman_tree(self,freqlist):
        # while tuple_list[0] != tree_root
        #   build_huffman_tree_node with  the first two elemments
        #   add the new node to the tuple list
        #   sort the tuple list
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


    def trim(self):
        def _trim(node):
            node.value = node.value[0]
            if node.has_left_child():
                _trim(node.get_left_child())
            if node.has_right_child():
                _trim(node.get_right_child())

        root = self.tree.get_root()
        _trim(root)




    def encode(self,value):
        root = self.tree.get_root()
        print(self.tree)

        def _encode(node):
            if node.value[1] == value:
                return

            if node.has_left_child():
                encoding.append("0")
                _encode(node.get_left_child())

            if node.has_right_child():
                encoding.append("1")
                _encode(node.get_right_child())

        _encode(root)
        return "".join(encoding)



    def encode_tree(self):
        def _encode_tree(node):
            if node.is_leaf_node():
                yield(f"{schema.LEAF_NODE}{bin(node.value[1])[2:].zfill(schema.BITS_PER_VALUE)}")
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
        return tree.Tree(root)
        



def huffman_encoding(data):
    pass

def huffman_decoding(data):
    pass
