# Given a random non-negative number,
# you have to return the digits of this number within an array in reverse order.
# Example:
# 348597 => [7,9,5,8,4,3]

def digitize(n):
    return [int(a) for a in str(n)][::-1]

print(digitize(35231))
print(digitize(23582357))
print(digitize(45762893920))