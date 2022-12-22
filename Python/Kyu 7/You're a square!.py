
'''
7 kyu
You're a square!

A square of squares
You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!

However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.

Task
Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.

Examples
isSquare(-1) returns  false
isSquare(0) returns   true
isSquare(3) returns   false
isSquare(4) returns   true
isSquare(25) returns  true
isSquare(26) returns  false
'''


def is_square(n):
    '''
    This function get a number and check if it was a perfect square or not
    :param n: a number(int)
    :return: True(if the number is perfect square), or False (if the number is NOT perfect square)
    Time Complexity: O( sqrt(n) )
    '''
    # the number is not perfect square if it is Negative or 3
    if (n < 0) or (n == 3):
        return False
    # the number is perfect square if it is 0 or 1
    elif (n == 0) or (n == 1):
        return True
    # testing many numbers to find the perfect square
    else:
        for i in range((n//2)+1):
            # if i*i equal the given number then it is perfect square
            if i*i == n:
                return True
            # if i*i greater the given number then it has exeded the number thus it is not a perfect square
            if i*i > n:
                return False
            # if i*i less than the given number then change i
            if i*i < n:
                continue


# Test Case #1: False
print(is_square(-1))

# Test Case #2: True
print(is_square(0))

# Test Case #3: False
print(is_square(3))

# Test Case #4: True
print(is_square(25))

# Test Case #5: True
print(is_square(119399329))