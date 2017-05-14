class Animal(object):
    def __init__(self):
        print
        "Animal created"

    def whoAmI(self):
        print
        "Animal"

    def eat(self):
        print
        "Eating"


class Dog(Animal):
    def __init__(self):
        # Animal.__init__(self)
        print
        "Dog created"

    def whoAmI(self):
        print
        "Dog"

    def bark(self):
        print
        "Woof!"


d = Dog()
d.eat()


class Book(object):
    def __init__(self, title, author, pages):
        print
        "A book is created"
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title:%s , author:%s, pages:%s " % (self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print
        "A book is destroyed"


book = Book("Python Rocks!", "Jose Portilla", 159)


class Vehicle(object):
    """A vehicle for sale by Jeffco Car Dealership.

    Attributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    """

    base_sale_price = 0

    def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Vehicle object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """Return the sale price for this vehicle as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)


class Car(Vehicle):
    def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Car object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on
        self.base_sale_price = 8000


class Truck(Vehicle):
    def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Truck object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on
        self.base_sale_price = 10000


a = Car(3, 1, 'dodge', '11', '2012', '21')
b = a.purchase_price()
print
b
print
a.wheels
