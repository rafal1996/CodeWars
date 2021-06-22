# Given an array of numbers, check if any of the numbers are the character codes
# for lower case vowels (a, e, i, o, u).
# If they are, change the array value to a string of that vowel.
# Return the resulting array.

def is_vow(inp):
    b = {97: 'a', 101: 'e', 105: 'i', 111: "o", 117: 'u'}
    for i in inp:
        if i in b:
            c = inp.index(i)
            inp.pop(c)
            inp.insert(c, b[i])
    return inp

print(is_vow([118,117,120,121,117,98,122,97,120,106,104,116,113,114,113,120,106 ]))
print(is_vow([101,121,110,113,113,103,121,121,101,107,103 ]))