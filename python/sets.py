"""Demonstrates sets.
"""


def demonstrate_sets():
    """Creating and using sets.
    - create a set with an attempt to duplicate items
    - demonstrate some of the typical set operators:
        & (intersection)
        | (union)
        - (difference)
        ^ (disjoint)
    """

    # imagine = {} recnik
    imagine = set()
    print(type(imagine))
    imagine.add('Imagine')
    print(imagine)
    imagine = {'Imagine', 1971, 'John Lennon'}
    print(imagine)
    imagine.update({'Klaus Voormann', 'Alan White'})
    print(imagine)
    imagine.add('Imagine') # elementi u skupu se ne ponavljaju
    print(imagine)
    print()

    l = ['Imagine', 1971, 'John Lennon', 'Imagine']
    print(l)
    print(set(l)) # iz liste u set i obrnuto, eliminisu se duplikati
    print(list(set(l)))
    print()

    imagine = {'Imagine', 1971, 'John Lennon'}
    print(imagine | {'Klaus Voormann', 'Alan White'}) # unija
    # redosled u skupu nije obavezno odredjen
    # redosledom ubacivanja elemenata
    # kod skupova redosled i nije vazan
    imagine = imagine | {'Klaus Voormann', 'Alan White'}
    print(imagine)
    print(imagine & {'Klaus Voormann'})
    print(imagine - {'Klaus Voormann'})
    print(imagine ^ {'Klaus Voormann'}) # simetricna razlika elementi samo u jednom od skupova



if __name__ == '__main__':

    demonstrate_sets()