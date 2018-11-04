# Character Input
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that
# they will turn 100 years old.
# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

name = input('Name: ')
age = int(input('Age: '))

result = 2018 + 100 - age
print('{} in {} you will have 100 years'.format(name, result))
