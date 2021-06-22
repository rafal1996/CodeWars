# You are given two sorted arrays that both only contain integers.
# Your task is to find a way to merge them into a single one, sorted in asc order.
# Complete the function mergeArrays(arr1, arr2), where arr1 and arr2 are the original sorted arrays.
#
# You don't need to worry about validation, since arr1 and arr2 must be arrays' \
# ' with 0 or more Integers. If both arr1 and arr2 are empty, then just return an empty array.

def merge_arrays(arr1, arr2):
    return sorted(set(arr1 + arr2))

print(merge_arrays([1,2,3,4], [5,6,7,8]))
print(merge_arrays([1,3,5,7,9], [10,8,6,4,2]))