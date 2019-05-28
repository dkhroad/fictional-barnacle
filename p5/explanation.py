The blockchain is implemented using a single linked list as requested. 
The functionality is provided by the following two main classes. 

1. Block - its constructor creates a block from the given data, timestamp in seconds, block
height and hash of the previous block. The `calc_hash` function computes the
assigns a sha256 hash for the content of the block. 

I am unable to get the information about the time complexity of python hashlib
library. For the Block constructor, all operations other than calc_hash() are
of O(1). The overall time complexity is expected to be dominated by the
`update` function in the hashlib libaray. My best guess is O(n) where n is the number
of bytes in the block data.

2. Blockchain - this class implements the blockchain functionality using a
linked list. The time complexity of the `add` function is O(1), which is same
as adding an element to a linked list. The method `getblock` has the worst case
time complexity of O(n) where n are the number of blocks in the blockchain.
