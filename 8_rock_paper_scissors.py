# Rock Paper Scissors
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players
# want to start a new game)
# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

# 1st method
# while True:
#     try:
#         player0 = int(input('Tom please select [0 - rock, 1, scissors, '
#                             '2 - paper, -1 - exit and enter a number: '))
#         player1 = int(input('Mark please select [0 - rock, 1, scissors, '
#                             '2 - paper, -1 - exit and enter a number: '))
#
#         if player0 == 0 and player1 == 0:
#             print('Again')
#         elif player0 == 0 and player1 == 1:
#             print('Win')
#         elif player0 == 0 and player1 == 2:
#             print('Lose')
#         elif player0 == 1 and player1 == 1:
#             print('Again')
#         elif player0 == 1 and player1 == 0:
#             print('Lose')
#         elif player0 == 1 and player1 == 2:
#             print('Win')
#         elif player0 == 2 and player1 == 2:
#             print('Again')
#         elif player0 == 2 and player1 == 0:
#             print('Win')
#         elif player0 == 2 and player1 == 1:
#             print('Lose')
#         elif player0 == -1 or player1 == -1:
#             break
#         else:
#             print('Wrong number')
#     except ValueError:
#         print('Wrong value')

# 2nd method
choice = {'rock': 0, 'scissors': 1, 'paper': 2}


Tom = int(input('Tom please select {0} and enter a number: '
                .format(list(enumerate(choice, 0)))))
Mark = int(input('Mark please select {0} and enter a number: '
                 .format(list(enumerate(choice, 0)))))

if Tom == choice['rock']:
    print("Again")








