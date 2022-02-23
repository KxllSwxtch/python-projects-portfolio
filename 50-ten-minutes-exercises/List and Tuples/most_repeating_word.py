#!/usr/bin/env python

from collections import Counter


def most_repeating_word(lst: list) -> str:
    """
    Outputs a string with most repeated number of characters
    """
    return max(lst, key=lambda word: Counter(word).most_common(1)[0][1])

    ### OLD SOLUTION ###
    # sorted_lst = sorted(lst, key=len, reverse=True)
    # output = []

    # for i in range(len(sorted_lst)):
    #     word = sorted_lst[i]
    #     d = {}

    #     for char in word:
    #         d[char] = word.count(char)

    #     output.append(d)

    # output = [sum([value if value > 1 else 0 for value in d.values()])
    #           for d in output]
    # idx_max = output.index(max(output))

    # return sorted_lst[idx_max]


def main():
    words = ['this', 'is', 'an', 'elementary',
             'test', 'example', 'anagram']
    print(most_repeating_word(words))  # elementary


if __name__ == '__main__':
    main()
