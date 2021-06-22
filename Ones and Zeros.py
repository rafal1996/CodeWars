# Given an array of ones and zeroes, convert the equivalent binary value to an integer.
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
# Examples:
# Testing: [0, 0, 0, 1] ==> 1
# Testing: [0, 0, 1, 0] ==> 2

def binary_array_to_number(arr):
    return int(''.join(str(x) for x in arr), 2)

print(binary_array_to_number([0,0,0,1]))
print(binary_array_to_number([1,1,1,1]))