"""
Project Euler #25
Lewis J Ellis

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""
import math

p1 = 1
p2 = 1
fn = p1 + p2
n = 3



# This is probably doable with a crafty list comprehension using this while condition in the if condition. To think about later.
while math.floor(math.log10(fn)+1) < 1000:
  p1 = p2
  p2 = fn
  fn = p1 + p2
  n += 1
print n
