"""
Project Euler #4
Lewis J Ellis

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
# I should revisit this later and refactor it to look nicer. It's kind of ugly (break flag eww) and only has like two nice parts. But it works, and there are more interesting problems to be solved.
b1 = 100
b2 = 999
f = False
for i in range(0,(b2-b1)):
  if f:
    break
  l = (range(i/2+1))
  l.reverse()
  for j in l:
    p = str((b2-j)*(b2-i+j))
    if all([p[k] == p[5-k] for k in range(3)]):
      print p
      f = True
      break
