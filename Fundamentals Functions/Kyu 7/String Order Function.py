def order(sentence):
    '''
    This function takes one argument(string) a sentence with words that has numbers in it
    and it sorts the sentence using the numbers given in the words

    input: String(Sentence words that have numbers in it)
    output: sorted String(sorted by the numbers inside words)
    time: O(log(n))
    '''
    # convert string->list
    result = []
    lst = sentence.split(' ')

    # count the number of words in the string
    for i in range(len(lst) + 1):
        # starting from 0 to the (number of words in the string)
        for j in lst:
            if str(i) in j:
                result.append(j)

    # convert list->string
    result = ' '.join(result)
    return result


# Test Case 1: ("Thi1s is2 3a T4est")
# print(order("is2 Thi1s T4est 3a"))

# Test Case 2: ("Fo1r the2 g3ood 4of th5e pe6ople")
# print(order("4of Fo1r pe6ople g3ood th5e the2"))
