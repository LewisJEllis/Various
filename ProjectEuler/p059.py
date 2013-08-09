# Here I assume only that space is the most common character.
# From there, with no additional knowledge, I derive the key.
n = eval('[' + open('p059_cipher.txt', 'r').readlines()[0] + ']')
print sum([c ^ k for c, k in zip(n, ([max(n[i::3], key=n[i::3].count) ^ ord(' ') for i in range(3)])*401)])
print (''.join([chr(max(n[i::3], key=n[i::3].count) ^ ord(' ')) for i in range(3)]))

# That was the one-liner-battle form. Here's a more readable version.

def space(l):
    # Return the most frequent element, which I assume to correspond to space
    return max(l, key=l.count)

a = chr(space(n[0::3]) ^ ord(' '))
b = chr(space(n[1::3]) ^ ord(' '))
c = chr(space(n[2::3]) ^ ord(' '))

key = (a + b + c)*401
print sum([c ^ k for (c,k) in zip(n, map(ord, key))])