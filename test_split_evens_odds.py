import unittest

from split_evens_odds import SplitEvensOdds


def build(values):
    lst = SplitEvensOdds()
    lst.build_list_forward(values)
    return lst


def node_ids(lst):
    ids = []
    node = lst._head
    while node is not None:
        ids.append(id(node))
        node = node.next
    return ids


class TestSplitEvensOdds(unittest.TestCase):

    def check_result(self, lst):
        """Tail, tail.next, and count must be right for a result list."""
        values = list(lst)
        self.assertEqual(lst._count, len(values))
        if values:
            self.assertEqual(lst._tail.data, values[-1])
            self.assertIsNone(lst._tail.next)
        else:
            self.assertIsNone(lst._head)
            self.assertIsNone(lst._tail)

    def check_source_empty(self, src):
        self.assertIsNone(src._head)
        self.assertIsNone(src._tail)
        self.assertEqual(src._count, 0)

    def test_mixed(self):
        src = build([1, 2, 3, 4, 5, 6, 7, 8])
        evens, odds = src.split_even_odd()
        self.assertEqual(list(evens), [2, 4, 6, 8])
        self.assertEqual(list(odds), [1, 3, 5, 7])
        self.assertEqual(len(evens) + len(odds), 8)
        self.check_result(evens)
        self.check_result(odds)
        self.check_source_empty(src)

    def test_mixed_keeps_order_with_duplicates_and_negatives(self):
        src = build([10, 13, 14, 18, -3, -4, 13])
        evens, odds = src.split_even_odd()
        self.assertEqual(list(evens), [10, 14, 18, -4])
        self.assertEqual(list(odds), [13, -3, 13])
        self.check_result(evens)
        self.check_result(odds)

    def test_all_even(self):
        src = build([2, 4, 6])
        evens, odds = src.split_even_odd()
        self.assertEqual(list(evens), [2, 4, 6])
        self.assertEqual(list(odds), [])
        self.assertTrue(odds.is_empty())
        self.check_result(evens)
        self.check_result(odds)
        self.check_source_empty(src)

    def test_all_odd(self):
        src = build([1, 3, 5])
        evens, odds = src.split_even_odd()
        self.assertEqual(list(evens), [])
        self.assertEqual(list(odds), [1, 3, 5])
        self.check_result(evens)
        self.check_result(odds)
        self.check_source_empty(src)

    def test_single_even(self):
        src = build([4])
        evens, odds = src.split_even_odd()
        self.assertEqual(list(evens), [4])
        self.assertEqual(len(odds), 0)
        self.assertIs(evens._head, evens._tail)
        self.check_source_empty(src)

    def test_single_odd(self):
        src = build([7])
        evens, odds = src.split_even_odd()
        self.assertEqual(len(evens), 0)
        self.assertEqual(list(odds), [7])
        self.assertIs(odds._head, odds._tail)
        self.check_source_empty(src)

    def test_empty_raises_value_error(self):
        with self.assertRaises(ValueError):
            SplitEvensOdds().split_even_odd()

    def test_same_node_objects_are_moved(self):
        src = build([1, 2, 3, 4, 5])
        before = set(node_ids(src))
        evens, odds = src.split_even_odd()
        after = node_ids(evens) + node_ids(odds)
        self.assertEqual(len(after), len(set(after)))   # no node in both lists
        self.assertEqual(set(after), before)            # same objects, none new, none lost

    def test_results_are_usable_lists(self):
        src = build([1, 2, 3, 4])
        evens, odds = src.split_even_odd()
        evens.append(100)
        odds.prepend(0)
        evens.remove(2)
        self.assertEqual(list(evens), [4, 100])
        self.assertEqual(list(odds), [0, 1, 3])

    def test_source_reusable_after_split(self):
        src = build([1, 2])
        src.split_even_odd()
        src.append(9)
        self.assertEqual(list(src), [9])
        self.assertEqual(len(src), 1)

    def test_inherited_operations_still_work(self):
        lst = SplitEvensOdds()
        lst.build_list_backward([1, 2, 3])
        lst.insert_after(2, 99)
        self.assertEqual(list(lst), [3, 2, 99, 1])
        self.assertEqual(lst.remove_all(99), 1)


if __name__ == "__main__":
    unittest.main()
