import unittest

from singly_linked_list import SinglyLinkedList


def build(values):
    lst = SinglyLinkedList()
    lst.build_list_forward(values)
    return lst


class TestSinglyLinkedList(unittest.TestCase):

    def check_invariants(self, lst):
        """Count, head, tail, and tail.next must all agree."""
        nodes = []
        node = lst._head
        while node is not None:
            nodes.append(node)
            node = node.next
        self.assertEqual(lst._count, len(nodes))
        if lst._count == 0:
            self.assertIsNone(lst._head)
            self.assertIsNone(lst._tail)
        else:
            self.assertIs(lst._tail, nodes[-1])
            self.assertIsNone(lst._tail.next)

    # ---- append / prepend ----
    def test_append_empty(self):
        lst = SinglyLinkedList()
        lst.append(1)
        self.assertEqual(list(lst), [1])
        self.assertIs(lst._head, lst._tail)
        self.check_invariants(lst)

    def test_append_nonempty(self):
        lst = build([1, 2])
        lst.append(3)
        self.assertEqual(list(lst), [1, 2, 3])
        self.check_invariants(lst)

    def test_prepend_empty(self):
        lst = SinglyLinkedList()
        lst.prepend(1)
        self.assertEqual(list(lst), [1])
        self.assertIs(lst._head, lst._tail)
        self.check_invariants(lst)

    def test_prepend_nonempty(self):
        lst = build([2, 3])
        lst.prepend(1)
        self.assertEqual(list(lst), [1, 2, 3])
        self.check_invariants(lst)

    # ---- builders ----
    def test_build_forward(self):
        values = [10, 20, 30, 40, 50]
        lst = SinglyLinkedList()
        lst.build_list_forward(values)
        self.assertEqual(list(lst), [10, 20, 30, 40, 50])
        self.assertEqual(values, [10, 20, 30, 40, 50])
        self.check_invariants(lst)

    def test_build_backward(self):
        values = [10, 20, 30, 40, 50]
        lst = SinglyLinkedList()
        lst.build_list_backward(values)
        self.assertEqual(list(lst), [50, 40, 30, 20, 10])
        self.assertEqual(values, [10, 20, 30, 40, 50])
        self.check_invariants(lst)

    # ---- queries ----
    def test_contains(self):
        lst = build([1, 2, 3])
        self.assertTrue(lst.contains(2))
        self.assertFalse(lst.contains(99))
        self.assertFalse(SinglyLinkedList().contains(1))

    def test_is_empty_len_iter(self):
        lst = SinglyLinkedList()
        self.assertTrue(lst.is_empty())
        self.assertEqual(len(lst), 0)
        self.assertEqual(list(lst), [])
        lst.append(5)
        self.assertFalse(lst.is_empty())
        self.assertEqual(len(lst), 1)

    def test_str(self):
        self.assertEqual(str(build([10, 20, 30])), "Head -> 10 -> 20 -> 30 -> None")
        self.assertEqual(str(SinglyLinkedList()), "Head -> None")

    # ---- insert_after ----
    def test_insert_after_interior(self):
        lst = build([1, 3])
        lst.insert_after(1, 2)
        self.assertEqual(list(lst), [1, 2, 3])
        self.check_invariants(lst)

    def test_insert_after_tail_updates_tail(self):
        lst = build([1, 2])
        lst.insert_after(2, 3)
        self.assertEqual(list(lst), [1, 2, 3])
        self.assertEqual(lst._tail.data, 3)
        self.check_invariants(lst)

    def test_insert_after_missing_raises(self):
        lst = build([1, 2])
        with self.assertRaises(ValueError):
            lst.insert_after(99, 5)
        self.assertEqual(list(lst), [1, 2])
        self.check_invariants(lst)

    # ---- remove ----
    def test_remove_head(self):
        lst = build([1, 2, 3])
        lst.remove(1)
        self.assertEqual(list(lst), [2, 3])
        self.check_invariants(lst)

    def test_remove_interior(self):
        lst = build([1, 2, 3])
        lst.remove(2)
        self.assertEqual(list(lst), [1, 3])
        self.check_invariants(lst)

    def test_remove_tail_updates_tail(self):
        lst = build([1, 2, 3])
        lst.remove(3)
        self.assertEqual(list(lst), [1, 2])
        self.assertEqual(lst._tail.data, 2)
        self.check_invariants(lst)

    def test_remove_only_node(self):
        lst = build([1])
        lst.remove(1)
        self.assertTrue(lst.is_empty())
        self.check_invariants(lst)

    def test_remove_missing_raises(self):
        lst = build([1, 2])
        with self.assertRaises(ValueError):
            lst.remove(99)
        self.assertEqual(len(lst), 2)

    def test_remove_from_empty_raises(self):
        with self.assertRaises(ValueError):
            SinglyLinkedList().remove(1)

    # ---- remove_all ----
    def test_remove_all_many_locations(self):
        lst = build([5, 1, 5, 5, 2, 3, 5])   # head, consecutive, tail
        removed = lst.remove_all(5)
        self.assertEqual(removed, 4)
        self.assertEqual(list(lst), [1, 2, 3])
        self.check_invariants(lst)

    def test_remove_all_everything(self):
        lst = build([7, 7, 7])
        self.assertEqual(lst.remove_all(7), 3)
        self.assertTrue(lst.is_empty())
        self.check_invariants(lst)

    def test_remove_all_no_match_returns_zero(self):
        lst = build([1, 2, 3])
        self.assertEqual(lst.remove_all(99), 0)
        self.assertEqual(list(lst), [1, 2, 3])
        self.check_invariants(lst)

    def test_remove_all_empty_list(self):
        self.assertEqual(SinglyLinkedList().remove_all(1), 0)

    # ---- invariants after a mix of operations ----
    def test_invariants_after_mixed_operations(self):
        lst = SinglyLinkedList()
        lst.append(2)
        lst.prepend(1)
        lst.insert_after(2, 3)
        lst.remove(1)
        lst.remove_all(3)
        self.assertEqual(list(lst), [2])
        self.assertIs(lst._head, lst._tail)
        self.check_invariants(lst)


if __name__ == "__main__":
    unittest.main()
