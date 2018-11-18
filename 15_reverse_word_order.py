# Write a program (using functions!) that asks the user for a long string containing multiple
# # words. Print back to the user the same string, except with the words in backwards order.
# # For example, say I type the string:
# # My name is Michele
# # Then I would see the string:
# # Michele is name My
# # shown back to me.


def reverse_function(text="My name is Michele"):
    text_split = text.split(" ")
    for i in text_split[::-1]:
        print("{} ".format(i), end="")


if __name__ == '__main__':
    reverse_function("ala ma kot")
