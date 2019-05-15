from  DoubleLinkedList import *
def test_add_to_head():
    ll = DoubleLinkedList(3)
    n = Node(3,5)
    ll.add_to_head(n)
    assert ll.head.key == n.key
    assert ll.head.value == n.value
    assert ll.tail.key == n.key
    assert ll.tail.value == n.value
    
    n2 = Node('a',1)
    ll.add_to_head(n2)
    assert ll.head.key == n2.key
    assert ll.head.value == n2.value
    assert ll.tail.key == n.key
    assert ll.tail.value == n.value

    # print(ll)

    ll.delete(n)
    assert ll.head.key == n2.key
    assert ll.head.value == n2.value
    assert ll.tail.key == n2.key
    assert ll.tail.value == n2.value

    n3 = Node('b',2)
    ll.add_to_head(n3)
    assert ll.head.key == n3.key
    assert ll.head.value == n3.value
    assert ll.tail.key == n2.key
    assert ll.tail.value == n2.value
    print(ll)

    n4 = Node('c',3)
    ll.add_to_head(n4)
    n5 = Node('d',4)
    ll.add_to_head(n5)
    print(ll)

    assert ll.head.key == n4.key
    assert ll.head.value == n4.value
    assert ll.tail.key == n2.key
    assert ll.tail.value == n2.value
    assert ll.count == 3
    ll.delete(n4)

    assert ll.head.key == n3.key
    assert ll.head.value == n3.value
    assert ll.tail.key == n2.key
    assert ll.tail.value == n2.value
    assert ll.count == 2


