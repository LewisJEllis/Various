"""
Project Euler #4
Lewis J Ellis

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
print reduce(max, [x*y for x in range(100,1000) for y in range(x,1000) if int(str(x*y)[::-1]) == x*y])