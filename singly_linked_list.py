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
