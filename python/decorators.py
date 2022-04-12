"""Demonstrates functions as parameters of other functions,
functions as return values of other functions and
user-defined decorators
"""


import functools


def pass_simple_function_as_parameter():
    """Demonstrates using another function as a parameter. It works because functions are objects.
    If a call to f includes positional arguments, then they are part of the *args argument of this function.
    The same holds for optional *args in the call to f.
    """

    # Try something like this in Python Console:
    #     p = *[1,2,3]        # generates an error;
    #                           asterisk * isn't simply unary operator,
    #                           it's argument-unpacking operator for functions definitions and functions calls;
    #                           heuristics: use it "inside of something else", like inside of (), [] and constructors
    #     p = *[1,2,3],       # generates a tuple, because of the comma (* is actually "inside of creating a tuple")
    #     p = 44, *[1,2,3]    # generates another tuple
    #     print(p)
    #     print(*p)

    # Case 1: 0 or more arguments

    def f(*args):
        # print(args) #  (1, 2, 3)
        # print(*args) #  1 2 3
        return sum(args)

    def g(f, *args):
        return f(*args)

    # print(g(f, *[1,2,3])) # 6
    # print(g(f, *(1, 2, 3))) # 6
    # print(g(f)) # o, nema zadatih brojeva

    # Try also this in Python Console:
    #     def f(*args):
    #         return sum(args)      # it must be sum(args), not sum(*args); e.g. in Python Console sum((1, 2)) is OK
    #     def g(f, *args):
    #         return f(*args)       # heuristics: if *args is in a f. signature, use *args in the f. body as well
    #     g(f, *(1, 2, 3))          # result: 6
    #     g(f, *[1, 2, 3])          # result: 6

    # Case 2: 1 or more arguments (the first one is positional)

    def song(title, *args):
        print(title)
        print(', '.join([str(arg) for arg in args]))

    def print_song(song, *args):
        song(*args)

    print_song(song, *['Imagine', 1971, 'John Lennon']) # prvi uzima za title, druga dva stampa
    print()
    print_song(song, *['Imagine']) # prvi uzima kao obavezni parametar song
    # za obavezan parametar song funkcija je potrosila parametar iz *args
    print()
    # print_song(song) # nece provi jer nedostaje jedan obavezan pozicioni arg title
    # args mora da ima bar onoliko argumenata koliko ima pozicionih parametara

def pass_function_as_parameter(f, *args, **kwargs):
    """Demonstrates using another function as a parameter. It works because functions are objects.
    The argument/parameter list specified as in this function is a fairly general one -
    it works regardless of the number of *args and **kwargs in the function call (both can be 0).
    If a call to f includes positional arguments, then they are part of the *args argument of this function.
    The same holds for optional *args in the call to f. Likewise, if f is called with keyword arguments,
    they are included in the **kwargs argument of this function.
    In other words, from https://stackoverflow.com/a/3394898/1899061:
    You can use *args and **kwargs along with named arguments too. The explicit arguments get values first
    and then everything else is passed to *args and **kwargs. The named arguments come first in the list. For example:
        def table_things(titlestring, **kwargs)
    If f has default arguments, they can be included in **kwargs in the beginning of f
    (e.g., if f has a default arg d=4, then the first line of f would be kwargs['d'] = d),
    and then f is called as f(*args, **kwargs), just as if d=4 was always part of **kwargs:
    -------
    def f(*args, year=1962, **kwargs):
        kwargs['year'] = year

        print(args)             # result: a tuple of args
        print(*args)            # result: a sequence of args, 'untupled'
        print(kwargs)

    def g(h, *args, **kwargs):
        return h(*args, **kwargs)

    g(f, 'John', 'Lennon', 8, birth=1940)
    -------
    See https://stackoverflow.com/a/34206138/1899061 for further details.
    """
    # args obuhvata i pozicione i fleksibilnw argumente
    # kwargs obuhvata podrazumevane i one koje po potrebi zadajemo

    f(*args, **kwargs)

def return_function(full_name, first_name_flag):
    """Demonstrates using a function as the return value from another function.
    In this example, depending on the first_name_flag, return_function() returns one of the following functions:
    - a function that returns a person's first name
    - a function that returns a person's family name
    """

    f, l = full_name.split()

    def first():
        return f

    def last():
        return l

    return first if first_name_flag else last


def return_function_with_args(*args):
    """Demonstrates using a function as the return value from another function.
    The returned function has parameters/arguments.
    In this example, depending on len(args), return_function_with_args() returns one of the following functions:
    - a function that returns an empty list
    - a function that returns a tuple of args (or a list of args, or...)
    """

    def empty(*parameters):
        return []

    def non_empty(*parameters):
        return parameters

    return empty if not args else non_empty

def a_very_simple_decorator(f):
    """Illustrates the essential idea of decorators:
        - take a function (f) as a parameter of a decorator function (decorator)
        - use the parameter function f inside an inner wrapper function (g)
        - return the inner wrapper function g from the decorator function
    Then define f and run f = decorator(f) before calling f.
    Even better, just put @decorator before the definition of f. Each call to f will then actually run decorator(f).
    """

    # Examples (run them in Python Console):

    # def decorator(f):
    #     def g():
    #         return f('John Lennon')
    #     return g
    #
    # def something(x):
    #     return x
    # ...
    # >>> something(4)
    # 4
    # ...
    # >>> something = decorator(something)
    # >>> something
    # <function __main__.decorator.<locals>.g()>
    # >>> something()
    # John Lennon

    # def decorator(f, *args):
    #     def g():
    #         print('John Lennon')
    #         return f(*args)
    #     return g
    #
    # def something(x):
    #     return x
    # ...
    # >>> something(4)
    # 4
    # ...
    # >>> something = decorator(something, 'John Lennon')
    # >>> something
    # <function __main__.decorator.<locals>.g()>
    # >>> something()
    # John Lennon
    # John Lennon

    # dekorator je specijalna funkcija kojoj se kao parametar
    # prosledjuje druga funkcija i ona tu drugu funkciju poziva
    # u obavijajucoj (dekorisucoj) funkciji kada se namerava da se radi nesto
    # pre i posle izvrsavanja prosledjene funkcije

    # dekorator je jednostavna funkcija, nema velike mudrosti
    # koristi se kada zelimo da se svako izvrsavanje neke
    # f-je dekorise

    def wrap(*p):
        print('Before')
        v = f(*p)
        print('After')
        return v

    return wrap

def members(f_to_decorate):
    """Demonstrates how to develop a decorator.
    Uses the decorator-writing pattern (https://stackoverflow.com/a/3394911/1899061):
    import functools
    def decorator(f_to_decorate):
        @functools.wraps(f_to_decorate)			        # preserves func's identity after it's decorated
        def wrapper_decorator(*args, **kwargs):         # see https://stackoverflow.com/a/309000/1899061 for details
            # Do something before
            value = f_to_decorate(*args, **kwargs)
            # Do something after
            return value
        return wrapper_decorator
    """
    @functools.wraps(f_to_decorate)
    def wrap(*args, **kwargs):
        print('Band: ', end = '')
        v = f_to_decorate(*args, **kwargs)
        print(', '.join([str(arg) for arg in args[1:]]))
        print(', '.join([str(k) + ': ' + str(v) for k, v in kwargs.items()]))
        return v
    return wrap

@members
def print_band(name, *members, **years_active):
    """Prints the name and the members of a band, assuming that both name and *members are strings.
    The decorator before the function signature (@members) illustrates how to apply a decorator;
    omit it if decorating manually.
    """

    print(name)


if __name__ == '__main__':

    # pass_simple_function_as_parameter()

    from python.functions import *

    john = 'John Lennon'
    paul = 'Paul McCartney'
    george = 'George Harrison'
    ringo = 'Ringo Starr'
    the_beatles = [john, paul, george, ringo]

    # pass_function_as_parameter(use_all_categories_of_args, 'The Beatles', *the_beatles, start=1962, end=1970)
    # pass_function_as_parameter(use_all_categories_of_args, 'The Beatles', *the_beatles)

    # f = return_function(john, False) # vracanje funkcije kao rezultat druge f-je
    # print(f())

    # f = return_function_with_args('Imagine', 1971)
    # print(f(*['Imagine', 1971]))

    # @a_very_simple_decorator # znaci da ce se izvrsiti dekorisana varijanta f-je
    # def imagine(*args):
    #     print(args)

    # u prvom slucaju nedekorisano
    # ('Imagine', 1971)

    # imagine('Imagine', 1971)
    # print()

    # f = a_very_simple_decorator(imagine)
    # f('Imagine', 1971)

    # u drugom slucaju dekorisano
    # Before
    # ('Imagine', 1971)
    # After

    # imagine = a_very_simple_decorator(imagine)
    # imagine ('Imagine', 1971)
    # print(imagine.__name__) # wrap daje ime dekorisuce funkcije
    # print()
    # imagine('John Lennon')

    print_band('The Beatles', *the_beatles, start = 1962, end = 1970)
    print()
    print_band('The Beatles', *the_beatles)
    print()
    print(print_band.__name__)
    # DEKORATORSKI PATERN DRZATI POD JASTUKOM