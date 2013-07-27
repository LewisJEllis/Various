# There's probably a nicer way to do this with a little number theory and modular arithmetic
# But this is a oneliner and I like oneliners.

print str(sum([i ** i for i in range(1, 1001)]))[-10:]