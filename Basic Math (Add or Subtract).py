# In this kata, you will do addition and subtraction on a given string.
# The return value must be also a string.
# Note: the input will not be empty.
#
# Examples
# "1plus2plus3plus4"  --> "10"
# "1plus2plus3minus4" -->  "2"

def calculate(s):
    return str((eval(s.replace('plus', '+').replace('minus', '-'))))

print(calculate('1minus2minus3minus4'))
print(calculate('1plus2plus3plus4'))
print(calculate('1plus2plus3minus4'))