#!/usr/bin/env python
from distutils.log import ERROR
from email.policy import default
import time
import asyncio
import aiohttp
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


async def get_weather_for_city(city: str, weather_api_url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(weather_api_url) as response:
            try:
                weather_data = await response.json()
                time.sleep(2)
                current_state = weather_data["weather"][0]["main"]
                city = city[0].upper() + city[1:]
                output_string = f'\nIts {current_state} in {city}'
                print(output_string)
            except Exception as e:
                print(e)


async def main():
    print(divider)
    print('Welcome to a weather application')
    time.sleep(2)
    app_running = True

    while app_running:
        print_selection_menu()
        user_selection = str(input('\nPlease enter your option: '))

        match user_selection:
            case '4':
                pass

            case '3':
                pass

            case '2':
                pass

            case '1':
                # Ask user to input the city name
                city = str(input('Please enter the city: '))
                weather_api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}'
                await get_weather_for_city(city, weather_api_url)

            case '0':
                print('Thank you for using application\n')
                app_running = False

            case _:
                print('\nIncorrect value')
                print('Please enter one option from the menu')


if __name__ == '__main__':
    asyncio.run(main())
