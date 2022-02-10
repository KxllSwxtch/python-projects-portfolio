#!/usr/bin/env python
import random
from time import sleep
from utils import print_message


def check_guess(guess: int, generated: int):
    difference = (guess - generated) * - 1 if (guess -
                                               generated) < 0 else (guess - generated)

    if difference == 1:
        print('Just right')
        return False

    if guess > generated:
        print('Too high')
        return False
    elif guess < generated:
        print('Too low')
        return False
    else:
        print('CORRECT!')
        return True


def main():
    print_message('Welcome to a number guessing game!')
    sleep(2)

    game_running = True
    generated_number = random.randint(0, 30)

    print_message(
        "There is a random number between 0 and 30 <included>, try guessing it 😉")

    while game_running:
        user_guess = int(str(input('Enter your guess: ')).strip())
        correct_guess = check_guess(user_guess, generated_number)

        if correct_guess:
            print_message('Good Job!!!')
            retry_choice = input('Would you like to try again <y/n>?')

            if retry_choice == 'y':
                generated_number = random.randint(0, 30)
                print_message(
                    "There is a random number between 0 and 30 <included>, try guessing it 😉")
                continue
            else:
                print_message('Thank you for playing!')
                break
        else:
            print('Please try again\n')
            continue


if __name__ == '__main__':
    main()
