#Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

def remove_exclamation_marks(s):
    count=s.count("!")
    s = s.replace('!','',count)
    return s

print(remove_exclamation_marks("Hello World!"))
print(remove_exclamation_marks("Hello World!!!"))
print(remove_exclamation_marks("Hi! Hello!"))
print(remove_exclamation_marks(""))
print(remove_exclamation_marks("Oh, no!!!"))