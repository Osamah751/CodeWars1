'''
7 kyu
String ends with?

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
'''

def solution(string, ending):
    digits = len(ending)
    if digits == 0:
        return True
    if string[-(digits):] == ending:
        return True
    else:
        return False


# Test Case #1: (True)
# print (solution('abc', 'bc'))

# Test Case #2: (False)
# print (solution('abc', 'd'))

# Test Case #3: (False)
# print(solution('abc', 'abcdfg'))

# Test Case #4: (True)
print(solution('abc', ''))