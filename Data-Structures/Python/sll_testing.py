from Singly_Linked_list import SinglyLL

def test_insert_at_beginning():
    ll = SinglyLL()
    ll.insert_at_beginning(1)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(3)
    assert ll.head.data == 3
    assert ll.head.next.data == 2
    assert ll.head.next.next.data == 1
    assert ll.head.next.next.next is None
    print('test_insert_at_beginning passed')

def test_insert_at_end():
    ll = SinglyLL()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    assert ll.head.data == 1
    assert ll.head.next.data == 2
    assert ll.head.next.next.data == 3
    assert ll.head.next.next.next is None
    print('test_insert_at_end passed')

def test_insert_at_index():
    ll = SinglyLL()
    ll.insert_at_index(1, 0)

    ll.insert_at_index(2, 1)

    ll.insert_at_index(3, 2)

    ll.insert_at_index(4, 1)

    assert ll.head.data == 1
    assert ll.head.next.data == 4
    assert ll.head.next.next.data == 2
    assert ll.head.next.next.next.data == 3
    assert ll.head.next.next.next.next is None
    print('test_insert_at_index passed')

def test_delete_at_beginning():
    ll = SinglyLL()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.delete_at_beginning()
    assert ll.head.data == 2
    assert ll.head.next.data == 3
    assert ll.head.next.next is None
    print('test_delete_at_beginning passed')

def test_delete_at_end():
    ll = SinglyLL()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.delete_at_end()
    assert ll.head.data == 1
    assert ll.head.next.data == 2
    assert ll.head.next.next is None
    print('test_delete_at_end passed')

def test_delete_at_index():
    ll = SinglyLL()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.delete_at_index(1)
    assert ll.head.data == 1
    assert ll.head.next.data == 3
    assert ll.head.next.next is None
    print('test_delete_at_index passed')

def test():
    ...
    # test_insert_at_beginning()
    # test_insert_at_end()
    # test_insert_at_index()
    # test_delete_at_beginning()
    # test_delete_at_end()
    # test_delete_at_index()

def mytest():
    myll = SinglyLL()
    myll.insert_at_beginning(10)
    myll.insert_at_beginning(30)
    myll.insert_at_beginning(11)
    myll.insert_at_end(20)
    myll.insert_at_end(40)
    myll.insert_at_index(50, 1)
    myll.insert_at_index(60, 4)
    myll.print_list() # 11 -> 50 -> 30 -> 10 -> 60 -> 20 -> 40 -> None
    print(myll.search(30))
    print(myll.search_recursive(myll.head, 11))

    myll.update_data(30, 5)
    myll.update_idx(0, 7)
    myll.print_list() # 7 -> 50 -> 5 -> 10 -> 60 -> 20 -> 40 -> None

    myll.delete_at_beginning()
    myll.delete_at_end()
    myll.delete_at_index(1)
    myll.print_list() # 50 -> 5 -> 10 -> 60 -> 20 -> None


if __name__ == '__main__':
    # test()
    # mytest()
    ...