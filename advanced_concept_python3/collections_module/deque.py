""" deques are generalizatiohn of stacks and queues

Replacement container for the python list Deques are thread-safe [re-entrant]
and support memory efficient appends and pops either side of the deque.

List is optimized for fast fixed-length operations.
deque accepts a maxlen argument which sets the bounds for the deque. Otherwise
will grow to an arbitrary size

Any new items added to full bounded deque will cause the same number of items to
poped off the other end

- deque :
    As general rule, if you need fast appends or fast pops, use deque.

- list :
    For fast random access
"""

from collections import deque
import string

# create deque and print ascii a-z
d = deque(string.ascii_lowercase)
for letter in d:
    print(letter)

d.append('bork')
print(d)

d.appendleft('test')
print(d)

# rotate onee time to the right
d.rotate(1)
print(d)


def get_last(filename, n=5):
    """

    Parameters
    ----------
    filename : file
        The file to open
    n: integer (default is 5)


    Returns
    -------
    deque
        a deque of n tail line of the open file
    """
    try:
        with open(filename) as f:
            return deque(f, n)
    except OSError:
        print(f"Error opening file: {filename}")
        raise


k = get_last("./deque.py")
print(k)

k.append('new append to end')
print(k)

k.appendleft('new append to start')
print(k)

# 1
# 2
# 3
# 4
# 5
