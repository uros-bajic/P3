"""Demonstrates details of writing Python functions: annotations, default args, kwargs.
"""

# def demonstrate_annotations(title:, year):
def demonstrate_annotations(title: str, year: int) -> str:
    """Demonstrates how to use annotations of
    function parameters/arguments (<arg>: <type>) and of function return type (def f(...) -> <type>:).
    - print the function parameters/arguments
    - print the value of the __annotations__ attribute of this function
    - print the name and the docstring of this function
    - return a formatted string (including function parameters/arguments)
    """
    # funckije su objekti kao i sve u pythonu
    # funkcije imaju neka svoja polja, npr anotacije
    # ideja anotacija - kontrola tipova ulaznih i izlaznih vrednosti

    print(demonstrate_annotations.__annotations__)
    # {'title': <class 'str'>, 'year': <class 'int'>, 'return': <class 'str'>}
    print(demonstrate_annotations.__name__)
    # demonstrate_annotations
    print(demonstrate_annotations.__doc__)
    # ispisuje docstring pod """..."""
    return f'{title}, {year}'


# def show_song(title, author='John Lennon', year: int = 1971): # u slucaju anotacija
def show_song(title, author='John Lennon', year=1971):

    """Demonstrates default arguments/parameters.
    - print locals()
    - print the function arguments/parameters in one line
    """
    # pozicioni argumenat - moraju da se nadju
    # za specificiranoj poziciji pri spoljnom pozivu f-je
    # author='John Lennon' - argument moze da se izostavi
    # prilikom poziva funkcije, pri cemu ce u tom slucaju
    # vrednost biti podrazumevana - John

    # t = True
    # print(locals()) # ispisuje promenljive vidljive unutar funkcije

    print(f'{title}, {author}, {year}')


def use_flexible_arg_list(band: str, *members):
    """Demonstrates flexible number of arguments/parameters.
    - print the band name and the list of band members in one line
    """
    # imamo proizvoljno mnogo parametara u funkciji *members
    # print(type(members)) # tuple tip
    print(f'{band}: {members}')


def use_all_categories_of_args(band, *members, is_active=True, **details):
    """Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).
    - print all arguments/parameters, including the keyword arguments/parameters, in one line
    """
    # 1. band - pozicioni
    # 2. *members - proizvoljno mnogo
    # 3. is_active = True - podrazumevani
    # 4. **details - jos neki
    # hijerarhija parametara

    # print(type(details)) # dict

    print(f'{band}, {members}, {is_active}, {details}')


if __name__ == "__main__":

    imagine = 'Imagine'
    year = 1971

    john = 'John Lennon'
    paul = 'Paul McCartney'
    george = 'George Harrison'
    ringo = 'Ringo Starr'
    the_beatles = [john, paul, george, ringo]

    # print(demonstrate_annotations(imagine, year))

    # show_song(imagine)
    # show_song(imagine, author='JL') # moze se menjati default vrednost
    # show_song(imagine, year =1970, author='JL') # promena pozicija u pozivu
    #  # samo ako se specificiraju identifikatori

    # use_flexible_arg_list('The Beatles', *the_beatles)
    # * - list unpacking
    # use_flexible_arg_list('The Beatles')
    # use_flexible_arg_list('The Beatles') # pozicioni arg. mora da se zada, tu nema zavitlavanja

    use_all_categories_of_args('The Beatles', is_active=False, start=1962, end=1970)
    # zahvaljujuci ** details na licu mesta dodajemo proizvoljno mnogo parametara ili ne
    use_all_categories_of_args('The Beatles', *the_beatles, is_active=False, start=1962, end=1970)
