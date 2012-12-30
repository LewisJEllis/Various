"""
Project Euler #6
Lewis J Ellis

The sum of the squares of the first ten natural numbers is ... 385
The square of the sum of the first ten natural numbers is ... 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

# Python's awesome lists make this easy:
print sum(range(101))**2 - sum([i*i for i in range(101)])