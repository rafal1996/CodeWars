# Given a sequence of integers, return the sum of all the integers that have an even index,
# multiplied by the integer at the last index.
# Indices in sequence start from 0.
# If the sequence is empty, you should return 0.

def even_last(numbers):
    return 0 if len(numbers) == 0 else sum(numbers[::2]) * numbers[-1]

print(even_last([2, 3, 4, 5]))
print(even_last([]))