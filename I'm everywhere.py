# Task:
# Your task is to make a function that takes the value of word
# and returns it with an "i" at the beginning of the word.
# For example we get the word "Phone", so we must return "iPhone". But we have a few rules:
#
# The word should not begin with the letter "I", for example Inspire.
# The number of vowels should not be greater than or equal to the number of consonants,
# for example East or Peace. ("y" is considered a consonant)
# The first letter should not be lowercase, for example road.
# If the word does not meet the rules, we return "Invalid word".

def i(word):
    samogloski = ('a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', "I", 'E')
    count = 0

    if word == '':
        return 'Invalid word'
    if word[0].islower():
        return 'Invalid word'
    if word[0] == "I":
        return 'Invalid word'

    for x in word:
        if x in samogloski:
            count += 1

    if count >= len(word) - count:
        return 'Invalid word'

    return 'i' + word

print(i('Phone'))
print(i('World'))
print(i(''))