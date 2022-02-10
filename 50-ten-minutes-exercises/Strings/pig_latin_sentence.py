# !/usr/bin/env python
from pig_latin import pig_latin


def pig_latin_sentence(sentence: str) -> str:
    if not isinstance(sentence, str):
        return 'Wrong input parameter'

    output = []
    for word in sentence.split(' '):
        output.append(pig_latin(word))

    return ' '.join(output)


def main():
    print(pig_latin_sentence('this is test translation'))
    print(pig_latin_sentence('programming is great'))
    print(pig_latin_sentence('my best choice is you'))
    print(pig_latin_sentence(''))
    print(pig_latin_sentence([]))


if __name__ == '__main__':
    main()
