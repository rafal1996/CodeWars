# Complete the solution so that it reverses all of the words within the string passed in.
#
# Example:
# "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"

def reverse_words(s):
    s = s.split()
    s = " ".join(reversed(s))
    return s
print(reverse_words("The greatest victory is that which requires no battle"))