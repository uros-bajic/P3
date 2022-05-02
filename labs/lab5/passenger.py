"""
LAB 5, class Passenger
"""

"""
Create the Passenger class with the following methods:

- a constructor (__init__()) that receives four input arguments that are used to 
  initialise the following 4 attributes:
     - name - the passenger's name and surname
     - country - the passanger's country of origin
     - passport - the passenger's passport number
     - is_COVID_safe - a boolean indicator variable; it is true if the passenger is vaccinated 
     or has recently been tested negative; the default value of this argument is False

- get and set methods for the *passport* attribute (using appropriate decorators);
  designate this attribute as private and assure that it is a string of length 6,
  consisting of digits only or a 6-digit number.

- a method that sets *is_COVID_safe* based on the value of its input parameters: 
  - evidence type: a string that should be either 'vaccinated' or 'tested_negative'
  - evidence date: the date of vaccination / PCR test; if given as a string, it is 
  expected to be in the following format: %d/%m/%Y
  The method sets *is_COVID_safe* to True if:
  - the vaccination was within the last 6 months OR
  - the negative test is not older than 3 days    
  Note: for datetime formatting codes, check this table:
  https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

- class method covid_free_Aussie_passenger for creating a passenger from Australia who is COVID safe
  (alternative constructor); the method receives the passenger's name and passport number.

- a method that returns a string representation of a Passenger object (__str__())

- a method that checks for equality of the given Passenger object and another object
  that is passed to the method as its input parameter (__eq__()); two passenger objects
  are considered the same if they are citizens of the same country and have the same passport number
"""

from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta


class Passenger:

    def __init__(self, name, country, passport, covid_safe=False):
        self.name = name
        self.country = country
        self.passport = passport # da smo stavili __passport kao antribut onda
        # direktno ide dodela, za njega ovaj seter i geter ne vaze
        self.is_COVID_safe = covid_safe

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

    def __str__(self):
        # plavi kruzic u pycharm IDE pored potpisa ukazuje na overrajdovanje, slicno kao zeleni trouglic u javi
        passenger_str = f"Passenger {self.name}, from {self.country}, "\
                        f"with passport number {self.passport}"
        passenger_str += ", with valid COVID permit" if self.is_COVID_safe else ", WITHOUT valid COVID permit"
        return passenger_str

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


if __name__ == '__main__':

    bob = Passenger("Bob Smith", "Serbia", "123456", True)
    john = Passenger("John Smith", "Spain", 987656, True)
    jane = Passenger("Jane Smith", "Italy", "987659")
    mike = Passenger.covid_free_Aussie_passenger("Mike Brown", "123654")

    print("PASSENGERS DATA:\n")
    print(bob)
    print(john)
    print(jane)
    print(mike)

    print()
    print("Checking if 'bob' and 'john' refer to the same passenger")
    print(bob == john)

    print("\nPASSENGERS DATA AFTER CHECKING COVID PERMITS:\n")
    jane.check_COVID_permit('vaccinated', '12/09/2021')
    print(jane)

    bob.check_COVID_permit('test_negative', '01/05/2022')
    print(bob)