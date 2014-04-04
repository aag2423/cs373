#!/usr/bin/env python3

# ---------
# Store3.py
# ---------

"""
Extract Method (110)
Move Method (142)
Create Rental.get_frequent_renter_points()
"""

print("Store3.py")

class Movie (object) :
    REGULAR     = 0
    NEW_RELEASE = 1
    CHILDRENS   = 2

    def __init__ (self, title, price_code) :
        self.title = title
        self.set_price_code(price_code)

    def get_price_code (self) : # const
        return self.price_code

    def get_title (self) : # const
        return self.title

    def set_price_code (self, price_code) :
        self.price_code = price_code

class Rental (object) :
    def __init__ (self, movie, days_rented) :
        self.movie       = movie
        self.days_rented = days_rented

    """
    Movie
        REGULAR
        NEW_RELEASE
        CHILDRENS
    get_movie()
        get_price_code()
    """
    def get_charge (self) : # const
        result = 0
        if self.get_movie().get_price_code() == Movie.REGULAR :       # why not self.movie?
            result += 2
            if self.get_days_rented() > 2 :                           # why not self.days_rented?
                result += (self.get_days_rented() - 2) * 1.5
        elif self.get_movie().get_price_code() == Movie.NEW_RELEASE :
            result += self.get_days_rented() * 3
        elif self.get_movie().get_price_code() == Movie.CHILDRENS :
            result += 1.5
            if self.get_days_rented() > 3 :
                result += (self.get_days_rented() - 3) * 1.5
        return result

    def get_days_rented (self) : # const
        return self.days_rented

    """
    Movie
        NEW_RELEASE
    get_movie()
        get_price_code()
    """
    def get_frequent_renter_points (self) : # const
        if (self.get_movie().get_price_code() == Movie.NEW_RELEASE) and \
           (self.get_days_rented()            >  1) :                     # why not self.movie, self.days_rented?
            return 2
        return 1

    def get_movie (self) : # const
        return self.movie

class Customer (object) :
    def __init__ (self, name) :
        self.name    = name
        self.rentals = []

    def add_rental (self, rental) :
        self.rentals.append(rental)

    def get_name (self) : # const
        return self.name

    """
    iter(rentals).next()
        get_charge()
        get_frequent_renter_points()
        get_movie()
            get_title()
    """
    def statement (self) : # O(n)
        total_amount           = 0
        frequent_renter_points = 0
        result                 = "Rental Record for " + self.get_name() + "\n";
        for each in self.rentals :
            total_amount           += each.get_charge()
            frequent_renter_points += each.get_frequent_renter_points()
            result                 += "\t" + each.get_movie().get_title() + "\t" + str(each.get_charge()) + "\n" # each.get_harge() again!
        result += "Amount owed is " + str(total_amount)           + "\n"
        result += "You earned "     + str(frequent_renter_points) + " frequent renter points";
        return result

x = Customer("Penelope")
assert(x.statement() ==                     \
    "Rental Record for Penelope\n"        + \
    "Amount owed is 0\n"                  + \
    "You earned 0 frequent renter points")

x.add_rental(Rental(Movie("Shane", Movie.REGULAR), 2))
assert(x.statement() ==                     \
    "Rental Record for Penelope\n"        + \
    "\tShane\t2\n"                        + \
    "Amount owed is 2\n"                  + \
    "You earned 1 frequent renter points")

x.add_rental(Rental(Movie("Red River", Movie.REGULAR), 5))
assert(x.statement() ==                     \
    "Rental Record for Penelope\n"        + \
    "\tShane\t2\n"                        + \
    "\tRed River\t6.5\n"                  + \
    "Amount owed is 8.5\n"                + \
    "You earned 2 frequent renter points")

x.add_rental(Rental(Movie("Giant", Movie.NEW_RELEASE), 1))
assert(x.statement() ==                     \
    "Rental Record for Penelope\n"        + \
    "\tShane\t2\n"                        + \
    "\tRed River\t6.5\n"                  + \
    "\tGiant\t3\n"                        + \
    "Amount owed is 11.5\n"               + \
    "You earned 3 frequent renter points")

x.add_rental(Rental(Movie("2001", Movie.NEW_RELEASE), 3))
assert(x.statement() ==                     \
    "Rental Record for Penelope\n"        + \
    "\tShane\t2\n"                        + \
    "\tRed River\t6.5\n"                  + \
    "\tGiant\t3\n"                        + \
    "\t2001\t9\n"                         + \
    "Amount owed is 20.5\n"               + \
    "You earned 5 frequent renter points")

x.add_rental(Rental(Movie("Big Country", Movie.CHILDRENS), 3))
assert(x.statement() ==                     \
    "Rental Record for Penelope\n"        + \
    "\tShane\t2\n"                        + \
    "\tRed River\t6.5\n"                  + \
    "\tGiant\t3\n"                        + \
    "\t2001\t9\n"                         + \
    "\tBig Country\t1.5\n"                + \
    "Amount owed is 22.0\n"               + \
    "You earned 6 frequent renter points")

x.add_rental(Rental(Movie("Spartacus", Movie.CHILDRENS), 5))
assert(x.statement() ==                     \
    "Rental Record for Penelope\n"        + \
    "\tShane\t2\n"                        + \
    "\tRed River\t6.5\n"                  + \
    "\tGiant\t3\n"                        + \
    "\t2001\t9\n"                         + \
    "\tBig Country\t1.5\n"                + \
    "\tSpartacus\t4.5\n"                  + \
    "Amount owed is 26.5\n"               + \
    "You earned 7 frequent renter points")

print("Done.")
