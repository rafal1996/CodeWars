# Given a non-negative integer n, write a function to_binary/ToBinary
# which returns that number in a binary format.
#
# to_binary(1)  # should return 1
# to_binary(5)  # should return 101
# to_binary(11) # should return 1011

def to_binary(n):
    return int(bin(n)[2:])

print(to_binary(1))
print(to_binary(5))
print(to_binary(11))

