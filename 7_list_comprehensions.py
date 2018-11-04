# List Comprehensions
# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even
# elements of this list in it.

_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

new_list = []

# 1st method
for i in _list:
    if i % 2 == 0:
        new_list.append(i)
print(new_list)

# 2nd method
new_list = [i for i in _list if i % 2 ==0]
print(new_list)

# 3rd method
new_list = list(filter(lambda j: j % 2 == 0, _list))
print(new_list)
