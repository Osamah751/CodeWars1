"""
7 kyu
Remove the minimum

The museum of incredible dull things
The museum of incredible dull things wants to get rid of some exhibitions. Miriam, the interior architect,
comes up with a plan to remove the most boring exhibitions.
She gives them a rating, and then removes the one with the lowest rating.

However, just as she finished rating all exhibitions, she's off to an important fair,
so she asks you to write a program that tells her the ratings of the items after one removed the lowest one. Fair enough.

Task
Given an array of integers, remove the smallest value. Do not mutate the original array/list.
If there are multiple elements with the same value, remove the one with a lower index.
If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.
"""


def remove_smallest(numbers):
    # return if the array is empty
    if len(numbers) == 0:
        return numbers

    # find the smallest_number in the array and find its index
    smallest_number = numbers[0]
    num_index = 0
    for index in range(len(numbers)):
        if numbers[index] < smallest_number:
            smallest_number = numbers[index]
            num_index = index

    # make a copy of the given array then remove the index of the smallest_number
    arr = numbers[:]
    arr.pop(num_index)
    return arr


# Test Case #1: [2, 3, 4, 5]
print(remove_smallest([1, 2, 3, 4, 5]))

# Test Case #2: [5, 3, 2, 4]
print(remove_smallest([5, 3, 2, 1, 4]))

# Test Case #3: [2, 3, 1, 1]
print(remove_smallest([1, 2, 3, 1, 1]))

# Test Case #4: []
print(remove_smallest([]))


