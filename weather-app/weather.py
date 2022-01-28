#!/bin/python
import time
from decouple import config

weather_api_key = config('WEATHER_API_KEY')
divider = '--------------------------------------------'


def print_selection_menu():
    print(divider + '\n')
    print('Please select from the following options')
    print('1. Get a weather for a city')
    print('2. Get a weather for a city and save it in a file')
    print('3. Get a 16 day forecast')
    print('4. Get a 4 days hourly forecast')
    print('0. Exit application.')
    return


def main():
    print(divider)
    print('Welcome to a weather application')
    time.sleep(2)

    app_running = True
    while app_running:
        print_selection_menu()
        user_selection = str(input('\nPlease enter your option: '))

        match user_selection:
            case '1':
                pass

            case '0':
                print('Thank you for using application\n')
                app_running = False


if __name__ == '__main__':
    main()
