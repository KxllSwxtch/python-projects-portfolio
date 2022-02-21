#!/usr/bin/env python

from operator import itemgetter


def alphabetize_names(lst: list) -> list:
    """
    Sorts a list of dictionaries by last name, and the by first name
    """
    return sorted(lst, key=itemgetter('last', 'first'))

    # OLD SOLUTION
    # lst_length = len(lst)
    # is_input_list = isinstance(lst, list)

    # if not is_input_list:
    #     return []

    # if lst_length == 0 or lst_length == 1:
    #     return lst
    # else:
    #     output = []

    #     for i in range(lst_length - 1):
    #         item = lst[i]
    #         next_item = lst[i+1]

    #         if item['last'] > next_item['last']:
    #             output.append(next_item)
    #         if item['last'] < next_item['last']:
    #             output.append(item)

    #         if item['first'] > next_item['first']:
    #             output.append(next_item)
    #         if item['first'] < next_item['first']:
    #             output.append(item)

    #     return output


def main():
    PEOPLE = [{'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
              {'first': 'Donald', 'last': 'Trump', 'email': 'donald@trump.com'}, ]

    print(alphabetize_names(PEOPLE))


if __name__ == '__main__':
    main()
