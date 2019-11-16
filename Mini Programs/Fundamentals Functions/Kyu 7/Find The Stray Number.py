'''
7 kyu
Find the stray number

Insructions:-
You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3
'''

def stray(arr):
    '''
    a function that finds the stray number in a list
    :param arr: a list of identical numbers except one number
    :return: the number only used ones in the list
    Time: O(1)
    '''
    # sort the numbers to make the stray number either at the beginning or the end of the array
    arr.sort()

    # if the first number is the same as the second then the first number is the stray number(after sorting)
    # otherwise the last number is the stray number
    if arr[0] != arr[1]:
        return arr[0]
    else:
        return arr[-1]


# Test Case #1: (2)
print(stray([1, 1, 1, 1, 1, 1, 2]))

# Test Case #2: (3)
print(stray([2, 3, 2, 2, 2]))

# Test Case #3: (3)
print(stray([3, 2, 2, 2, 2]))