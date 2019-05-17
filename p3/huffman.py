import tree
class HuffEncDec:
    def __init__(self):
        pass

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

    def build_huffman_tree(self,tuple_left,tuple_right,hufftree):
        if hufftree is None:
            node = tree.Node((tuple_left[0]+tuple_right[0],None))
            node.add_left_child(tuple_left)
            node.add_right_child(tuple_right)
            hufftree = tree.Tree(node)

        return hufftree
        



def huffman_encoding(data):
        pass

def huffman_decoding(data):
    pass
