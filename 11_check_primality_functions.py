# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity
# to practice using functions,described below.


def is_prime():

    def get_integer():
        input_value = input("Give a number: ")
        try:
            return int(input_value)
        except ValueError:
            return 1

    number = get_integer()

    if number <= 1:
        print("{} is not a prime".format(number))
    elif number == 2:
        print("{} is a prime".format(number))
    else:
        counter = 0
        for entry in range(3, number+1):
            if (number % entry) == 0:
                counter += 1

        if counter == 1:
            print("{} is a prime".format(number))
        else:
            print("{} is not a prime".format(number))


if __name__ == '__main__':
    while True:
        is_prime()
