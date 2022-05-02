"""
LAB 5, class Flight
"""

"""
Create the Flight class with the following elements:

- class attribute *departure_format* representing the expected format for 
  the departure date and time; its value should be "%Y-%m-%d %H:%M"

- a constructor (__init__()) that receives two input parameters and uses them to initialise 
  *flight_num* (flight number) and *departure* (departure date and time) attributes; 
  it also initialises the *passengers* attribute (a list of objects of the Passenger class) 
  to an empty list

- get and set methods for the *departure* attribute (using appropriate decorators); 
  make this attribute private and assure that it is a datetime object that refers to 
  a moment in the future

- a method for adding a passenger to the *passengers* list; the method adds a new passenger 
  only if the input parameter is of the Passenger class, if the passenger is not already 
  in the list, and if he/she is covid safe

- a method that returns a string representation of the given Flight object (__str__())

- a method that returns the time left till departure as a tuple of the form (days, hours, mins)

- methods for turning the given Flight object into an iterator (__iter__(), __next__()) over the 
  flight passengers (that is, elements of the *passengers* list)

"""
from datetime import datetime
from labs.lab5.passenger import Passenger


class Flight:
    # class atributi jedini su koje zadajemo eksplicitno u okviru klase
    # obicni, na nivou objekata se uvode u okviru konstruktora
    departure_format = "%Y-%m-%d %H:%M"

    def __init__(self, flight_num, departure):
        self.flight_num = flight_num
        self.departure = departure
        self.passengers = list()

    @property
    def departure(self):
        return  self.__departure

    @departure.setter
    def departure(self, value):
        if isinstance(value, datetime) and value > datetime.now():
            self.__departure = value
            return
        if isinstance(value, str):
            dt_value = datetime.strptime(value, Flight.departure_format)
            if dt_value > datetime.now():
                self.__departure = dt_value
                return
        print("Error when setting the departure date and time.")
        self.__departure = None # uvek treba dodeliti neku vrednost
        # atributu ili ce on prakticno ostati nevidljiv, ne bi se znalo za njegovo postojanje

    def add_passenger(self, p):
        if type(p) is Passenger and p not in self.passengers and p.is_COVID_safe:
            self.passengers.append(p)
        else:
            print("Error! The passenger cannot be added!")

    def __str__(self):
        flight_str = f"Flight, number {self.flight_num}, " \
                     f"scheduled departure date/time: " \
                     f"{datetime.strftime(self.departure, Flight.departure_format) if self.departure else 'unknown'}"
        if len(self.passengers) == 0:
            flight_str += "\nStill no passengers."
        else:
            flight_str += f"\nPassengers on the flight:\n" + '\n'.join([str(p) for p in self.passengers])
        return flight_str

    def time_till_departure(self):
        if self.departure:
            time_left = self.departure - datetime.now()
            hours_left, rest_sec = divmod(time_left.seconds, 3600)
            mins_left, rest_sec = divmod(rest_sec, 60)
            return time_left.days, hours_left, mins_left

        print("Departure time is still unknown")
        return None

    def __iter__(self):
        self.__i = 0
        return self

    def __next__(self):
        if len(self.passengers) > self.__i:
            next_passenger = self.passengers[self.__i]
            self.__i += 1
            return next_passenger
        raise StopIteration


if __name__ == '__main__':

    lh1411 = Flight('LF1411', '2022-12-05 6:50')
    lh992 = Flight('LH992', '2022-11-25 12:20')

    print("\nFLIGHTS DATA:\n")
    print(lh1411)
    print()
    print(lh992)

    print()

    bob = Passenger("Bob Smith", "Serbia", "123456", True)
    john = Passenger("John Smith", "Spain", 987656, True)
    jane = Passenger("Jane Smith", "Italy", "987659")
    mike = Passenger.covid_free_Aussie_passenger("Mike Brown", "123654")

    for p in [bob, john, jane, mike]:
        lh1411.add_passenger(p)

    print("\nTRYING TO ADD A PASSENGER WHOIS ALREADY IN THE LIST")
    lh1411.add_passenger(Passenger("J Smith", "Spain", "987656", True))
    print()

    print(f"\nFLIGHTS DATA AFTER ADDING PASSENGERS TO THE FLIGHT {lh1411.flight_num}:\n")
    print(lh1411)

    print()

    days, hours, mins = lh1411.time_till_departure()
    print(f"Time till departure of the flight {lh1411.flight_num}: {days} days, {hours} hours, and {mins} minutes")

    print()
    print("\nPASSENGERS ON FLIGHT LH1411:")
    flight_iter = iter(lh1411)

    try:
        while True:
            print(next(flight_iter))
    except StopIteration:
        print("No more passengers")

    print()

    print("\nPASSENGERS ON FLIGHT LH1411 (FOR loop):")
    for passenger in lh1411:
        print(passenger)



