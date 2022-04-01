"""Demonstrates how operators and expressions work in Python.
"""

from settings import *


def demonstrate_arithmetic_operators():
    """Working with arithmetic operators.
    Arithmetic operators in Python are pretty much the same as in other programming languages.
    The integer division operator: //
    """

    print((45//12) % 3 - 234)


def demonstrate_relational_operators():
    """Working with relational operators.
    - simple comparisons
    - comparing dates (== vs. is)
    - comparing dates (>, <, etc. with dates)
    - None in comparisons, type(None)
    """

    print(12 > 34)
    print()

    if 12 > 34:
        print(True) # kompajlerska greska
    else:
        print(False)
    if '':
        print(True)
    else:
        print(False)
    print()
    # False
    #
    # False
    # False

    from datetime import date
    d1 = date(1971, 10, 11)
    d2 = date(1971, 10, 11)
    # d2 = date.today()
    if d1 > d2:
        print('d1 > d2')
    else:
        print('d1 not > d2')
    # 'sve' je dozvoljeno u pythonu, treba se zdravorazumski
    # i intuitivno ponasati

    print(d1 == d2) # default je poredjenje po sadrzaju
    print(id(d1) == id(d2)) # poredjenje u smislu adresa - default u Javi npr
    print(id(d1), id(d2))
    print()
    # None je specijalna zverka

    print(type(None)) # None je jedina moguca vrednost klase NoneType
    # None se ponasa vrlo mocno
    # print(d1 > None)
    print(d1 == None)
    print()



def demonstrate_logical_operators():
    """Working with logical operators.
    - logical operations with True, False and None
    - logical operations with dates
        - make sure to read this: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not !!!
          (or just this: https://stackoverflow.com/questions/44612144/logical-operators-in-python)
    - logical operations with None (incl. None and int, None and date, etc.)
    - None and date vs. None > date
    """
    # u logickim tipovima malo cudno jer radi i sa onim sto nije bool tipa
    print(True and False) # False
    print(True and True) # True
    print(True or None) # True
    print(0 or None) # None
    print()
    # pogledati linkove u prilogu

    from datetime import date
    d1 = date(1971, 10, 11)
    d2 = date(1973, 10, 11)

    print(d1 and d2) # 1973-10-11
    print(0 and d2) # 0 je uslovni False - printa 0
    print(False and d2) # False
    print(False or d2) # 1973-10-11
    print(False or not d2) # False
    print(not d2) # not ponistava uslovni True i pretvara u pravi False, printa - False
    print()

    print(None and d1) # None
    print(None or d1) # 1971-10-11
    print(None or not d1) # False
    print()

    print(d1.strftime(PREFERRED_DATE_FORMAT))

if __name__ == '__main__':

    # demonstrate_arithmetic_operators()
    # demonstrate_relational_operators()
    demonstrate_logical_operators()
