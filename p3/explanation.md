Huffman encoding and decoding functionality is implemented using HuffEncDec
class.

The primary data structures to provide this functionality are 1) priorityQ which is 
implemented is min-heap tree (see heap.py), 2) hashmap that stored encodings
for each character in the huffman tree for a faster lookup, and binary tree 
representing huffman encoding tree.

The main methods of this class are designed iteratively using test driven
developmen as the following: 

* HuffEncDec(data) 
    constructor that create the object of class HuffEncDec
    based on the data to be encoded. It uses an internal 
    helper method _build_pq() that creates unordered list of 
    tuples (freq,value). The list of tuples is then efficiently
    inserted into priorityQ in O(log n) time.

* build_huffman_tree()
    This method builds a binary huffman tree by repeatedly extracting 
    the top two nodes from the priorityQ and constuct a binary tree with
    parent node with the value that is equal to the sum of the frequencies of
    the indivdual node. The parent node is inserted back into the priorityQ. 
    After inserting the new element (parent node), the priorityQ heap is
    restored to ensure that the node containing the smallest frequency is at
    the root. 
    
    The time complexity of this method is O(log m) where m is the number of
    elements in the priority heap. 


* build_encodings() 
    This method builds a hashmap (python dictionary) for for each unique
    character (leaf node) in the binary huffman tree build during the previous
    step. The encoding for each character is stored as value for character as a
    key in the hashmap.

* encode_data() 
   This method encodes the data into huffman encodings by looking up each
   character encoding in the hashmap created by build_encodings() method.

   Time complexity of this method is O(n), where n is number of characters in 
   the input data to be encoded.

* encode_tree()
    This method serialize (encodes) the huffman tree according to the schema
    specifed in schema.py file. 

* decode_tree()
    This method reverses the work done by the encode_tree() earlies by taking the encoded
    bitstream and construct the huffman tree from it. 

* decode_data()
    This method parses the encoded bitstream, and walks the huffman tree to
    generate the originally encoded data. 
    The time complexity is O(n) where n is the number of characters in the
    decoded data.


The time complexity of huffman_encoding() function is O(n) where n is the number
of characters in the data to be encoded.

The time complexity of the huffman_decoding() function is also linear w.r.t
number of characters in the decoded data. 

    
