# Write a function that reverses the bits in an integer.
# For example, the number 417 is 110100001 in binary. Reversing the binary is 100001011 which is 267.
# You can assume that the number is not negative.

def reverse_bits(n):
    return int(bin(n)[2:][::-1],2)

print(reverse_bits(417))
print(reverse_bits(267))
print(reverse_bits(2017))