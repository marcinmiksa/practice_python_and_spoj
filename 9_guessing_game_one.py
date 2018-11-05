# Guessing Game One
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user
# input lessons from the very first exercise)
#
# Extras:
#
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
counter = 0

while True:
    counter = counter + 1
    try:
        number = int(input('Enter a number [press 0 to exit game]: '))
        random_number = random.randint(1, 9)

        if number == random_number:
            print('Correct number!')
            break
        elif number > random_number:
            print('Your number is too high!')
        elif number == 0:
            break
        else:
            print('Your number is too low')

    except ValueError:
        print('Wrong number!')

if number != 0:
    print('\nYou needed {} steps to guess a number!'.format(counter))
else:
    print('Exit game')
