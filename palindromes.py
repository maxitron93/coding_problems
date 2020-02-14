'''
Given a string, return true if the string is a palindrome or false if not.
Palindromes are strings that form the same word if it's reversed.
'''

def check_palindrome_1(string):
    reversed_string = ''
    for i in range(len(string)):
        i = i + 1
        reversed_string += string[-i]
    return string == reversed_string
