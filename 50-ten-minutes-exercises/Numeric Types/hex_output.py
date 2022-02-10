#!/usr/bin/env python

def hex_output() -> int:
    """
    Converts the hexadecimal to decimal
    """
    output = 0
    hex = input('Please enter the hexadecimal value: ')

    for power, num in enumerate(reversed(hex)):
        mul = int(num, 16)
        powered = mul * (16 ** power)
        output += powered

    return output


def main():
    print(hex_output())


if __name__ == '__main__':
    main()
