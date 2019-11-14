'''
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

Examples:-
expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'


NOTE: All numbers will be whole numbers greater than 0.
'''


def expanded_form(num):
    '''
    input: number
    output: string(the number as a string in Expanded Form)
    time: O(n)
    '''
    result = []

    # convert the Number given to String
    num = str(num)

    # check one digit at a time
    for i in range(1, len(num)+1):
        if num[i-1] == '0':
            continue
        else:
            result.append(int(num[i-1]) * (10**(len(num)-i)))

    # wraps the result to the wanted form
    result = "".join(str(result))
    result = result[1:-1]
    result = result.replace(",", " +")
    return result


# Test Case #1:
print(expanded_form(142))


