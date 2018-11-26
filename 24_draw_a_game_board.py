# This exercise is Part 1 of 4 of the Tic Tac Toe exercise series.
# The other exercises are: Part 2, Part 3, and Part 4.
# Time for some fake graphics! Let’s say we want to draw game boards that look like this:
#   ---- --- ---
# # |   |   |   |
# #  ----- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes
# (8x8 for chess, 19x19 for Go, and many more).
# Ask the user what size game board they want to draw, and draw it for them to the screen
# using Python’s print statement.


# def single_field():
#     list_of_signs = []
#     list_of_signs.append([' ', '-', '-', '-', ' '])
#     list_of_signs.append(['|', ' ', ' ', ' ', '|'])
#     list_of_signs.append([' ', '-', '-', 'v', ' '])
#     list_of_elements = [" --- ",
#                         "     ",
#                         "|   |",
#                         "     ",
#                         " --- "]
#     field = "\n".join(list_of_elements)
#     return field, list_of_signs
#
# def m_matrix(x_size=3, y_size=4, element=[[]]):
#     display_matrix = []
#     ele_lines_no = len(element)
#     if ele_lines_no > 0:
#         ele_signs_no = len(element[0])
#     else:
#         ele_signs_no = 0
#
#     y_elements = []
#     x_elements_no = ele_lines_no * x_size
#     y_elements_no = ele_lines_no * y_size
#     for x in range(x_elements_no+1):
#         for y in range(y_elements_no+1):
#             y_elements.append('.')
#         display_matrix.append(y_elements)
#         y_elements = []
#
#     return display_matrix
#
# def matrix(x=3, y=3):
#     for entry_x in range(x):
#         for entry_y in range(y):
#             print(single_field(), end="")  # <-----popraw
#
#
# if __name__ == '__main__':
#     #matrix(x=3, y=3)
#     file, elems = single_field()
#     # for line in elems:
#     #     print('')
#     #     for m_sign in line:
#     #         print(m_sign, end='')
#     # print(elems[2][3])
#     display = m_matrix(2, 3, elems)
#     print(display)

def board(size):
    for i in range(size):
        print('---'.join(' ' * (size + 1)))
        print('   '.join('|' * (size + 1)))
    print('---'.join(' ' * (size + 1)))


if __name__ == '__main__':
    board(3)
