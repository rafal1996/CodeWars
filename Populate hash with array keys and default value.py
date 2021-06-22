# Complete the function so that it takes an array of keys
# and a default value and returns a hash (Ruby) / dictionary (Python) with all keys set to the default value.
#
# Example
# ["draft", "completed"], 0   # should return {"draft": 0, "completed: 0}

def populate_dict(keys, default):
    return {x:default for x in keys}

print(populate_dict(["draft", "completed"], 0))
print(populate_dict(["a", "b", "c"], None))