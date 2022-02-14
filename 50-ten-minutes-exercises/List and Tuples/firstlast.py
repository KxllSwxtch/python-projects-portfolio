#!/usr/bin/env python

def firstlast(input: str or list or tuple):
    """
    Retrieves the first and last elemnt of an input
    """
    return [input[0], input[len(input)-1]] if len(input) > 0 else input


def main():
    print(firstlast('string'))
    print(firstlast([0, 1, 2, 3, 5, 1, 1, 22]))
    print(firstlast((9, 3, 1, 444, 112, 31)))
    print(firstlast(()))


if __name__ == '__main__':
    main()
