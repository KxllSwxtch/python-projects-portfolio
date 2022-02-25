#!/usr/bin/env python

# The function returns a new dict that expresses the difference between the two dicts.
# Check if the keys are the same
    # if not, then add None to the output dict
# Check if the values are the same
    # If not then add None to the output dict

def dictdiff(d1: dict, d2: dict) -> dict:
    """
    Returns the dict output which contains difference(s) between the two dicts.
    """
    output = {}
    union = d1 | d2

    for key, value in union.items():
        if d1.get(key) != d2.get(key):
            output[key] = [d1.get(key), d2.get(key)]

    return output


def main():
    d1 = {'a': 1, 'b': 2, 'c': 3}
    d2 = {'a': 1, 'b': 2, 'c': 4}

    print(dictdiff(d1, d1)) # {}
    print(dictdiff(d1, d2)) # { 'c': [3, 4] }

    d3 = {'a': 1, 'b': 2, 'd': 3}
    d4 = {'a': 1, 'b': 2, 'c': 4}

    print(dictdiff(d3, d4)) # { 'd': [3, None], 'c': [None, 4] }

    d5 = {'a': 1, 'b': 2, 'd': 4}

    print(dictdiff(d1, d5)) # { 'c': [3, None], 'd': [None, 4] }


if __name__ == '__main__':
    main()
