# Let’s continue building Hangman. In the game of Hangman, a clue word is given by the
# program that the player has to guess, letter by letter. The player guesses one
# letter at a time until the entire word has been guessed. (In the actual
# game, the player can only guess 6 letters incorrectly before losing).
# Let’s say the word the player has to guess is “EVAPORATE”.
# For this exercise, write the logic that asks a player to guess a
# letter and displays letters in the clue word that were guessed correctly.
# For now, let the player guess an infinite number of times until they
# get the entire word. As a bonus, keep track of the letters the player
# guessed and display a different message if the player tries to guess
# that letter again. Remember to stop the game when all the letters
# have been guessed correctly! Don’t worry about choosing a word randomly or
# keeping track of the number of guesses the player has remaining -
# we will deal with those in a future exercise.
# An example interaction can look like this:
#
# >>> Welcome to Hangman!
# _ _ _ _ _ _ _ _ _
# >>> Guess your letter: S
# Incorrect!
# >>> Guess your letter: E
# E _ _ _ _ _ _ _ E
# ...

import random


def find_word():
    with open('sowpods.txt', 'r') as file:
        lines = file.read().splitlines()
    random_word = random.choice(lines)
    return random_word


def entry_letter():
    return input('Guess your letter: ')


if __name__ == '__main__':

    print('Welcome to Hangman!')
    word = find_word()
    guess_word = []
    letter = entry_letter()
    while True:
        if letter.upper() in word:
            print(letter)
        else:
            print('incorrect')
