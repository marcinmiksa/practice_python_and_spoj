# String Lists
# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

word = str(input('Enter string: '))

# 1st method
if word == word[::-1]:
    print('Palindrome')
else:
    print('No Palindrome')

# 2nd method
word_rev = reversed(word)
if list(word) == list(word_rev):
    print('Palindrome')
else:
    print('No Palindrome')
