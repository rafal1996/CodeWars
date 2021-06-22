# You are given a string of n lines, each substring being n characters long. For example:
#
# s = "abcd\nefgh\nijkl\nmnop"
#
# We will study the "horizontal" and the "vertical" scaling of this square of strings.
#
# A k-horizontal scaling of a string consists of replicating k times each character of the string (except '\n').
#
# Example: 2-horizontal scaling of s: => "aabbccdd\neeffgghh\niijjkkll\nmmnnoopp"
# A v-vertical scaling of a string consists of replicating v times each part of the squared string.
#
# Example: 2-vertical scaling of s: => "abcd\nabcd\nefgh\nefgh\nijkl\nijkl\nmnop\nmnop"
# Function scale(strng, k, v) will perform a k-horizontal scaling and a v-vertical scaling.

def scale(strng, k, n):
    new = []
    if strng == "":
        return strng
    b = strng.split("\n")
    for i in range(len(b)):
        for x in range(n):
            new.append(b[i])
    c ="\n".join(new)
    new =''.join([x*k for x in c])
    new = new.split('\n')
    return "\n".join(new[::k])

a = "abcd\nefgh\nijkl\nmnop"
print(scale(a, 2, 3))