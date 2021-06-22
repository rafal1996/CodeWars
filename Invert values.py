# Given a set of numbers, return the additive inverse of each.
# Each positive becomes negatives, and the negatives become positives.
#
# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []

import numpy as geek
def invert(lst):
    return [geek.invert(x)+1 for x in lst]

print(invert([1,2,3,4,5]))
print(invert([1,-2,3,-4,5]))
print(invert([]))