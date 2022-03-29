"""The very first Python script - main.py.
"""


# Hello world: the print() built-in function and the + operator.
# print("Imagine" + " is a beautiful song" + "\n" +
#       "written and composed by John Lenon.")
# print() #prazan red

# The input() built-in function

# print('Enter the year when \'Imagine\' was first released:', end = ' ')
# year = input()
# print(year)

# year = int(input('Enter the year when \'Imagine\' was first released: '))
# print(year)
# print(type(year))

# A simple function and function call

# def release_year():
#     """A simple Python function.
#     """
#     song = 'Imagine'
#     year = 1971
#     print(f'The song {song} was first released in {year}.')
#     return

# release_year()

# A simple loop and the range() built-in function

# for i in range(0, 10, 1):
#     print(i)

# A simple list, accessing list elements, printing lists

# theBeatles = ['John', 'Paul', 'George', 'Ringo']
# print(theBeatles)
# print(theBeatles[0])

# Looping through list elements - for and enumerate()
# theBeatles = ['John', 'Paul', 'George', 'Ringo']
# # for beatle in theBeatles:
# #     print(beatle)
# for i, beatle in enumerate(theBeatles):
#     print(str(i+1) + ': ' + beatle)

# Global variables: __name__, __file__, __doc__,...

# print(globals())
# print(__name__)
# #print(release_year)
# print(release_year.__doc__)

from python.inception import *

release_year()


# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
