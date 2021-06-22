#The code provided is supposed replace all the dots '.' in the specified String str with dashes '-'

import re
def replace_dots(str):
    return re.sub(r"\.", "-", str)

print(replace_dots(""))
print(replace_dots("no dots"))
print(replace_dots("one.two.three"))
