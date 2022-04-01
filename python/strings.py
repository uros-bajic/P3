"""Demonstrates working with strings in Python.
"""

import string

import settings


def demonstrate_formatting():
    """Demonstrating details of string formatting.
    - using classical formatting
    - \n is the new line char
    - r'...' - raw formatting
    - using \"\"\"...\"\"\" for multi-line formatting
    - string "multiplication"
    - substrings / slicing
    - str() vs. repr() (usually the same, but with whitespace there is a difference)
    """

    print('%s is a nice song from %d written by %s, sold worldwide in %1.2f.' % ('Imagine', 1971, 'John Lennon', 20.2))
    print('C:\nobody')
    print(r'C:\nobody') # r oznacava raw, prikazi bas taj string
    print("""John
Lennon
...""") # vodi racuna i printa tabove, doslovno
    print('       Imagine' * 3)
    print('Imagine')
    print('Imagine'[0:4])
    print('Imagine'[:-2])
    print(str(12))
    print(str('Imagine   \n'))
    print(repr('Imagine   \n')) # representation printa doslovno
    print(repr('Imagine')) # za obicne prave stringove samo dodaje navodnike


def demonstrate_fancy_formatting():
    """Using "fancy" formatting.
    - format strings like '{0}{1} {2}', '{0}{1} {2}, {3}', etc.
    """

    print('{} is a nice song from {} written by {}, sold worldwide in {}.'.format('Imagine', 1971, 'John Lennon', 20.2))


def demonstrate_fancy_formatting_with_f_strings():
    """Using f-strings in formatting.
    - format strings like f'Some text {some var}, more text {another var}...', etc.
    """

    imagine = 'Imagine'
    year = 1971
    print(f'{imagine} is a nice song from {year} written by {"John Lennon"}, sold worldwide in {20.2}.'.format('Imagine', 1971, 'John Lennon', 20.2))


def demonstrate_string_operations():
    """Using different string operations.
    - endswith(), split(), center(), in (aka contains()), == (aka equals()), len(), ..., strip() (lstrip(), rstrip())
    """

    print('Imagine'.endswith('ne'))
    print('Imagine is a song from 1971.'.split())
    print('Imagine is a song from 1971.'.split('Imagine'))
    print('Imagine'.center(30, '*'))
    print('Img' not in 'Imagine')
    imagine = 'Imagine'
    print(imagine == 'Imagine')
    print(len('Imagine'))
    print('    Imagine   ')
    print('    Imagine   '.strip())
    print('    Imagine   '.lstrip())
    print('    Imagine   '.rstrip())


if __name__ == '__main__':

    # demonstrate_formatting()
    # demonstrate_fancy_formatting()
    # demonstrate_fancy_formatting_with_f_strings()
    demonstrate_string_operations()