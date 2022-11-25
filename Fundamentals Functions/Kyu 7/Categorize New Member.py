'''
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

Input
Input will consist of a list of lists containing two items each. Each list contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.

Note for F#: The input will be of (int list list) which is a List<List>

Example Input
[[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]
Output
Output will consist of a list of string values (in Haskell: Open or Senior) stating whether the respective member is to be placed in the senior or open category.

Example Output
["Open", "Open", "Senior", "Open", "Open", "Senior"]
'''


def openOrSenior(data):
    '''
    This function check weather each member a ("Senior"){older than 55 years old and has greater than 5 handicap.Otherwise, it is ("Open").
    :param data: a (list-> sub-list -> 2-element(age, handicap)
    :return: a list, each element in the list is either ("Senior") if the satisfy the requirements, otherwise it is ("Open")
    Time: O(n)
    '''
    output_list = []
    # Check each sub-list in the data
    for person in data:

        # if the person have the required to be a ("Senior") otherwise they are ("Open")
        if (person[0] >= 55) and (person[1] > 7):
            output_list.append("Senior")
        else:
            output_list.append("Open")

    return output_list


# Test Case #1: (['Open', 'Senior', 'Open', 'Senior'])
print(openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]]))

# Test Case #2: (['Open', 'Open', 'Senior', 'Open'])
print(openOrSenior([[16, 23],[73,1],[56, 20],[1, -1]]))