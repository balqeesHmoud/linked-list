

# Linked List Implementation

This repository contains a Python implementation of a singly linked list, along with a test suite to verify its functionality.

## Files

- **Node.py**: Defines the `Node` class used in the linked list, representing individual nodes with a value and a pointer to the next node.
  
- **LinkedList.py**: Implements the `LinkedList` class, which manages a collection of nodes. It supports operations like appending nodes, accessing nodes by index, calculating the length, and generating a string representation of the list.
  
- **test_linked_list.py**: Contains unit tests using the `unittest` framework to validate the functionality of the `LinkedList` class. Tests cover initialization, appending nodes, accessing nodes by index, calculating the length, and verifying string representations.

## Usage

To use the `LinkedList` class in your own projects:

1. **Import the LinkedList class**:
   ```python
   from linkedlist.LinkedList import LinkedList
   ```

2. **Create a new LinkedList**:
   ```python
   my_list = LinkedList()
   ```

3. **Operations**:
   - **Append elements**:
     ```python
     my_list.append(value)
     ```
   - **Access elements by index**:
     ```python
     element = my_list[index]
     ```
   - **Calculate length**:
     ```python
     length = len(my_list)
     ```
   - **String representation**:
     ```python
     string_rep = str(my_list)
     ```

## Running Tests

To run the test suite and verify the functionality of the `LinkedList` class:

```sh
pytest test/test_linked_list.py
```

---

In this summary, replace `value` with the actual value you wish to add