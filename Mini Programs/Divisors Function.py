'''
Create a function named divisors/Divisors that
takes an integer n > 1
and
returns an array with all of the integer's divisors(except for 1 and the number itself),
from smallest to largest.

If the number is prime return the string '(integer) is prime'.

Example:
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
'''


def divisors(integer):
    '''
    :param integer: an integer n > 1
    :return: an array with all of the integer's divisors (from smallest to largest)
    '''

    answer = []
    for i in range(2, integer):
        if integer % i == 0:
            answer.append(i)
    if not answer:
        return str(integer) + " is prime"
    else:
        return answer


# Test Case #1: ([3, 5])
print(divisors(15))

# Test Case #2: ([2, 3, 4, 6])
print(divisors(12))

# Test Case #3: ("13 is prime")
print(divisors(13))
