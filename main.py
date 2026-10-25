from singly_linked_list import SinglyLinkedList
from split_evens_odds import SplitEvensOdds


def heading(text):
    print(f"\n=== {text} ===")


def main():
    # ---- Part 1: SinglyLinkedList ----
    heading("Part 1: Building lists")
    values = [10, 20, 30, 40, 50]
    print(f"Python list:      {values}")
    forward = SinglyLinkedList()
    forward.build_list_forward(values)
    print(f"Built forward:    {forward}")
    backward = SinglyLinkedList()
    backward.build_list_backward(values)
    print(f"Built backward:   {backward}")
    print(f"Python list after: {values}  (unchanged)")

    heading("Part 1: Insert and remove")
    print(f"Before:                {forward}")
    forward.insert_after(30, 35)
    print(f"insert_after(30, 35):  {forward}")
    forward.insert_after(50, 60)
    print(f"insert_after(50, 60):  {forward}   (tail insert)")
    forward.remove(10)
    print(f"remove(10):            {forward}   (head)")
    forward.remove(60)
    print(f"remove(60):            {forward}   (tail)")
    print(f"Length: {len(forward)}, contains(35): {forward.contains(35)}, "
          f"contains(99): {forward.contains(99)}")

    heading("Part 1: remove_all")
    dupes = SinglyLinkedList()
    dupes.build_list_forward([5, 1, 5, 5, 2, 5])
    print(f"Before:          {dupes}")
    print(f"remove_all(5) -> removed {dupes.remove_all(5)}")
    print(f"After:           {dupes}")
    print(f"remove_all(99) -> removed {dupes.remove_all(99)}  (no matches)")

    # ---- Part 2: SplitEvensOdds ----
    heading("Part 2: Split evens and odds")
    source = SplitEvensOdds()
    source.build_list_forward([1, 2, 3, 4, 5, 6, 7, 8])
    print(f"Source before split: {source}")
    evens, odds = source.split_even_odd()
    print(f"Even list:           {evens}  (count {len(evens)})")
    print(f"Odd list:            {odds}  (count {len(odds)})")
    print(f"Source after split:  {source}  (empty: {source.is_empty()})")

    heading("Part 2: Inherited operations still work")
    evens.append(10)
    odds.prepend(0)
    odds.remove(3)
    print(f"Even list after append(10):            {evens}")
    print(f"Odd list after prepend(0), remove(3):  {odds}")

    # ---- Error handling ----
    heading("Error handling")
    for label, action in [
        ("remove(99) on odd list", lambda: odds.remove(99)),
        ("insert_after(99, 1) on odd list", lambda: odds.insert_after(99, 1)),
        ("split_even_odd() on empty list", lambda: SplitEvensOdds().split_even_odd()),
    ]:
        try:
            action()
        except ValueError as error:
            print(f"{label}: ValueError - {error}")


if __name__ == "__main__":
    main()
