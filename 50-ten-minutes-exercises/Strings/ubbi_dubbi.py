# !/usr/bin/env python

def ubbi_dubbi(word: str) -> str:
    if not isinstance(word, str):
        return 'Wrong input parameter'

    vowels = ['a', 'e', 'o', 'u', 'i']
    filtered = ''.join(list(filter(lambda x: x.isalpha(), word)))
    output = ''

    for char in filtered:
        if char in vowels:
            new_char = 'ub' + char
            output += new_char
        else:
            output += char

    return output


def main():
    print(ubbi_dubbi('elephant'))
    print(ubbi_dubbi('octopus'))
    print(ubbi_dubbi('200ubbi'))
    print(ubbi_dubbi(''))
    print(ubbi_dubbi([]))


if __name__ == '__main__':
    main()
