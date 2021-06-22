# Write a function that takes an array of strings as an argument
# and returns a sorted array containing the same strings, ordered from shortest to longest.
# For example, if this array were passed as an argument:
# ["Telescopes", "Glasses", "Eyes", "Monocles"]
# Your function would return the following array:
# ["Eyes", "Glasses", "Monocles", "Telescopes"]

def sort_by_length(arr):
    return sorted(arr, key = len)

print(sort_by_length(["beg", "life", "i", "to"]))
print(sort_by_length(["longer", "longest", "short"]))