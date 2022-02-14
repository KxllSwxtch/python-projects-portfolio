# !/usr/bin/env python


def strsort(string: str) -> str:
    """
    Sorts a string
    """
    return ''.join(sorted(string))


def main():
    print(strsort('bca'))  # abc


if __name__ == '__main__':
    main()
