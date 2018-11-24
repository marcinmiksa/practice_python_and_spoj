# In the previous exercise we created a dictionary of famous scientists’ birthdays.
# In this exercise, modify your program from Part 1 to load the birthday dictionary
# from a JSON file on disk, rather than having the dictionary defined in the program.

import json

with open("info.json", "w") as file:
    birthday_file = json.load(file)

name = input('Welcome to the birthday dictionary. We know the birthdays of:'
             '\nAlbert Einstein\nBenjamin Franklin\nAda Lovelace')
if birthday_file:
    print()
