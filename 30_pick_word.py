# This exercise is Part 1 of 3 of the Hangman exercise series. The other exercises are:
# Part 2 and Part 3.
# In this exercise, the task is to write a function that picks a random word from a list
# of words from the SOWPODS dictionary. Download this file and save it in the same
# directory as your Python code. This file is Peter Norvig’s compilation of the
# dictionary of words used in professional Scrabble tournaments. Each line in the
# file contains a single word.
# Hint: use the Python random library for picking a random word.

import random


def find_line():
    with open('sowpods.txt', 'r') as file:
        lines = file.read().splitlines()
    random_line = random.choice(lines)
    return random_line


def find_line2():
    with open('sowpods2.txt', 'r') as file2:
        lines2 = file2.readlines()
    random_line2 = random.randint(0, len(lines2)-1)
    return lines2[random_line2]


if __name__ == '__main__':
    print(find_line())
    print(find_line2())
