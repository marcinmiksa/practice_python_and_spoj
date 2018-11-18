# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

a = [5, 10, 15, 20, 25]


def short_list():
    a_short = a[0], a[-1]
    print(list(a_short))


if __name__ == '__main__':
    short_list()
