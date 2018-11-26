# Create a program that will play the “cows and bulls” game with the user.
# The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they have a “cow”.
# For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over. Keep track of the number
# of guesses the user makes throughout teh game and tell the user at the end.

import random


def random_digit():
    random_number = random.randrange(1000, 9999)
    return random_number


def choice_number():
    error = "Wrong digit"
    try:
        your_number = int(input("Enter 4 digit number: "))
        if your_number < 1000 or your_number > 9999:
            print(error)
        else:
            return your_number
    except ValueError:
        return print(error)


def the_game():
    x_random_digit = random_digit()
    y_choice_number = choice_number()

    print("Computer:", x_random_digit)
    cows = 0

    for x_entry in str(x_random_digit):
        for y_entry in str(y_choice_number):
            if x_entry == y_entry:
                cows += 1

    bulls = 4 - cows

    print("{} cows, {} bulls".format(cows, bulls))


if __name__ == '__main__':
    the_game()
