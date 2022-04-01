"""Demonstrates working with lists.
"""

# u Pythonu vektori kao takvi mnogo nisu zastupljeni
# u principu sve se radi sa listama
# mogu imati razlicite tipove, ne kao u Javi da mora isti tip

def demonstrate_lists():
    """Using just the simplest operations with lists.
    - create a non-empty list with different kinds of elements
    - accessing/slicing a list
    - comparing 2 lists (== vs. is)
    - concatenating 2 lists (the + operator)
    - looping through a list
    """

    imagine = ['Imagine', True, 1971]
    print(imagine)
    # print(str(imagine))
    print(imagine[0:2])
    print(imagine[1:])
    print(imagine == ['Imagine', True, 1971, True]) # liste poredi po sadrzaju
    print(imagine is ['Imagine', True, 1971])  # liste poredi po adresi, bez obz na sadrzaj
    print(imagine + ['John Lennon', True])
    for item in (imagine + ['John Lennon', True]):
        print(item)


def demonstrate_list_methods():
    """Using
    append()
    insert()
    remove()
    pop()
    extend()
    count()
    index()
    reverse()
    len()
    ...
    Also, "in" and "not in" operators can be used to search lists
    for the occurrence of a given element.
    """
    imagine = ['Imagine', True, 1971]
    print(imagine.append('John Lennon')) # izvrsilo se ali ne vraca nista jer je operacija void
    print(imagine)
    imagine.insert(2, 'Klaus Voormann') # dodavanje el. na poziviju
    # indeksiranje krece od 0, dakle dodat je na 3. poziciju
    print(imagine)
    imagine.remove('Klaus Voormann')
    print(imagine)
    imagine.pop()
    print(imagine)
    imagine.pop(1)
    print(imagine)
    imagine.extend(['Imagine'])
    print(imagine)
    print(imagine.count('Imagine')) # br pojavljivanja u listi
    print(imagine.index('Imagine')) # index prvog pojavljivanja
    print([i for i in range(len(imagine)) if imagine[i] == 'Imagine'])
    imagine.append('John')
    print(imagine)
    imagine.reverse()
    print(imagine)
    imagine.reverse()
    print('Imagine' in imagine)
    print('Imagine' not in imagine)


def demonstrate_arrays():
    """Using array.array() to build list-based numeric arrays.
    Demonstrating that lists and arrays are different types.
    """

    # pravi vektori se nalaze u paketu array
    from array import array
    a = array('i', [1, 2, 3, 4])
    print(type(a))
    print(a)
    l = list(a)
    print(l)
    print(type(l))

def populate_empty_list():
    """Creating an empty list and populating it with random values
    using random.seed() and random.randint()
    """

    from random import randint, seed
    seed(23)
    l = []
    for i in range(100):
        l.append(randint(0, 1000))
    print(l[34:56])


def duplicate_list():
    """Duplicating lists (carefully :)).
    Don't use l2 = l1, but either of the following:
    - l2 = l1.copy()
    - l2 = l1 + []
    - l2 = l1[:]
    """

    imagine = ['Imagine', True, 1971]
    l = imagine # jednako kopira pointere
    # l i imagine referenciraju na istu listu
    print(id(imagine), id(l))
    print(id(imagine) == id(l))
    l = imagine.copy() # kopira se lista, razl. ref
    print(id(imagine), id(l))
    print(id(imagine) ==  id(l))
    l = imagine + [] # razlicite reference
    print(id(imagine), id(l))
    print(id(imagine) ==  id(l))
    l = imagine[:] # razlicite reference
    print(id(imagine), id(l))
    print(id(imagine) == id(l))


def demonstrate_list_comprehension():
    """Showing examples of list comprehension.
    - list comprehension over an array.array()
    - list comprehension over a list of strings
    - list comprehension with enumerate(), to find indices of all occurrences of an element in a list
    Using str() and join() in printing results.
    """

    from array import array
    a = array('i', [1, 2, 3, 4])
    print([i for i in a])
    print([i for i in a if i % 2])

    songs = ['Imagine a Man', 'There\'s a Place', 'No Expectations', 'Heaven Knows']
    print([song for song in songs if song.startswith('Imagine')])

    fw = [song.split()[0] for song in songs]
    print(fw) # printa kao listu
    fw = fw[0] + ' ' + ' '.join([fwl.lower() for fwl in fw[1:]])
    print(fw)


if __name__ == '__main__':

    # demonstrate_lists()
    # demonstrate_list_methods()
    # demonstrate_arrays()
    # populate_empty_list()
    # duplicate_list()
    demonstrate_list_comprehension()