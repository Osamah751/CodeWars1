"""
5 kyu
Moving Zeros To The End

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]

***** Best Answer *****
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
***********************
"""

def move_zeros(array):
    lst = []
    workspace = len(array)
    zeros = 0
    for i in array:
        if i == 0 and i is not False:
            zeros += 1
        else:
            lst.append(i)
    for j in range(zeros):
        lst.append(0)
    return lst

# Test Case 1: ([ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
# print(move_zeros([1,2,0,0,1,0,1,0,3,0,1]))

# Test Case 2: ([9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
# print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))

# Test Case 3: ([1,None,2,False,1,0,0])
# print(move_zeros([0,1,None,2,False,1,0]))