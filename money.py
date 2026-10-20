
class CurrencyMismatchError(Exception):
    """If two currency is not match."""
    

class Money:
    """
    Represents money (TRY)
    the smallest amount (1) represent 1 kurus in TRY, or cent in EUR
    """
    def __init__(self, minor_units, currency):

        if not isinstance(minor_units, int):
            raise TypeError("The minor units must be integer")
            # TypeErro because we demand only integer
        if currency == "" or currency is None:
            raise ValueError("The currency can not be empty")
            # ValueError because want a specific format but not empty value

        self.minor_units=minor_units
        self.currency=currency

    def __add__(self, m2):
        if self.currency==m2.currency:
            new_unit=self.minor_units+m2.minor_units
            return Money(new_unit, self.currency)        
        else:
            raise CurrencyMismatchError(f"The currencies are not matched. ({self.currency} and {m2.currency})")

    def __sub__(self, m2):
        if self.currency==m2.currency:
            new_unit=self.minor_units-m2.minor_units
            return Money(new_unit, self.currency)            
        else:
            raise CurrencyMismatchError(f"The currencies are not matched. ({self.currency} and {m2.currency})")

    def __mul__(self, money):
        if isinstance(money, Money):
            raise TypeError("Two money object should not be match.")
        elif isinstance(money, int):
           new_unit=self.minor_units*money
           return Money(new_unit, self.currency) 
        else:
            raise TypeError(f"There is an unexpected value.")
        
    def __lt__(self, money):
        if not self.currency==money.currency:
            raise CurrencyMismatchError(f"The currencies are not matched. ({self.currency} and {money.currency})")
        else:
            return self.minor_units < money.minor_units

    def __str__(self) -> str:
        return f"{self.minor_units//100}.{self.minor_units%100:02} {self.currency}"
        #// rounds down, toward minus infinity, not toward zero, fix at W43.

    def __repr__(self) -> str:
        return f"Money({self.minor_units}, '{self.currency}')"

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.minor_units == other.minor_units and self.currency == other.currency

    def __hash__(self) -> int:
        return hash((self.minor_units, self.currency))

m0=Money(1250,"TRY")
m1=Money(1250,"TRY")
m2=Money(1205,"TRY")
m3=Money(1205,"EUR")

print(m1)
print(m2)
s = set([m1,m0])
print(hash(m1)==hash(m0)) # It is True after I set the __hash__ method.
print(len(s))

print(f"Correct Add:{m1.__add__(m2)}")
#print(f"Wrong Add:{m1.__add__(m3)}") #CurrencyMismatchError

print(f"Correct Sub:{m1.__sub__(m2)}")
#print(f"Wrong Sub:{m1.__sub__(m3)}") #CurrencyMismatchError

print(f"Correct Mul:{m1.__mul__(10)}")
#print(f"Wrong Mul:{m1.__mul__(m2)}") # TypeError

print(f"Correct list:{sorted([m1,m2])}")
#print(f"Wrong list:{sorted([m1,m3])}") #CurrencyMismatchError

#sum([m1, m2]) #TypeError: unsupported operand type(s) for +: 'int' and 'Money'
#sum([m1, m2], start=[]) #TypeError: can only concatenate list (not "Money") to list
# the sum function start to call from left to right. ı think it give error because it doesn't know what the Money is. Look up __radd__ in the W43