"""The class representing the concept of playlist.
It includes a list of Song objects and the dates when the playlist was created and completed.
"""

from datetime import date, datetime, time
from util.utility import *
import json

# from music.song import Song
# from util.utility import format_date
from settings import *
from util.utility import *


class Playlist:
    """The class representing the concept of playlist.
    It includes a list of Song objects and the dates when the playlist was created and completed.
    """

    # Class variables: much like static fields in Java; typically defined and initialized before __init__()
    # Insert one or more class variables (static fields), such as phrases used in __str__(), date_pattern,...

    play_me = 'Play me :)' # staticko polje

    def __init__(self, name, *songs, created=date.today(), completed=date.today()):
        self.name = name
        self.songs = songs
        self.created = created
        self.completed = completed
        # self.__i = 0  # brojac iterator moze i ovde
        # pass                                            # introduce and initialize iterator counter, self.__i

    def __str__(self):
        n = self.name
        s = ', '.join([str(s) for s in self.songs]) if self.songs else '(empty)'
        from_to = format_date(self.created) + ' - ' + format_date(self.completed)
        return '\n'.join([n, s, from_to])

    def __eq__(self, other):
        return self.__dict__ == other.__dict__ if type(self) is type(other) else False

    @staticmethod
    def is_date_valid(d):
        """It is assumed that a playlist has not been created more than ~10 years ago.
        So, the valid date to denote the creation of a playlist is between Jan 01, 2011, and today.
        """
        return date(2011, 1, 1) <= d <= date.today()

    @staticmethod
    def parse_playlist_str(self, playlist_str):
        """Splits a playlist string into its typical segments.
        """
        pass

    # Alternative constructor
    @classmethod
    def from_playlist_str(cls, playlist_str):
        pass

    def __iter__(self):
        """Once __iter__() and __next__() are implemented in a class,
        we can create an iterator object by calling the iter() built-in function on an object of the class,
        and then call the next() built-in function on that object.
        It is often sufficient to just return self in __iter__(),
        if the iterator counter such as self.__i is introduced and initialized in __init__().
        Alternatively, the iterator counter (self.__i) is introduced and initialized  here.
        """

        self.__i = 0 # moze ovako lokalno a moze i kao atribut u konstruktoru
        return self               # sufficient if the iterator counter is introduced and initialized in __init__()

    def __next__(self):
        if self.__i < len(self.songs):
            s = self.songs[self.__i]
            self.__i += 1
            return s
        else:
            raise StopIteration


def next_song(playlist):
    # generator metoda u kojoj umesto return ima yield
    """Generator that shows the songs from a playlist, one at a time.
    yield produces a generator object, on which we call the next() built-in function.
    A great tutorial on generators: https://realpython.com/introduction-to-python-generators/.
    """

    for s in playlist:
        input("Next: ")
        yield s
        print('Yeah:')


class PlaylistError(Exception):
    """Base class for exceptions in this module.
    """

    pass


class PlaylistDateError(PlaylistError):
    """Exception raised when the date when a playlist was created is after the date when the playlist was completed.
    """

    # define __init__() to include an appropriate message if the input args (created, completed) dates are not OK

    pass


class PlaylistEncoder(json.JSONEncoder):
    """JSON encoder for Playlist objects (cls= parameter in json.dumps()).
    """

    def default(self, playlist):
        # recommendation: always use double quotes with JSON

        pass


def playlist_py_to_json(playlist):
    """JSON encoder for Playlist objects (default= parameter in json.dumps()).
    """

    pass


def playlist_json_to_py(playlist_json):
    """JSON decoder for Playlist objects (object_hook= parameter in json.loads()).
    """

    # The songs field is specified as *songs in Playlist.__init__(),
    # make sure to use tuple(json.loads(<songs in playlist_json>))

    pass


if __name__ == "__main__":

    from testdata.songs import *

    # Class variables (like static fields in Java; typically defined and initialized before __init__())
    print(Playlist.play_me)
    print()

    # Check the basic methods (__init__(), __str__(),...)
    pl = Playlist('My songs', *[across_the_universe, imagine, happiness_is_a_warm_gun],
                  created=date(2020, 2, 13),completed=date.today())
    print(pl)
    print()

    # Check date validator (@staticmethod is_date_valid(<date>))
    print(Playlist.is_date_valid(date(1971, 10, 11)))
    print(Playlist.is_date_valid(date(2018, 10, 11)))
    print()

    # Check the alternative constructor (@classmethod from_playlist_str(<playlist_str>))
    print()

    # Check the iterator
    # i = iter(pl) # samo inicijalizacija iteratora
    # while True:
    #     try:
    #         print(next(i))
    #     except StopIteration:
    #         break
    # print()

    # Repeated attempt to run the iterator fails, because the iterator is exhausted
    # print(next(i)) # ovo nece proci jer je iterator dosao do kraja
    # mora opet da se inicijalizuje kao:
    # i = iter(pl) # i onda ce ovako da radi

    # Demonstrate generators
    # next_s = next_song(pl) # samo inicijalizacija generatora
    # while True:
    #     try:
    #         print(next(next_s))
    #     except StopIteration:
    #         break
    # print()

    # Repeated attempt to run the generator fails, because the generator is exhausted
    # print(next(next_s)) # nece proci jer vise nemamo kroz sta da prolazimo
    next_s = next_song(pl) # mora opet prvo da se inicijalizuje
    print()

    # Demonstrate generator expressions
    e = (i**2 for i in [1,2,3])
    print(e) # printa da je e generatorski objekat
    print(next(e))
    print(next(e))
    print(next(e))
    print()

    # Demonstrate exceptions
    # Here's the hierarchy of built-in exceptions: https://docs.python.org/3/library/exceptions.html#exception-hierarchy

    # Demonstrate exceptions - the general structure of try-except statements, possibly including else and finally
    print()

    # Demonstrate exceptions - except: Exception as <e> (and then type(<e>), <e>.__class__.__name__, <e>.args,...)
    print()

    # Demonstrate exceptions - user-defined exceptions (wrong playlist date(s))
    print()

    # Demonstrate writing to a text file - <outfile>.write(), <outfile>.writelines()
    print()

    # Demonstrate reading from a text file - <infile>.read(), <infile>.readline()
    print()

    # Demonstrate writing to a binary file - pickle.dump()
    print()

    # Demonstrate reading from a binary file - pickle.load()
    print()

    # Demonstrate JSON encoding/decoding of Playlist objects
    # Single object
    print()

    # List of objects
    print()