#!/usr/bin/env python

def how_many_different_numbers(ints: list[int]) -> int:
    """Returns a number of different numbers in a list of integers (without repeating them)."""
    return len(list(set(ints)))
    

def main():
    numbers = [1, 2, 3, 1, 2, 3, 4, 1]
    print(how_many_different_numbers(numbers)) # 4

if __name__ == '__main__':
    main()