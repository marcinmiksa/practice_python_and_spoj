# Rock Paper Scissors
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players
# want to start a new game)
# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

player = ['Tom', 'Mark']
choice = ['rock', 'scissors', 'paper']
input('{1} please select {0} and enter a number: '.
      format(list(enumerate(choice, 0)), player[0]))
input('{1} please select {0} and enter a number: '.
      format(list(enumerate(choice, 0)), player[1]))
