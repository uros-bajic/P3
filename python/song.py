"""Domain classes and functions related to the concept of song.
"""


# from util import utility
# from music.enums import *
import json

# kao i u Javi, klasa object je nadklasa svih klasa

# 4 stvari kada se razmislja o klasama:
# konstruktori, seteri i geteri, toString i equals

class Song:
    """The class describing the concept of song.
    It is assumed that a song is sufficiently described by its
    title and whether it is "unplugged" song or not.

    This class illustrates some of the important concepts of Python classes:
    - self
    - __init__()
    - __str__()
    - __eq__(self, other) is the equivalent of Java equals() and should be overridden in classes
    - __dict__ attribute of all objects
    - data fields (instance variables)
    - methods - calling them by self.<method>(...) from the same class where they are defined
    """
    # polja klase se navode samo u konstuktoru
    # ne pre kao sto je u Javi slucaj
    # self - this iz Jave
    # za razliku od jave self se obavezno pise
    # u svakoj python-ovoj metodi, pa i u konstruktoru

    def __init__(self, title, is_unplugged=False):
        self.title = title
        self.is_unplugged = is_unplugged
        self.__n = 'kkk'                                    # 'private' field
        self._n = 'lll'                                     # 'protected' field

    # Properties: 'private' fields:
    #   @property
    #   def <attr>(self):
    #       return self.__<attr>
    #   @<attr>.setter
    #   def <attr>(self, <attr>):
    #       self.__<attr> = <attr> if ... else ...
    # Run setters and getters in the debugger.
    # Make title a property (after setting up __init__(), __str__(), __eq__(), methods,...).

    # Add an immutable property (no setter for it) - just return self; prints as __str__().
    # dekorator @property za privatne atribute
    # on dekorise funkciju atributa koji zelimo da proglasimo privatnim

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title if isinstance(title, str) else 'unknown0'

    # pandan Javine toString metode
    def __str__(self):
        return f'{self.title}' if not self.is_unplugged else \
            f'{self.title} (unplugged)'

    def __eq__(self, other):
        # isinstance je instanceof u Javin
        isi = isinstance(other, Song) # da li je other instance of Song
        t = self.title == other.title
        u = self.is_unplugged = other.is_unplugged
        # proveravamo da li je instanca klase pa onda da li ima
        # iste vrednosti polja
        return isi and t and u

    def play(self, artist, *args, **kwargs):
        """Assumes that artist, *args (e.g. expressions of gratitude) and kwargs.values() (e.g. messages) are strings.
        Prints song title, artist, and things like rhythm counts, expressions of gratitude and messages. A call example:
            <song>.play(artist, *['Thank you!', 'You're wonderful!], love='We love you!')
        """
        print(f'{self.title} ({artist})')

    # bitno - ako u nekoj metodi klase imamo poziv druge metode klase
    # u Javi nije bilo bitno da stavimo this, e ovde sada jeste

    def play_song(self, artist, *args, **kwargs):
        """Demonstrates calling another method from the same class (self.<method>(...) as a mandatory syntax).
        """
        self.play(artist, *args, **kwargs)

    # Alternative constructor
    @classmethod
    def from_str(cls, song_string):
        """Inverted __str__() method.
        Assumes that song_string is in the format generated by __str__().
        """

        pass


class SongEncoder(json.JSONEncoder):
    """JSON encoder for Song objects (cls= parameter in json.dumps()).
    """

    def default(self, song):
        # recommendation: always use double quotes with JSON

        pass
        # can simply return song_py_to_json(song), to avoid code duplication


def song_py_to_json(song):
    """JSON encoder for Song objects (default= parameter in json.dumps()).
    """

    # recommendation: always use double quotes with JSON


def song_json_to_py(song_json):
    """JSON decoder for Song objects (object_hook= parameter in json.loads()).
    """


class Ballad(Song):
    """The class describing the concept of ballad.
    It is assumed that a ballad is sufficiently described as a Song,
    with the addition of whether its tempo is slow or moderate.

    Useful link (related to inheritance in Python):
    https://stackoverflow.com/questions/3394835/use-of-args-and-kwargs/3394902#3394902 (calling super() in constructors)
    """

    # Version 1 - no multiple inheritance

    # Version 2 - with multiple inheritance

    def __str__(self):
        pass

    def __eq__(self, other):
        # Recommended if inheritance is involved
        # (https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes):
        # if type(other) is type(self):
        #     return self.__dict__ == other.__dict__
        # return False
        pass

    def play(self, artist, *args, **kwargs):
        """Assumes that artist, *args (e.g. expressions of gratitude) and kwargs.values() (e.g. messages) are strings.
        Prints song title, artist, and things like rhythm counts, expressions of gratitude and messages. A call example:
            <song>.play(artist, *['Thank you!', 'You're wonderful!], love='We love you!')
        """
        pass


class PianoSong(Song):
    """The class describing the concept of piano song.
    It is assumed that a piano song is sufficiently described as a song
    in which the dominating instrument is piano.
    """

    # Version 1 - no multiple inheritance

    # Version 2 - with multiple inheritance

    def __str__(self):
        pass

    def __eq__(self, other):
        # Recommended if inheritance is involved
        # (https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes):
        # if type(other) is type(self):
        #     return self.__dict__ == other.__dict__
        # return False

        pass

    def details(self):
        """Just a simple method to indicate details of a piano song.
        """

        pass


class PianoBallad(Ballad, PianoSong):
    """The class describing the concept of piano ballad.
    It is assumed that a piano ballad is sufficiently described as a song that is simultaneously piano-dominated.

    Useful links :
    https://stackoverflow.com/a/50465583/1899061 (designing classes (i.e. their __init__() methods) for multiple inh.)
    https://stackoverflow.com/a/533675/1899061 (mixins explained, and what good they are in multiple inheritance)
    """

    def __str__(self):
        pass

    def __eq__(self, other):
        # Recommended if inheritance is involved
        # (https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes):
        # if type(other) is type(self):
        #     return self.__dict__ == other.__dict__
        # return False

        pass


if __name__ == "__main__":

    # from testdata.songs import *

    # Print objects
    imagine = Song('Imagine', True)
    print(imagine)
    print()

    # Compare objects
    print(imagine == Song('Imagine'))
    print()

    # Access data fields (instance variables), including 'private' fields
    print(imagine.title)
    imagine.title = 'Imagine'
    print(imagine.title)
    imagine.is_unplugged = False
    print(imagine.is_unplugged)
    print()
    print(imagine._n) # oko protected se ne buni
    # print(imagine.__n) # za ovo kao private se buni
    print(imagine._Song__n) # za ovo se opet ne buni
    print()
    # iako je navodno privatni ima fore da se provali
    # u Pythonu nista nije zagarantovao private ili
    # protected kao u javi, sve moze da bude public
    # onoliko koliko mi zelimo, osim ako ne koristimo posebne pakete

    imagine.year =1971
    print(imagine.year)

    # Add new data fields (instance variables)
    #   1. <object>.<new_attr> = <value>
    #   2. <object>.__setattr__('<new_attr>', <value>)      # counterpart: <object>.__getattribute__('<attr>')
    #   3. setattr(<object>, '<new_attr>', <value>))        # counterpart: getattr(<object>, '<attr>')
    print()

    # Calling methods
    imagine.play('John Lennon')
    imagine.play_song('John Lennon')
    print()

    # Demonstrate object data fields and methods in Python Console for some built-in classes (boolean, int, object,...)
    # - True + 1
    # - True.__int__()
    # - (1).__class__.__name__
    # - (1).__class__
    # - o.__dir__()
    # - o.__dir__
    # - o.__dict__

    # Demonstrate object data fields and methods for Song objects
    print()

    # Demonstrate @classmethod (from_str())
    print()

    # Demonstrate inheritance
    # object class
    #   it's like the Object class in Java
    #   all classes inherit from object - try, e.g., list.__mro__ in the console
    #   object class defines object.__eq__(self, other) etc.
    #   object.__ne__(self, other), the inverse of object.__eq__(self, other),
    #   is provided by Python automatically once object.__eq__(self, other) is implemented
    print()

    # Demonstrate method overriding
    print()

    # Demonstrate multiple inheritance and MRO.
    # Make sure to read this first: https://stackoverflow.com/a/50465583/1899061 (especially Scenario 3).
    print()

    # Demonstrate JSON encoding/decoding of simple data types.
    # Refer to https://docs.python.org/3.3/library/json.html#encoders-and-decoders for details.
    print()

    # Demonstrate JSON encoding/decoding of Song objects
    # Single object
    print()

    # List of objects
    print()