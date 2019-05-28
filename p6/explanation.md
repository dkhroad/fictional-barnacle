This problem is solved using a single linked list. The next() method
is implemented using python iterator functions. This makes it easier to 
lazily iterate over of the members of the linked list. This lazy retrieval method 
also helps us with space complexity a bit as we don't accumulate all member in
a data structure before returning them to the caller. 

The time complexity of add a value to the linked list is O(1) as 
we keep track of the last element added to the list. This saves us
extra work required to iterate the list from the beginning. 

The time complexity to get an element from a list is also O(1). Therefore
the time complexity of getting/iterating over all elements of the list is O(n)

The time complexity of doing the union operation on the members of the given
two linked lists is O(m + n) where m and n are the size linked lists passed as
arguments respectively.

The time complexity of the intersection method is O(m * n), where m and n are
the size of the linked lists passed in as arguments. 

Essentially, the time complexity of these methods is the same as the time
complexity of python set operations. 

The test are implemented using unittest framework in file test_linkedlist.py

