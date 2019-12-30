""" Counter

Counter class can run it against most iterables
"""

from collections import Counter

print(Counter('superfluous'))
# Counter({'u': 3, 's': 2, 'p': 1, 'e': 1, 'r': 1, 'f': 1, 'l': 1, 'o': 1})

counter = Counter('superfluous')
print(counter['u'])  # 3

# elements which an iterator over the lements that
# are in the dictionary, but in arbitrary order
print(list(counter.elements()))

# most_common items are by passing in a number
print(counter.most_common(2))

# subtract methos accepts an iterable or mapping and
# uses that arg to subtract
counter_two = counter.copy()
counter_two.subtract('super')

print(counter_two)
