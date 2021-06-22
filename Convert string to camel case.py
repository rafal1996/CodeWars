# Complete the method/function so that it converts
# dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was
# capitalized (known as Upper Camel Case, also often referred to as Pascal case).
#
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

import re


def to_camel_case(text):
    if text == '':
        return ''

    word = ''.join([x.title() for x in re.split(r'[_-]', text)])

    if not text[0].isupper():
        new_string = word[0].lower() + word[1:]
        return new_string
    return word

print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))