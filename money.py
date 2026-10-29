class CurrencyMismatchError(Exception):
    """If two currency is not matched."""    

class Money:
    """
    Represents money. amount --> minor_units, currency-->the currency of money.
    the smallest amount (1) represent 1 kurus in TRY, or cent in EUR.
    """
    def __init__(self, minor_units, currency):

        if not isinstance(minor_units, int):
            # TypeError because we demand only integer
            raise TypeError("The minor units must be integer")
        #I have decided to reject negative values because we don't need debt or refund right now.
        if minor_units<0:
            raise ValueError("The minor units can not be negative.")
        if not isinstance(currency,str) or currency == "" or currency is None:
            # ValueError because want a specific format but not empty value
            raise ValueError("The currency should be string and can not be empty")

        self.minor_units=minor_units
        self.currency=currency

    def allocate(self, n):
        """This method is for; to seperate a money to equal parts."""
        if not isinstance(n, int):
            #TypeError because we expect a specific format.
            raise TypeError("The n must be an integer.")
        if n<1:
            #ValueError because the n must be more than 0.
            raise ValueError("The n must be more than 0")
        liste=[1]*n
        #It call 'allocate_by' because not to use the 'leftover' loop twice.
        money_list = self.allocate_by(liste)
        
        return money_list

    def allocate_by(self, nlist):
        """This method is for; to seperate a money by a list of ratio."""
        total=0
        for i in nlist:
            if i<1:raise ValueError("The list can not be include negatives or zero.")
            total+=i
        if total<1:
            raise ValueError("The sum of the list should be at least 1 and can not be empty.")
        liste=[]
        for i in nlist:
            liste.append(self.minor_units*i//total)
        leftovers=self.minor_units-sum(liste)
        for i in range(leftovers):
            liste[i]+=1
        money_list=[]
        for i in liste:
            money_list.append(Money(i, self.currency))
        
        return money_list

    def __add__(self, m2):
        """Same currency only or CurrencyMismatchError. Not implemented for int."""
        if isinstance(m2, Money):
            if self.currency==m2.currency:
                new_unit=self.minor_units+m2.minor_units
                return Money(new_unit, self.currency)        
            else:
                raise CurrencyMismatchError(f"The currencies are not matched. ({self.currency} and {m2.currency})")
    
        return NotImplemented
        #NotImplemented because we tell Python 'I don't know how to handle this type' and let Python try another ways. If all is failed Python will raise the error.

    def __sub__(self, m2):
        """Same currency only or CurrencyMismatchError. Not implemented if int."""
        if isinstance(m2, Money):
            if self.currency==m2.currency:
                new_unit=self.minor_units-m2.minor_units
                return Money(new_unit, self.currency)            
            else:
                raise CurrencyMismatchError(f"The currencies are not matched. ({self.currency} and {m2.currency})")
         
        return NotImplemented            

    def __mul__(self, money):
        """Multiply with int. Else TypeError."""
        if isinstance(money, Money):
            raise TypeError("You can only multiply a money with an integer.")
        elif isinstance(money, int):
           new_unit=self.minor_units*money
           return Money(new_unit, self.currency) 
        else:
            raise TypeError(f"There is an unexpected value.")
        
    def __lt__(self, money):
        """Define the sorting behaviour. '<' """
        if isinstance(money, Money):
            if not self.currency==money.currency:
                raise CurrencyMismatchError(f"The currencies are not matched. ({self.currency} and {money.currency})")
            else:
                return self.minor_units < money.minor_units

        return NotImplemented

    def __str__(self) -> str:
        """Reject the negatives. """
        return f"{self.minor_units//100}.{self.minor_units%100:02} {self.currency}"        

    def __repr__(self) -> str:
        return f"Money({self.minor_units}, '{self.currency}')"

    def __eq__(self, other):
        """Define the comparison. Only '=='. """
        if not isinstance(other, Money):
            return NotImplemented
        return self.minor_units == other.minor_units and self.currency == other.currency

    def __hash__(self) -> int:
        """Define the hash to not get fail with Set and Dict types."""
        return hash((self.minor_units, self.currency))