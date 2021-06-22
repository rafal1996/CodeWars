# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H
# Patrick Feeney => P.F

def abbrev_name(name):
    a = name.split()
    return "{}.{}".format(a[0][0], a[1][0]).upper()
print(abbrev_name('Sam Feeney'))
print(abbrev_name("Patrick Harris"))