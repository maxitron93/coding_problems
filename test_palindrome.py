import unittest
from palindromes import check_palindrome_1 as check_palindrome

class TestCheckPalindrime(unittest.TestCase):
    string1 = 'racecar'
    string2 = 'amanaplanacanalpanama'
    string3 = 'this is not a palindrime'
    string4 = 'neither is this'
    string5 = 'evacanistabbatsinacave'

    def test_check_palindrome_1(self):
        self.assertEqual(check_palindrome(self.string1), True)
        self.assertEqual(check_palindrome(self.string2), True)
        self.assertEqual(check_palindrome(self.string3), False)
        self.assertEqual(check_palindrome(self.string4), False)
        self.assertEqual(check_palindrome(self.string5), True)

if __name__ == '__main__':
    unittest.main()
