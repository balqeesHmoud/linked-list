# test_linked_list.py
import unittest
from linkedlist.LinkedList import LinkedList  # Correct import path for LinkedList

def test_init_empty_list():
    # Test initializing an empty LinkedList
    my_list = LinkedList()
    assert my_list.head is None
    assert len(my_list) == 0
    assert str(my_list) == ""

def test_add_and_access():
    # Test adding elements and accessing them by index
    my_list = LinkedList()
    my_list.append(5)
    my_list.append(10)
    my_list.append(15)

    assert my_list[0] == 5
    assert my_list[1] == 10
    assert my_list[2] == 15

    # Test accessing out-of-bound index
    with unittest.TestCase().assertRaises(IndexError):
        my_list[3]

def test_length():
    # Test calculating the length of the LinkedList
    my_list = LinkedList()
    assert len(my_list) == 0

    my_list.append(5)
    assert len(my_list) == 1

    my_list.append(10)
    my_list.append(15)
    assert len(my_list) == 3

def test_str_representation():
    # Test string representation of the LinkedList
    my_list = LinkedList()
    assert str(my_list) == ""

    my_list.append(5)
    assert str(my_list) == "5"

    my_list.append(10)
    my_list.append(15)
    assert str(my_list) == "5 -> 10 -> 15"

if __name__ == '__main__':
    # Run all test functions using unittest
    unittest.main()
