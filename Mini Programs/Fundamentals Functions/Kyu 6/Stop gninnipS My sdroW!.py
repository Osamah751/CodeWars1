"""
6 kyu
Stop gninnipS My sdroW!

Write a function that takes in a string of one or more words,
and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata).
Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:
    spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
    spinWords( "This is a test" ) => returns "This is a test"
    spinWords( "This is another test" )=> returns "This is rehtona test"
"""
import random

def spin_words(sentence):
    Answer = []
    lst = sentence.split(" ")
    for word in lst:
        if len(word) >= 5:
            # to reverse the word
            word = word[::-1]

            # to shuffle the word
            # word = ''.join(random.sample(word, len(word)))

        Answer.append(word)
    return ' '.join(Answer)


# Test Case 1: ("Hey wollef sroirraw")
print(spin_words("Hey fellow warriors"))

# Test Case 2: ("This is a test")
print(spin_words("This is a test"))

# Test Case 3: ("This is rehtona test")
print(spin_words("This is another test"))

# Test Case 4: ("emocleW")
print(spin_words("Welcome"))
