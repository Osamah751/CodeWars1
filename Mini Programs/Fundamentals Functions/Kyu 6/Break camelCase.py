'''
6 kyu
Break camelCase

Complete the solution so that the function will break up camel casing, using a space between words.

Example
solution("camelCasing")  ==  "camel Casing"
solution("helloWorld") == "hello World"

Note From me:
1- the task is to add a space between the words.
2- The first world starts with lowercase letter, and the other words start with uppercase letters,
'''


def solution(string):
    Answer = []
    for index in range(len(string)):
        if string[index].isupper():
            Answer.append(' ')
        Answer.append(string[index])
    Answer = ''.join(Answer)

    return Answer


# Test Case #1: ("camel Casing")
# print(solution("camelCasing"))

# Test Case #2: ("hello World")
# print(solution("helloWorld"))

# Test Case #3: ("break Camel Case")
# print(solution("breakCamelCase"))
