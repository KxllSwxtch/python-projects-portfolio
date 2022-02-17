#!/usr/bin/env python

def mysum(*args):
    if not args:
        return args
    else:
        output = args[0]
        for item in args[1::]:
            output += item
        return output


def main():
    print(mysum(12, 4))
    print(mysum('abc', 'def'))
    print(mysum([1, 2, 3], [4, 5, 6]))
    print(mysum((1, 2, 3), (4, 5, 6)))


if __name__ == '__main__':
    main()
