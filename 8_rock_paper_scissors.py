# Rock Paper Scissors
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players
# want to start a new game)
# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import random

# 1st method
while True:
    try:
        player0 = int(input('Please select [0 - rock, 1, scissors, '
                            '2 - paper, -1 - exit and enter a number: '))
        player1 = int(random.randint(0, 2))
        print('Mark chose: {}'.format(player1))

        if player0 == 0 and player1 == 0:
            print('Again')
        elif player0 == 0 and player1 == 1:
            print('You win!')
        elif player0 == 0 and player1 == 2:
            print('You lose')
        elif player0 == 1 and player1 == 1:
            print('Again')
        elif player0 == 1 and player1 == 0:
            print('You lose')
        elif player0 == 1 and player1 == 2:
            print('You win!')
        elif player0 == 2 and player1 == 2:
            print('Again')
        elif player0 == 2 and player1 == 0:
            print('You win!')
        elif player0 == 2 and player1 == 1:
            print('You lose')
        elif player0 == -1 or player1 == -1:
            break
        else:
            print('Wrong number')
    except ValueError:
        print('Wrong value')
