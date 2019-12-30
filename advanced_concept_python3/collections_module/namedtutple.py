""" namedtuple which can use to replace tuple but not a drop-in replacement

namedtuple can use it like a struct, struct is basically a complex data type
that groups a list of variable under one name.

One of the benefits of using namedtuple over tuple is that you no longer have to
keep track of each item is named and accessed via class property, we can use dir
to track new properties

Named tuples are especially useful for assigning field names to result tuples
returned by the csv or sqlite3 modules using _make(iterabe)
"""

from collections import namedtuple

# namedtuple
Parts = namedtuple('Parts', 'id_num desc cost amount')
auto_parts = Parts(id_num='1234', desc='Ford Engine', cost=1200.00, amount=10)

print(auto_parts)
print(auto_parts.id_num)

# regular tuple
auto_parts = ('1234', 'Ford Engine', 1200.00, 10)

print(auto_parts)  # access the cost
# 1200.0

id_num, desc, cost, amount = auto_parts
print(f"id_num : {id_num}")

# convert dict into namedtuple
Parts = {'id_num': '1234', 'desc': 'Ford Engine',
         'cost': 1200.00, 'amount': 10}

# (**Parts) is equal to parts(**Parts)
parts = namedtuple('Parts', Parts.keys())(**Parts)
print(parts.desc)
