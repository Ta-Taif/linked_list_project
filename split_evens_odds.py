from singly_linked_list import SinglyLinkedList


class SplitEvensOdds(SinglyLinkedList):
    """SinglyLinkedList that can split itself into even and odd lists."""

    def split_even_odd(self):
        """Move every existing node into an even list or an odd list.

        Only node references change. No Node objects are created, and
        append/prepend/remove are not used. The source list ends up empty.
        Returns (even_list, odd_list).
        """
        if self.is_empty():
            raise ValueError("split_even_odd failed: cannot split an empty list")

        even_list = SplitEvensOdds()
        odd_list = SplitEvensOdds()

        # Keep a cursor to the first node, then empty the source list.
        current = self._head
        self._head = None
        self._tail = None
        self._count = 0

        while current is not None:
            # Save the next node BEFORE cutting the link.
            next_node = current.next
            current.next = None

            destination = even_list if current.data % 2 == 0 else odd_list
            if destination._tail is None:
                destination._head = current
                destination._tail = current
            else:
                destination._tail.next = current
                destination._tail = current
            destination._count += 1

            current = next_node

        return even_list, odd_list
