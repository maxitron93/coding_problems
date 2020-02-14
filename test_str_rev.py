import unittest
from string_reversal import reverse_string_my_attempt as rev_str_try
from string_reversal import reverse_string_sol_1 as rev_str_sol_1

class TestStringReversal(unittest.TestCase):
    string1 = 'this is a test string'
    string2 = 'this is how to do multiple tests on the same function'
    string3 = 'and a third one just for fun'

    def test_rev_str_my_attempt(self): # the name has to be test_ followed by the function name
        self.assertEqual(rev_str_try(self.string1), self.string1[::-1])
        self.assertEqual(rev_str_try(self.string2), self.string2[::-1])
        self.assertEqual(rev_str_try(self.string3), self.string3[::-1])

    def test_rev_str_sol_1(self):
        self.assertEqual(rev_str_sol_1(self.string1), self.string1[::-1])
        self.assertEqual(rev_str_sol_1(self.string2), self.string2[::-1])
        self.assertEqual(rev_str_sol_1(self.string3), self.string3[::-1])

if __name__ == '__main__':
    unittest.main()
