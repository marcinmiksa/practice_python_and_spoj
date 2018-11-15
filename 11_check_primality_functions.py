# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions,
# described below.


def get_integer():
    return int(input("Give a number: "))


number = get_integer()

if number > 1:
    for entry in range(2, number):
        if (number % entry) == 0:
            print("{} is not a prime".format(number))
        else:
            print("{} is a prime".format(number))
# number smaller than 1 is not prime
else:
    print("{} is not a prime".format(number))
