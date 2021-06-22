# You will be given a vector of strings.
# You must sort it alphabetically (case-sensitive,
# and based on the ASCII values of the chars) and then return the first value.
# The returned value must be a string, and have "***" between each of its letters.
# You should not remove or add elements from/to the array.

def two_sort(a):
    a.sort()
    b = [i+"***" for i in a[0][:-1]]
    c = "".join(b) + a[0][-1]
    return c

print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))
print(two_sort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]))