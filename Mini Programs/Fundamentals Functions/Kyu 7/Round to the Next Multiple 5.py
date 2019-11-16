'''
7 kyu
Round to the next multiple of 5.

Given an integer as input, can you round it to the next (meaning, "higher") 5?

Examples:

input:    output:
0    ->   0
2    ->   5
3    ->   5
12   ->   15
21   ->   25
30   ->   30
-2   ->   0
-5   ->   -5
etc.
Input may be any positive or negative integer (including 0).

You can assume that all inputs are valid integers.
'''


def round_to_next5(n):
    # Your code here
    return n

# Test Case #1: (0)
print(round_to_next5(0))

# Test Case #2:
print(round_to_next5(1))

# Test Case #3: (0)
print(round_to_next5(-1))