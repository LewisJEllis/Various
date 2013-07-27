def spell(n):
    tens = [None, None, "twenty", "thirty", "forty",
          "fifty", "sixty", "seventy", "eighty", "ninety"]
    small = ["zero", "one", "two", "three", "four", "five",
           "six", "seven", "eight", "nine", "ten", "eleven",
           "twelve", "thirteen", "fourteen", "fifteen",
           "sixteen", "seventeen", "eighteen", "nineteen"]

    if n == 1000:
        return "one thousand"

    def rest(c, n):
        return "" if n == 0 else c + spell(n)
    if n < 20:
        return small[n]
    elif n < 100:
        a, b = divmod(n, 10)
        return tens[a] + rest(" ", b)
    elif n < 1000:
        a, b = divmod(n, 100)
        return small[a] + " hundred" + (" and" + rest(" ", b) if b else "")

def nsl(s):
    return len("".join(s.split()))

print sum([len("".join(spell(n).split())) for n in range(1,1001)])
