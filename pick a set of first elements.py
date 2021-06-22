# Write a function to get the first elements of asequence.
# Passing a parameter n (default=1) will return the first n elements of the sequence.
# If n == 0 return an empty sequence []
#
# Examples
# arr = ['a', 'b', 'c', 'd', 'e']
# first(arr)    # --> ['a']
# first(arr, 2) # --> ['a', 'b']
# first(arr, 3) # --> ['a', 'b', 'c']

def first(seq, n=1):
    return seq[0:n]

arr = ['a', 'b', 'c', 'd', 'e']
print(first(arr))
print(first(arr, 2))
print(first(arr, 3))