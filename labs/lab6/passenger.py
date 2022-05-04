"""
LAB 6, class Passenger
"""

"""
Create the FlightService enumeration that defines the following items (services):
snack, refreshments, meal, priority boarding, onboard wifi, onboard media, 
and an item for cases when services are not specified.
"""

from enum import Enum

class FlightService(Enum):
    snack = 'snack'
    refreshments = 'refreshments'
    meal = 'meal'
    priority_boarding = 'priority boarding'
    onboard_wifi = 'onboard wifi'
    onboard_media = 'onboard media'
    unspecificed = 'unspecified'

    @staticmethod
    def valid_service_str(str_value):
        return any([str_value in [s.value, s.name] for s in FlightService])

    @staticmethod
    def get_service_from_str(str_value):
        if not FlightService.valid_service_str(str_value):
            return None
        for s in FlightService:
            if str_value in [s.name, s.value]:
                return s


"""
Modify the Passenger class from Lab5 as follows:

In addition to the existing attributes, the class should also have the following attributes:
- airfare - the price the passenger has paid for the flight
- checked_in - a boolean indicator, true if the passenger has checked in 
- services - the attribute represents a list of flight services available to the passenger; 
  these services should be defined as elements of the FlightService enumeration.

The following methods of the Passenger class need to be revised:

- constructor (__init__()) - it should receive 5 input arguments, one for each attribute except the 
  *airfare* and *services* attributes. The arguments for the passenger's name, country, and passport 
  have to be specified; the arguments for *checked_in* and *is_COVID_safe* are False by default. 
  The *services* attribute should be initialised to an empty list, whereas *airfare* should be 
  defined as private and set to None.

- a method that returns a string representation of a given Passenger object (__str__()) so that it describes 
  a passenger with the extended set of attributes.

Finally, the following new methods should be added:

- get and set methods (using appropriate decorators) for the *airfare* attribute; the set method: 
  i) should assure that a non-negative numeric value is assigned to this attribute, and 
  ii) should be able to handle both float and string value as the input argument

- get and set methods (using appropriate decorators) for the *checked_in* attribute; the attribute 
  should be made private; the set method should assure that a passenger can check in only if they are COVID safe
"""

from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
from sys import stderr

class Passenger:

    def __init__(self, name, country, passport, covid_safe=False, checked_in=False):
        self.name = name
        self.country = country
        self.passport = passport # da smo stavili __passport kao antribut onda
        # direktno ide dodela, za njega ovaj seter i geter ne vaze
        self.is_COVID_safe = covid_safe
        self.checked_in = checked_in
        self.services = list()
        self.__airfare = None

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, value):
        if isinstance(value, int) and len(str(value)) == 6:
            self.__passport = value
            return
        if type(value) is str and len(value) == 6 and all([ch.isdigit() for ch in value]):
            self.__passport = int(value)
            return
        print("Error! Invalid input, cannot set the passport number.")
        self.__passport = None

    @property
    def airfare(self):
        return self.__airfare

    @airfare.setter
    def airfare(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.__airfare = value
        elif isinstance(value, str):
            try:
                value_num = float(value) if '.' in value else int(value)
                self.__airfare = value_num
            except ValueError as err:
                stderr.write(f"Error while parsing input for airfare:\n{err}\n")
        else:
            stderr.write(f"Error! Incorrect input type {type(value)}\n")

    @property
    def checked_in(self):
        return self.__checked_in

    @checked_in.setter
    def checked_in(self, value):
        self.__checked_in = False
        if value and self.is_COVID_safe:
            self.__checked_in = value
        elif not self.is_COVID_safe:
            stderr.write(f"Error! Passenger {self.name} cannot check in since they do not have valid COVID permit.\n")

    def __str__(self):
        passenger_str = f"{self.name}\n\tcountry: {self.country}\n\tpassport number: " \
                        f"{self.passport if self.passport else 'unknown'}\n"
        passenger_str += f"\tCOVID status: {'valid' if self.is_COVID_safe else 'invalid'}\n"
        passenger_str += f"\tcheck in status: {'done' if self.checked_in else 'not yet'}\n"
        passenger_str += f"\tairfare: {self.airfare if self.airfare else 'not paid yet'}\n"
        passenger_str += f"\textra services: {self.get_services_as_str()}"
        return passenger_str

    def get_services_as_str(self):
        return "None" if len(self.services) == 0 \
            else "; ".join([s.value for s in self.services])

    def check_COVID_permit(self, evidence_type, evidence_date):
        if evidence_type.lower() not in ['vaccinated', 'test_negative']:
            print(f"Error! Wrong input value ({evidence_type}). Cannot proceed!")
            return
        evidence_date = self.get_date(evidence_date) # static funkciji pristupamo preko self posto je u scope-u klase
        if evidence_date:
            if evidence_type == "test_negative":
                self.is_COVID_safe = evidence_date + timedelta(days=3) > datetime.now()
            else:
                self.is_COVID_safe = evidence_date + relativedelta(months=6) > datetime.now()

    # static metode su kao ispomoc metodama klase, one nemaju ni pristup objektima (self) ni atributima objekta
    @staticmethod
    def get_date(value):
        if isinstance(value, (date, datetime)):
            return value
        if isinstance(value, str):
            return datetime.strptime(value, "%d/%m/%Y")
        print(f"Error! Wrong input value ({str(value)}). Cannot proceed!")
        return None

    # classmethod
    @classmethod
    def covid_free_Aussie_passenger(cls, name, passport): # cls referenca na klasu kao takvu
        return cls(name, "Australia", passport, True)

    def __eq__(self, other):
        return isinstance(other, Passenger) and self.country == other.country and self.passport == other.passport


"""
Create the EconomyPassenger class that extends the Passenger class and has:

- method add_service_selection that receives a dictionary where keys are services the passenger has bought
  while values are the prices paid for those services. The services should be added to the passenger's 
  *services* list, while the prices should be used to increase the value of the *airfare* attribute, BUT this
  should be done only if the passenger has paid the airfare.
  The method should also print a report about the added services and the resulting increase in the airfare. 
  Note: keys in the input dictionary are expected to be elements of the FlightService enumeration.  

- overridden __str__ method so that it first prints "Economy class passenger" and then the available information 
  about the passenger
"""

class EconomyPassenger(Passenger):

    def add_service_selection(self, services_dict):
        if not self.airfare:
            stderr.write("Error! Services cannot be added until airfare is paid.\n")
            return

        tot_price = 0
        added_services = []

        for service, price in services_dict.items():
            if type(service) is FlightService:
                added_services.append(service)
                tot_price += price
        self.services.extend(added_services)
        self.airfare += tot_price

        print(f"For passenger {self.name}, the following services were added: "
              f"{'; '.join([s.value for s in added_services])}")
        print(f"Airfare increased by {tot_price}, for a total of {self.airfare}.")

    def __str__(self):
        return "Economy class passenger: " + super().__str__()

"""
Create class BusinessPassenger that extends the Passenger class and has:

- the constructor (__init__()) that receives the same arguments as the constructor of the upper class
  plus a list of services to be assigned to the *services* attribute. This additional argument should be 
  a tuple of either strings (service names) or elements of the FlightService enumeration; its default value
  is FlightService.unspecified. The method should check the validity of the tuple elements before adding 
  them to the *services* attribute. 
  Important: the constructor should be written in a way that makes the class ready for multiple inheritance.

- overridden __str__ method so that it first prints "Business class passenger" and then 
  the available information about the passengers

"""

class BusinessPassenger(Passenger):

    def __init__(self, services = (FlightService.unspecificed,), **kwargs):
        # prva stvar u konstruktoru izvedene klase jeste poziv konstruktora nadredjene klase (Java, Python...)
        super().__init__(**kwargs)

        for service in services:
            if isinstance(service, FlightService):
                self.services.append(service)
            elif isinstance(service, str) and FlightService.valid_service_str(service):
                self.services.append(FlightService.get_service_from_str(service))
            else:
                stderr.write(f"Error! Invalid value ({service}) for flight service!\n")

    def __str__(self):
        return "Business class passenger: " + super().__str__()

if __name__ == '__main__':

    # jim = EconomyPassenger("Jim Jonas", 'UK', '123456', covid_safe=True)
    # print(jim)
    # print()
    #
    # # Try adding extra services to Jim
    # extra_services = {
    #     FlightService.refreshments: 10,
    #     FlightService.onboard_media: 15
    # }
    # jim.add_service_selection(extra_services)
    #
    # jim.airfare = 450
    # jim.add_service_selection(extra_services)
    #
    # bob = EconomyPassenger("Bob Jones", 'Denmark', '987654', checked_in=True, covid_safe=True)
    # print(bob)
    # print()

    mike = BusinessPassenger(name="Mike Stone", country="USA",
                             passport='234567', covid_safe=True,
                             services=(FlightService.priority_boarding, FlightService.onboard_wifi))
    print(mike)
    print()
    print(mike.__dict__)

    brian = BusinessPassenger(name="Brian Brown", country="UK",
                              passport='546234', covid_safe=True,
                              services=("priority_boarding", "onboard media", "drinks"))
    print(brian)
