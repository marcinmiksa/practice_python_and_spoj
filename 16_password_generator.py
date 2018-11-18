# Write a password generator in Python. Be creative with how you generate passwords -
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a
# new password. Include your run-time code in a main method.

import random

random_list_ascii = []

for i in range(20):
    random_list_ascii.append(chr(random.randrange(33, 126)))

password = "".join(random_list_ascii)

print("New password: {}".format(password))

