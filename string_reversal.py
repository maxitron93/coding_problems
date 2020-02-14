'''
Given a string, return a new string with the reversed order of characters
'''

def reverse_string_my_attempt(string):
    new_string = ''
    for i in range(len(string)):
        i = i + 1
        new_string += string[-i]
    return new_string


def reverse_string_sol_1(string):
    string.split()
    return string[::-1]
