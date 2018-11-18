# Implement a function that takes as input three variables,
# and returns the largest of the three. Do this without using the Python max() function!
# The goal of this exercise is to think about some internals that Python normally
# takes care of for us. All you need is some variables and if statements!

a = input("Entry number A: ")
b = input("Entry number B: ")
c = input("Entry number C: ")

if a > b and a > c:
    print("A = {} is greater than B = {} and C = {}".format(a, b, c))
elif b > a and b > c:
    print("B = {} is greater than A = {} and C = {}".format(b, a, c))
else:
    print("C = {} is greater than A = {} and B = {}".format(c, a, b))
