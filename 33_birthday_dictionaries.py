# For this exercise, we will keep track of when our friend’s birthdays are,
# and be able to find that information based on their name. Create a dictionary
# (in your file) of names and birthdays. When you run your program it should
# ask the user to enter a name, and return the birthday of that person back to them.
# The interaction should look something like this:
# >>> Welcome to the birthday dictionary. We know the birthdays of:
# Albert Einstein
# Benjamin Franklin
# Ada Lovelace
# >>> Who's birthday do you want to look up?
# Benjamin Franklin
# >>> Benjamin Franklin's birthday is 01/17/1706.


def name_choice():
    return input('Whos birthday do you want to look up?\n')


if __name__ == '__main__':

    print('Welcome to the birthday dictionary. We know the birthdays of:'
          '\nAlbert Einstein\nBenjamin Franklin\nAda Lovelace')

    names_dict = {'Albert Einstein': '01/01/1900',
                  'Benjamin Franklin': '10/10/1800',
                  'Ada Lovelace': '20/12/1950'}

    name = name_choice()

    if name in names_dict.keys():
        print("{}'s birthday is {}".format(name, names_dict[name]))
