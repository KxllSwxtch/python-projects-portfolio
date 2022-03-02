#!/usr/bin/env python

def passwd_to_dict(file: str) -> dict:
    """
    Reads from a UNIX-style file and returns dicionary with
    """
    output = {}

    with open(file, 'r') as f:
        lines = f.readlines()

        for line in lines:
            if not line.startswith("#"):
                splitted_line = line.split(':')
                username = splitted_line[0]
                user_id = splitted_line[2]
                output[username] = user_id

        f.close()

    return output


def main():
    file_path = 'sources/passwd.txt'
    print(passwd_to_dict(file_path))


if __name__ == '__main__':
    main()
