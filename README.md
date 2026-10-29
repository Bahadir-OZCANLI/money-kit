# Money
This is a Money class to use in my projects.

## Why the project is useful?
The project allow to control of money and financial process in my projects. So, I can import it into any of my project.

## Items
The Money class gets two items;
    minor_units(int) --> the amount of money, every unit correspond a cent in Euro or kuruş in TRY
    currency    --> currency of money (EUR, TRY)

## Basic Features
- It allow to make process on money; 
    sum          --> __add__
    substraction --> __sub__
    multiply     --> __mul__
- Define the comparison conditions and set the hash method to not get fail when working with Set and Dict types.
    comparison --> __eq__
    list       --> __lt__
    hash       --> __hash__
- Seperating money with equal parts or by list of ratio.
    equal parts       --> allocate()
    by list of ration --> allocate_by([])

## About the design
- I used integers instead of floats because floats can not stored exactly, so I might break the system.
- When I set __eq__ method, it broke the the hash function so Set and Dict types can not be used. Because of this I set the __hash__ method.
- Allocate function call 'allocate_by()' function to get remainders. It first find the equal parts of amount, then add the leftovers to the equal parts from left to right.
- Negative amounts are not accepted at the initialize because we don't need debt or refund situation.
- I might accept the negative values but  I should have changed a lot parts, this version is best for my usage for now.
- I set __repr__ for developers understand the output meaningfully, and __str__ for the users.

## Usage
- Venv     --> Set the virtual environment, then activate it.
- Install  --> Install 'pytest' and 'python'.
- Import   --> 'from money import Money'
- Run test --> 'python -m pytest'