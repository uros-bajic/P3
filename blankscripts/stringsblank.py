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


def demonstrate_fancy_formatting():
    """Using "fancy" formatting.
    - format strings like '{0}{1} {2}', '{0}{1} {2}, {3}', etc.
    """


def demonstrate_fancy_formatting_with_f_strings():
    """Using f-strings in formatting.
    - format strings like f'Some text {some var}, more text {another var}...', etc.
    """


def demonstrate_string_operations():
    """Using different string operations.
    - endswith(), split(), center(), in (aka contains()), == (aka equals()), len(), ..., strip() (lstrip(), rstrip())
    """


if __name__ == '__main__':

    demonstrate_formatting()
    demonstrate_fancy_formatting()
    demonstrate_fancy_formatting_with_f_strings()
    demonstrate_string_operations()
