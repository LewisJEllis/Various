from calendar import weekday
print sum([1 for m in range(1200) if weekday(1901 + m//12, m % 12 + 1, 7) == 0])
