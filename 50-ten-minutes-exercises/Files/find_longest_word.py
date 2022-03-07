#!/usr/bin/env python

def find_longest_word(filename: str) -> str:
    """
    Returns the longest word from the file
    """
    longest_word = ''

    for line in open(filename, 'r'):
        for word in line.split():
            if len(word) > len(longest_word) and word.isalpha():
                longest_word = word

    return longest_word


def main():
    file_path = 'sources/longest_source.txt'
    file_path_2 = 'sources/longest_source2.txt'

    print(find_longest_word(file_path))  # perpendicularity
    print(find_longest_word(file_path_2))  # thisisthelongeststringevercreated


if __name__ == '__main__':
    main()
