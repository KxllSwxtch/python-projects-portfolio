#!/usr/bin/env python

def pig_latin(word: str) -> str:
    filtered = ''.join(list(filter(lambda x: x.isalpha(), word))).strip()

    if len(filtered) == 0:
        return '-'

    vowels = ['a', 'e', 'o', 'u', 'i']
    is_first_vowel = filtered[0] in vowels

    if is_first_vowel:
        return filtered + 'way'
    else:
        return filtered[1::] + filtered[0] + 'ay'


def main():
    print(pig_latin('python'))  # 'ythonpay'
    print(pig_latin('air'))  # 'airway'
    print(pig_latin('eat'))  # 'eatway'
    print(pig_latin('cat'))  # 'atcay'
    print(pig_latin('computer'))  # 'omputercay'
    print(pig_latin(''))  # '-'
    print(pig_latin('123'))  # '-'
    print(pig_latin('alpha123'))  # 'alphaway


if __name__ == '__main__':
    main()
