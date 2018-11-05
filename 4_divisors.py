# Divisors
# Create a program that asks the user for a number and then prints out a list of all
# the divisors of that number. (If you don’t know what a divisor is, it is a number that
# divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has
# no remainder.)
# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html


def divisors(number=0):
    list_of_divisors = []

    for i in range(1, number + 1):
        if number % i == 0:
            list_of_divisors.append(i)
    print(list_of_divisors)


if __name__ == '__main__':
    divisors(number=30)
