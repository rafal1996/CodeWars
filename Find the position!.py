# When provided with a letter, return its position in the alphabet.
# Input :: "a"
#
# Ouput :: "Position of alphabet: 1"
# This kata is meant for beginners. Rank and upvote to bring it out of beta

def position(a):
    char2 = ['a','b','c','d','e','f','g','h','i','j','k','l',
               'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return f"Position of alphabet: {char2.index(a) + 1}"

print(position("a"))
print(position("h"))
print(position("z"))

