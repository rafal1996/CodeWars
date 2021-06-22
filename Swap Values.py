# I would like to be able to pass an array with two elements to my swapValues function
# to swap the values. However it appears that the values aren't changing.

def swap_values(args):
    args[0], args[1] = args[1], args[0]
    return args

print(swap_values([2, 1]))