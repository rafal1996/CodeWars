# Create a function that takes one positive three digit integer
# and rearranges its digits to get the maximum possible number.
# Assume that the argument is an integer.
# Return null (nil for Ruby, nothing for Julia) if the argument is not valid.

def max_redigit(nums):
    return int(''.join(sorted(str(nums), reverse = True))) if nums>99 and nums <1000 else None

print(max_redigit(123))
print(max_redigit(555))