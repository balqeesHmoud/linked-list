from Node import Node

class LinkedList:
    """A class representing a singly linked list."""
    def __init__(self):
        self.head = None

    def __getitem__(self, index):
        """Retrieve the element at the specified index using the [] operator."""
        current = self.head
        count = 0

        while current is not None:
            if count == index:
                return current.data
            current = current.next
            count += 1

        raise IndexError("Index out of range")

    def __len__(self):
        """Return the number of elements in the linked list."""
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next

        return count

    def __init__(self, values=None):
        """Initialize the linked list with optional initial values."""
        self.head = None

        if values is not None:
            for value in values:
                self.append(value)

    def __str__(self):
        """Return a string representation of the linked list."""
        elements = []
        current = self.head

        while current is not None:
            elements.append(str(current.data))
            current = current.next

        return " -> ".join(elements)

    def append(self, value):
        """Add a new node with the given value at the end of the linked list."""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
