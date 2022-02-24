#!/usr/bin/env python

# Users of your program will enter the name of a city
# If the city name is blank, then the function prints a report (which I’ll describe) before exiting.
# If the city name isn’t blank, then the program should also ask the user how much rain has fallen in that city (typically measured in millimeters).
# After the user enters the quantity of rain, the program again asks them for a city name, rainfall amount, and so on—until the user presses Enter instead of typing the name of a city.


def get_rainfall():
    app_running = True
    rainfall = {}

    while app_running:
        city = str(input('Enter the name of the city: '))

        if not rainfall and len(city) == 0:
            print('N/A')
            break
        elif len(city) > 0:
            rain = int(input('Enter rain (in millimeters): '))
            rainfall[city] = rain
            continue
        
        if rainfall and len(city) == 0:
            for city, rain in rainfall.items():
                print(f'{city}: {rain}')
            break
    return  
            
        




def main():
    get_rainfall()


if __name__ == '__main__':
    main()
