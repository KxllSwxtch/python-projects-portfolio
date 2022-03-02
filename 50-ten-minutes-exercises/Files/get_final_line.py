#!/usr/bin/env python

def get_final_line(filename: str) -> str:
    """Returns the final line of the file"""
    final_line = ''

    with open(filename, 'r') as f:
        lines = f.readlines()
        final_line = lines[len(lines)-1]
        f.close()

    return final_line


def main():
    file_path = 'sources/file1.txt'
    print(get_final_line(file_path), end='')


if __name__ == '__main__':
    main()
