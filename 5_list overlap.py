# List Overlap
# Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common
# between the lists (without duplicates). Make sure your program works on two lists of
# different sizes.

a_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# 1st method
c_list = set(a_list) & set(b_list)
print(c_list)

# 2nd method
print(set(a_list).intersection(set(b_list)))

# 3nd method <-- doesn't work properly!


def find_unicals(list_of_datas = [1, 2, 3, 1, 1]):
    unical = []
    for i in list_of_datas:
        counter = 0
        for j in unical:
            if i == j:
                counter += 1
        if counter == 0:
            unical.append(i)

    return unical


unic_a_list = find_unicals(a_list)
unic_b_list = find_unicals(b_list)

c_list = []
for i in unic_a_list:
    for j in unic_b_list:
        if i == j:
            c_list.append(i)

print(c_list)
