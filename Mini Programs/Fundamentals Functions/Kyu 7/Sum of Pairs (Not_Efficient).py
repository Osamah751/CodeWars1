# It does (time out error) when running on a really long list of numbers

"""
***Sum of Pairs***
Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * entire pair is earlier, and therefore is the correct answer
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined (Based on the language)

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * entire pair is earlier, and therefore is the correct answer
== [3, 7]
Negative numbers and duplicate numbers can and will appear.

NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements. Be sure your code doesn't time out.
"""


def sum_pairs(ints, s):
    '''
    :param ints: a list of numbers
    :param s: the sum the user wants to get the pairs, of number, for
    :return: the pairs of elements from (the given list) that sums to be (the sum wanted)
    Time: O(n)
    '''

    sum = None
    hashTable = ()

    # Check each element in the list given
    for i in ints:
        # Calculate (sum wanted - current element)
        sumMinusElement = s - i

        # Check if the number exists in hash table
        # if so then we found a pair of numbers that sum to (s)
        if sumMinusElement in hashTable:
            sum = [sumMinusElement, i]
            break

        # if no in the (hashTable) add the current number to it
        hashTable += (i, )
    # if the pairs is not found then there is no pairs in the list that sums to (s)
    return sum


# Test Case #1: ([3, 7])
print(sum_pairs([10, 5, 2, 3, 7, 5], 10))

# Test Case #2: ([1, 7])
print(sum_pairs([1, 4, 8, 7, 3, 15], 8))