""" OrderedDict is keep track of the order of the keys as they are added

- Regular dict
    is an unordered data colleciton

- OrderedDict
    When compare two OrderedDict will also order and items for equality.
    Also support reversed iteration

"""

# dict order may be diff overtime when execute, especially add new items
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
print(f"regular dict {d}")

# use OrderedDict
from collections import OrderedDict

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# noinspection PyTypeChecker
new_d = OrderedDict(sorted(d.items()))
print(new_d)

for key in new_d:
    print(key, new_d[key])

