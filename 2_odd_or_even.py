# Odd Or Even
# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user. Hint: how does an even / odd number
# react differently when divided by 2?
# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

number = float(input('Entry a number: '))

if number % 2 == 0:
    print('Even')
else:
    print('Odd')
