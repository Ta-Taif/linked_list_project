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

    def insert_after(self, existing_value, new_value):
        """Insert new_value after the first node holding existing_value."""
        current = self._head
        while current is not None and current.data != existing_value:
            current = current.next
        if current is None:
            raise ValueError(
                f"insert_after failed: value {existing_value!r} not found in list")
        new_node = Node(new_value, current.next)
        current.next = new_node
        if current is self._tail:
            self._tail = new_node
        self._count += 1

    def remove(self, value):
        """Remove the first node holding value."""
        previous = None
        current = self._head
        while current is not None and current.data != value:
            previous = current
            current = current.next
        if current is None:
            raise ValueError(
                f"remove failed: value {value!r} not found in list")
        self._unlink(previous, current)

    def _unlink(self, previous, current):
        """Helper: remove current (whose predecessor is previous)."""
        if previous is None:
            self._head = current.next
        else:
            previous.next = current.next
        if current is self._tail:
            self._tail = previous
        current.next = None
        self._count -= 1

    def remove_all(self, value):
        """Remove every node holding value. Return how many were removed."""
        removed = 0
        previous = None
        current = self._head
        while current is not None:
            next_node = current.next
            if current.data == value:
                self._unlink(previous, current)
                removed += 1
            else:
                previous = current
            current = next_node
        return removed

    # ---- project extensions ----
    def build_list_forward(self, values):
        """Build list in the same order as values (uses append)."""
        for value in values:
            self.append(value)

    def build_list_backward(self, values):
        """Build list in reverse order of values (uses prepend)."""
        for value in values:
            self.prepend(value)
