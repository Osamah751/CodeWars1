'''
7 kyu
Sum of all the multiples of 3 or 5

Your task is to write function findSum.

Upto and including n, this function will return the sum of all multiples of 3 and 5.

For example:

findSum(5) should return 8 (3 + 5)

findSum(10) should return 33 (3 + 5 + 6 + 9 + 10)
'''


def find(n):
    # set a place to add the founded numbers
    sum = 0
    # try all the number from 1 to (n)
    for i in range(1, n+1):
        # if they are either divisible by 3 or 5 add it to sum
        if i%3==0 or i%5==0:
            sum += i
    return sum


# Test Case #1: (8)
print(find(5))

# Test Case #2: (33)
print(find(10))