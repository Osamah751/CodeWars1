'''
7 kyu
Square Every Digit

Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer

input: square_digits(9119)
output: 811181
'''

def square_digits(num):
    '''
    This function takes a number and square each digit in it. then print the result
    :param num: (int)Number
    :return: (int)a new number made by squaring each digit in the input
    Time: O(n)
    '''
    digits = [int(x) for x in str(num)]

    for i in range(len(digits)):
        digits[i]= str(digits[i]**2)
    new_number = int(''.join(digits))
    return new_number


# Test Case #1:(811181)
print(square_digits(9119))