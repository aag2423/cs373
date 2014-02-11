#!/usr/bin/env python3

"""
CS373: Quiz #10 (5 pts) <Jake>
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    (4 pts)

[(2, 3), (3, 4), (4, 5)]
[5, 7, 9]
[3, 4, 5]
<generator>
"""

print(list(zip([2, 3, 4], [3, 4, 5])))
print(list(map(lambda x, y : x + y, [2, 3, 4], [3, 4, 5])))
print([x + 1 for x in [2, 3, 4]])
print((x + 1 for x in [2, 3, 4]))
