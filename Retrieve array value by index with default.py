# Complete the solution. It should try to retrieve the value of the array at the index provided.
# If the index is out of the array's max bounds then it should return the default value instead.
#
# data = ['a', 'b', 'c']
# solution(data, 1, 'd') # should == 'b'
# solution(data, 5, 'd') # should == 'd'

def solution(items, index, default_value):
    try:
        return items[index]
    except IndexError:
        return default_value

data = ['a', 'b', 'c']
print(solution(data, 1, 'd'))
print(solution(data, 5, 'd'))

