'''
Given an integer, return an integer that is the reverse ordering of numbers
reverseInt(15) == 51
reverseInt(981) == 189
reverseInt(500) == 5
reverseInt(-15) == -51
reverseInt(-90) == -9
'''

def my_sol(integer):
    str_int = str(integer)
    rev_str_int = ''
    if str_int[0] == '-':
        for i in range(len(str_int) - 1):
            i += 1
            rev_str_int += str_int[-i]
        rev_str_int = '-' + rev_str_int
    else:
        for i in range(len(str_int)):
            i += 1
            rev_str_int += str_int[-i]
    return int(rev_str_int)

def sol2(integer):
    str_int = str(integer)
    rev_str_int = ''
    for i in range(len(str_int)):
        i += 1
        rev_str_int += str_int[-i]

    if integer >= 0:
        return int(rev_str_int)
    else:
        return int(rev_str_int[:-1:]) * -1
