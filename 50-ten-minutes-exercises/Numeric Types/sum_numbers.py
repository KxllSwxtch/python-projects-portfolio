#!/usr/bin/env python

def sum_numbers(*args):
    """
    Returns the sum of args
    """
    if len(args) > 0:
        is_list = isinstance(args[0], list)

        if is_list:
            output = 0
            for n in args[0]:
                if str(n).isdigit():
                    output += n
            return output
        else:
            output = 0
            for n in args:
                if str(n).isdigit():
                    output += int(n)
            return output
    else:
        return 0


def main():
    print(sum_numbers(5, 40, 10))  # 55
    print(sum_numbers('2', 2, 'string'))  # 4
    print(sum_numbers([5, 40, 10]))  # 55
    print(sum_numbers([5]))  # 5
    print(sum_numbers([]))  # 0
    print(sum_numbers())  # 0


if __name__ == '__main__':
    main()
