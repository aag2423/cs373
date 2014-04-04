#!/usr/bin/env python3

# ---------
# Store9.py
# ---------

"""
Introduce eager Singleton
Create Movie.get_output()
Remove Movie.getTitle()
Create Rental.statement()
Remove Rental.getMovie()
Remove Customer.get_total_charge()
Remove Customer.get_total_frequent_renter_points()
"""

print("Store9.py")

class Price (object) :
    def get_frequent_renter_points (self, days_rented) : # const
        return 1

def Singleton (c) :
    x = c()
    return lambda : x

@Singleton
class RegularPrice (Price) :
    def get_charge (self, days_rented) : # const
        result = 2
        if days_rented > 2 :
            result += (days_rented - 2) * 1.5
        return result

@Singleton
class NewReleasePrice (Price) :
    def get_charge (self, days_rented) : # const
        return days_rented * 3

    def get_frequent_renter_points (self, days_rented) :
        return 2 if (days_rented > 1) else 1

@Singleton
class ChildrensPrice (Price) :
    def get_charge (self, days_rented) : # const
        result = 1.5
        if days_rented > 3 :
            result += (days_rented - 3) * 1.5
        return result

class Movie (object) :
    def __init__ (self, title, price) :
        self.title = title
        self.price = price

    """
    price
        get_charge()
    """
    def get_charge (self, days_rented) : # const
        return self.price.get_charge(days_rented)

    """
    price
        get_frequent_renter_points()
    """
    def get_frequent_renter_points (self, days_rented) :
        return self.price.get_frequent_renter_points(days_rented)

    def get_output (self, days_rented) : # const
        return "\t" + self.title + "\t" + str(self.get_charge(days_rented)) + "\n"

class Rental (object) :
    def __init__ (self, movie, days_rented) :
        self.movie       = movie
        self.days_rented = days_rented

    """
    movie
        get_charge()
    """
    def get_charge (self) : # const
        return self.movie.get_charge(self.days_rented)

    """
    movie
        get_frequent_renter_points()
    """
    def get_frequent_renter_points (self) : # const
        return self.movie.get_frequent_renter_points(self.days_rented)

    """
    movie
        get_output()
    """
    def get_output (self) : # const
        return self.movie.get_output(self.days_rented)

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
        get_output()
    """
    def statement (self) : # O(n)
        amount = 0
        for each in self.rentals :
            amount += each.get_charge()
        points = 0
        for each in self.rentals :
            points += each.get_frequent_renter_points()
        result = "Rental Record for " + self.get_name() + "\n";
        for each in self.rentals :
            result += each.get_output()
        result += "Amount owed is " + str(amount) + "\n"
        result += "You earned "     + str(points) + " frequent renter points";
        return result

x = Customer("Penelope")
assert(x.statement() ==                     \
    "Rental Record for Penelope\n"        + \
    "Amount owed is 0\n"                  + \
    "You earned 0 frequent renter points")

x.add_rental(Rental(Movie("Shane", RegularPrice()), 2))
assert(x.statement() ==                     \
    "Rental Record for Penelope\n"        + \
    "\tShane\t2\n"                        + \
    "Amount owed is 2\n"                  + \
    "You earned 1 frequent renter points")

x.add_rental(Rental(Movie("Red River", RegularPrice()), 5))
assert(x.statement() ==                     \
    "Rental Record for Penelope\n"        + \
    "\tShane\t2\n"                        + \
    "\tRed River\t6.5\n"                  + \
    "Amount owed is 8.5\n"                + \
    "You earned 2 frequent renter points")

x.add_rental(Rental(Movie("Giant", NewReleasePrice()), 1))
assert(x.statement() ==                     \
    "Rental Record for Penelope\n"        + \
    "\tShane\t2\n"                        + \
    "\tRed River\t6.5\n"                  + \
    "\tGiant\t3\n"                        + \
    "Amount owed is 11.5\n"               + \
    "You earned 3 frequent renter points")

x.add_rental(Rental(Movie("2001", NewReleasePrice()), 3))
assert(x.statement() ==                     \
    "Rental Record for Penelope\n"        + \
    "\tShane\t2\n"                        + \
    "\tRed River\t6.5\n"                  + \
    "\tGiant\t3\n"                        + \
    "\t2001\t9\n"                         + \
    "Amount owed is 20.5\n"               + \
    "You earned 5 frequent renter points")

x.add_rental(Rental(Movie("Big Country", ChildrensPrice()), 3))
assert(x.statement() ==                     \
    "Rental Record for Penelope\n"        + \
    "\tShane\t2\n"                        + \
    "\tRed River\t6.5\n"                  + \
    "\tGiant\t3\n"                        + \
    "\t2001\t9\n"                         + \
    "\tBig Country\t1.5\n"                + \
    "Amount owed is 22.0\n"               + \
    "You earned 6 frequent renter points")

x.add_rental(Rental(Movie("Spartacus", ChildrensPrice()), 5))
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
