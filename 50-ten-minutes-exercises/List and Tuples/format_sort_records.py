#!/usr/bin/env python

from operator import itemgetter


def format_sort_records(lst: list) -> str:
    """
    Outputs all the records from the input in a form of a string
    """
    string_formatting = '{1:10}{0:10}{2:5.2f}'
    sorted_lst = sorted(lst, key=itemgetter(1, 0))
    output = []

    for record in sorted_lst:
        output.append(string_formatting.format(*record))

    return output


def main():
    PEOPLE = [('Donald', 'Trump', 7.85),
              ('Vladimir', 'Putin', 3.626),
              ('Jinping', 'Xi', 10.603)]

    print('\n'.join(format_sort_records(PEOPLE)))
    # Trump     Donald      7.85
    # Putin     Vladimir    3.63
    # Xi        Jinping    10.60


if __name__ == '__main__':
    main()
