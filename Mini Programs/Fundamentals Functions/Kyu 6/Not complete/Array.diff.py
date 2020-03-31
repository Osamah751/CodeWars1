"""
6 kyu
Array.diff

Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
"""


def array_diff(a, b):
    letters_to_remove = []

    # for index in b:
    #     if index not in letters_to_remove:
    #         letters_to_remove.append(index)
    #
    # for number in a:
    #     if number in letters_to_remove:
    #         a.remove(number)
    #
    # return a

    numbers_to_remove = set(b)
    numbers_to_remove = list(numbers_to_remove)
    return list( number for number in a if number not in numbers_to_remove)


# Test Case 1: ([2])
# print(array_diff([1,2], [1]))

# Test Case 2: ([2, 2])
# print(array_diff([1,2,2], [1]))

# Test Case 3: ([1])
print(array_diff([1,2,2], [2]))

# Test Case 4: ([1, 2, 2])
# print(array_diff([1,2,2], []))

# Test Case 5: ([])
# print(array_diff([], [1, 2]))
