"""Demonstrates tuples.
"""


def demonstrate_tuples():
    """Creating and using tuples.
    - create and print 1-tuple, 2-tuple, mixed-type n-tuple
    - accessing elements of a tuple using []
    - demonstrate that tuples are immutable
    """

    empty_tuple = ()
    print(type(empty_tuple))
    one_tuple = ('Imagine', ) # mora zarez za jedan element ili ce biti string
    print(one_tuple)
    # pair = ('Imagine', 'John_Lennon')
    pair = 'Imagine', 'John_Lennon'
    print(pair)
    triplet = 'Imagine', 'John_Lennon', 1971 # zagrade su konnvencija, tuploidnost se postize zarezima
    print(triplet)
    print()

    print(triplet[0])
    print()

    # triplet[i] = '...' error, tuples su immutable


def demonstrate_packing():
    """Packing and unpacking tuples.
    """
    imagine = 'Imagine', 'John_Lennon', 1971
    print(imagine)
    i, j, k = imagine # raspakivanje
    print(j)
    print()


def demonstrate_zip():
    """Using the built-in zip() function with tuples and multi-counter for-loop.
    - demonstrate zip object
    - demonstrate converting a zip object to a list object
    - demonstrate that a zip object is an iterator (must be re-initialized after looping)
    """

    john = ('John Lennon', 1940, 'Liverpool')
    paul = ('Paul McCartney', 1942, 'Liverpool')
    george = ('George Harrison', 1944, 'Liverpool')
    ringo = ('Ringo Starr', 1940, 'Liverpool')

    theBeatles = zip(john, paul, george, ringo)
    print(theBeatles)
    print(list(theBeatles)) # zip objekat je lista tupleova
    # zip radi u ovom slucaju tako sto se prvi elementi ulaznih tupleova
    # smeste u prvi izlazni tuple

    print()


if __name__ == '__main__':

    # demonstrate_tuples()
    # demonstrate_packing()
    demonstrate_zip()