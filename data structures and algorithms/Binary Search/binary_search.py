#!/usr/bin/env python

class BinarySearch():
    def __init__(self, lst: list):
        self.lst = list(sorted(lst))

    def search(self, target):
        """
        Returns a position of a target in the list.\n
        If the target is not found, then the method returns -1
        """
        # Initialize variables
        low_idx = 0
        high_idx = len(self.lst)-1

        # Get a middle position
        mid_idx = len(self.lst) // 2
        mid_value = self.lst[mid_idx]

        # Traverse the list
        while low_idx <= high_idx:
            mid_idx = (low_idx + high_idx) // 2
            mid_value = self.lst[mid_idx]

            if mid_value == target:
                return mid_idx
            if mid_value > target:
                high_idx = mid_idx - 1
            else:
                low_idx = mid_idx + 1

        return -1


def main():
    lst = [1, 3, 1, 0, 34, 3, 6, 10, 22]
    binary_search = BinarySearch(lst)
    print(binary_search.search(1))
    print(binary_search.search(21))


if __name__ == '__main__':
    main()
