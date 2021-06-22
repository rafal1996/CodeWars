# Your task is to sort a given string. Each word in the string will
# contain a single number. This number is the position the word should have in the result.
#
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
#
# If the input string is empty, return an empty string. The words in the input String
# will only contain valid consecutive numbers.
#
# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""

def order(sentence):
    a = dict()
    word = list(map(str, sentence.split()))

    new = []

    for x in word:

        if "1" in x:
            a[1] = x
        elif "2" in x:
            a[2] = x
        elif "3" in x:
            a[3] = x
        elif "4" in x:
            a[4] = x
        elif "5" in x:
            a[5] = x
        elif "6" in x:
            a[6] = x
        elif "7" in x:
            a[7] = x
        elif "8" in x:
            a[8] = x
        elif "9" in x:
            a[9] = x

    dictionary_items = a.items()
    sorted_items = sorted(dictionary_items)

    for i in range(len(sorted_items)):
        new.append(sorted_items[i][1])
    return " ".join(x for x in new)


print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))