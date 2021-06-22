# Complete the solution so that it returns a formatted string.
# The return value should equal "Value is VALUE" where value is a 5 digit padded number.
#
# Example:
# solution(5)  # should return "Value is 00005"

def solution(value):
    return f'Value is {value:05}'

print(solution(0))
print(solution(109))
print(solution(1204))