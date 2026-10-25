from node import Node


class SinglyLinkedList:
    """Singly linked list that tracks _head, _tail, and _count."""

    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    # ---- basic queries ----
    def is_empty(self):
        return self._count == 0

    def __len__(self):
        return self._count

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current.data
            current = current.next

    def __str__(self):
        parts = ["Head"] + [str(v) for v in self] + ["None"]
        return " -> ".join(parts)

    def contains(self, value):
        current = self._head
        while current is not None:
            if current.data == value:
                return True
            current = current.next
        return False

    # ---- core operations ----
    def append(self, value):
        """Add a node after the tail. O(1)."""
        new_node = Node(value)
        if self._tail is None:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._count += 1

    def prepend(self, value):
        """Add a node before the head. O(1)."""
        new_node = Node(value, self._head)
        self._head = new_node
        if self._tail is None:
            self._tail = new_node
        self._count += 1
