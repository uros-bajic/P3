"""Demonstrates dictionaries.
From: https://qr.ae/TWCAvj:
Python uses dictionaries all over the place:
- the variables and functions in a module - stored in a dictionary  # can be shown using globals()
- the local variables in a function - stored in a dictionary        # can be shown using locals(); see functions.py
- the implementation of a function - a dictionary
- a class is a dictionary
- an instance of a class is another dictionary
- the modules your program has imported - you guessed it - another dictionary
- even Python set objects are implemented as modified dictionaries
To paraphrase Tim Peter's 'Zen of Python': "dictionaries are great - let's do more of them".
Read more at https://qr.ae/TWCAvj.
"""


def demonstrate_dictionaries():
    """Creating and using dictionaries.
    - create a blank (empty) dictionary
    - create a non-empty dictionary
    - access dictionary values by the corresponding keys (syntax: value = d[key])
    - print a non-empty dictionary
        - print all items using the items() function
        - print one item per line
    - pprint dictionary in one column
    - add/remove items to/from a dictionary
    - update a dictionary with the items from another dictionary or from an iterable of (k, v) pairs using dict.update()
    - using the keys() and values() functions
    """

    imagine = {}
    print(type(imagine))
    print(imagine)
    print()

    imagine = {'title': 'Imagine', 'year': 1971}
    print(imagine)
    print()

    print(imagine['title'])
    print(imagine.items())
    imagine['author'] = 'John Lennon'
    print(imagine)
    imagine.pop('author')
    print(imagine)
    imagine.update({'author': 'John Lennon', 'bass': 'Klaus Voormann'})
    print(imagine)

    for k, v in imagine.items():
        print(k, v)

    from pprint import pprint
    pprint(imagine, width=1)
    print()

    print(imagine.keys())
    print(imagine.values())

def sort_dictionary(d, by):
    """Sorting a dictionary by keys or by values.
    - using zip()
    - using operator.itemgetter()
    - using lambda
    """

    # 3 varijante sortiranja recnika

    # if by == 'k' or by == 'K':
    #     return dict(sorted(zip(d.keys(), d.values())))
    # elif by == 'v' or by == 'V':
    #     return dict(sorted(zip(d.values(), d.keys())))
    # else:
    #     return None

    # from operator import itemgetter

    # itemgetter kao rezultat vraca funkciju
    # f = itemgetter(0) - itemgetter vraca funkciju koja vraca 0-ti (i-ti) element kolekcije

    # if by == 'k' or by == 'K': # po kljucu
    #     return dict(sorted(d.items(), key=itemgetter(0)))
    # elif by == 'v' or by == 'V': # po vrednosti
    #     return dict(sorted(d.items(), key=itemgetter(1)))
    # else:
    #     return None

    if by == 'k' or by == 'K':  # po kljucu
        return dict(sorted(d.items(), key=lambda item: item[0]))
    elif by == 'v' or by == 'V': # po vrednosti
        return dict(sorted(d.items(), key=lambda item: item[1]))
    else:
        return None


def demonstrate_dict_sorting():
    """Demonstrate sorting a dictionary.
    """
    imagine = {'title': 'Imagine', 'year': '1971', 'author': 'John Lennon'}
    print(sort_dictionary(imagine, 'k'))
    print(sort_dictionary(imagine, 'v')) # greska
    # sortiranje po vrednostima baca gresku jer se porede string i int
    # tj razliciti tipovi pa samo stavimo 1971 pod navodnike
    # TypeError: '<' not supported between instances of 'int' and 'str'
    print(sort_dictionary(imagine, 123))

    # problem je sto se sortiranje po vrednosti radi tako da
    # vrednosti postaju kljucevi

if __name__ == '__main__':
    # demonstrate_dictionaries()
    demonstrate_dict_sorting()

    # print(globals())
