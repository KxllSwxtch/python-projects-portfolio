#!/usr/bin/env python

def most_repeating_word(lst: list) -> str:
    for word in lst:
        print(word)


def main():
    words = ['this', 'is', 'an', 'elementary', 'test', 'example']
    most_repeating_word(words)  # elementary


if __name__ == '__main__':
    main()
