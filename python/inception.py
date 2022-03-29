"""The very first module in a more structured version of the project.
"""


# Moving code from main.py

# print('Enter the year when \'Imagine\' was first released:', end=' ')
# year = input()
# print(year)
# print(__name__)


def release_year():
    """A simple Python function.
    """
    song = 'Imagine'
    year = 1971
    print(f'The song {song} was first released in {year}.')


# release_year()


# Taking care of the module __name__

if __name__ == '__main__':
    # release_year()
    # print(__name__)


    # Printing with ' ' and printing without '\n'

    # print('Enter the year when \'Imagine\' was first released:', end=' ')
    # year = input()
    # print(year)
    # print(__name__)
    #
    # Printing with classical formatting (%)

    # print('%s is a song from %d.' % ('Imagine', 1971))

    # Keyboard input


    # break and continue

    # for i in range(1, 15, 2):
    #     if i == 7:
    #         # break
    #         continue
    #     print(i)


    # Printing docstrings


    # Printing a list using enumerate()


    # Importing from Standard Library

    from datetime import date

    d = date(1971, 10, 11)
    print(d)
    d_format = '%b %d, %Y'
    print(d.strftime(d_format))