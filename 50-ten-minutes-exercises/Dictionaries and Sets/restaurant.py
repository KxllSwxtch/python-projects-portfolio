#!/usr/bin/env python


def restaurant(menu: dict) -> int:
    """
    Calculates the total amount of order (in $)
    """
    app_running = True
    total = 0

    while app_running:
        order = input('Order: ')

        if order in menu:
            price = menu[order]
            total += price
            print(f'{order} costs ${price}. Total is ${total}')

        if order not in menu and len(order) > 0:
            print(f'Sorry, we are fresh out of {order} today.')

        if not order or len(order) == 0:
            if total > 0:
                print(f'Your total is ${total}')
            else:
                print('You have not ordered any items today.')
            return total


def main():
    MENU = {'sandwich': 10, 'tea': 7, 'salad': 9}
    restaurant(MENU)


if __name__ == '__main__':
    main()
