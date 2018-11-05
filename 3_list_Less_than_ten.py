# List Less Than Ten
# Take a list, say for example this one:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print(_list)

number = float(input('Select number: '))

# 1st method

for entry in _list:
    if entry < number:
        print(entry)

# 2nd method
print(list(filter(lambda x: x < number, _list)))
