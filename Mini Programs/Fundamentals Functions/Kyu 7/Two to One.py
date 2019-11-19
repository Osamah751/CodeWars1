'''
7 kyu
Two to One

Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,

each taken only once - coming from s1 or s2.
Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
'''


def longest(s1, s2):
    '''
    this function takes two strings and makes them one without duplicated letters
    :param s1: a string of letters(str)
    :param s2: a string of letters(str)
    :return: one string made from s1 and s2 without duplicated letters
    '''

    answer = []

    # add all the letter from s1 to answer without duplicated letters
    for i in s1:
        if i not in answer:
            answer.append(i)

    # add all the letter from s2 to answer without duplicated letters
    for j in s2:
        if j not in answer:
            answer.append(j)

    answer = ''.join(sorted(answer))
    return answer


# Test Case #1: ("aehrsty")
print(longest("aretheyhere", "yestheyarehere"))

# Test Case #2: ("abcdefghilnoprstu")
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))

# Test Case #3: ("acefghilmnoprstuy")
print(longest("inmanylanguages", "theresapairoffunctions"))


'''
# best way

def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))
'''