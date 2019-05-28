The LRU_Cache is implemented as queue. 
The queue is implement using a DoubleLinkedList.

Any items accessed or added to the cache is moved to the head of the queue. 
If the queue becomes full, the cached items at the tail is evicted from the 
queue. 

Time complexity: 
The worst case time complexity of adding or removing an item is O(1) because
it only takes constant amount of time to add or remove an element at head or
tail of the queue. 
