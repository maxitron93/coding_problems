import unittest
from reverse_int import my_sol as rev_int_1
from reverse_int import sol2 as rev_int_2

class TestMySol(unittest.TestCase):
    int1 = 15
    int2 = 981
    int3 = 500
    int4 = -15
    int5 = -90

    def test_my_sol(self):
        self.assertEqual(rev_int_1(self.int1), 51)
        self.assertEqual(rev_int_1(self.int2), 189)
        self.assertEqual(rev_int_1(self.int3), 5)
        self.assertEqual(rev_int_1(self.int4), -51)
        self.assertEqual(rev_int_1(self.int5), -9)

    def test_sol2(self):
        self.assertEqual(rev_int_2(self.int1), 51)
        self.assertEqual(rev_int_2(self.int2), 189)
        self.assertEqual(rev_int_2(self.int3), 5)
        self.assertEqual(rev_int_2(self.int4), -51)
        self.assertEqual(rev_int_2(self.int5), -9)

if __name__ == '__main__':
    unittest.main()
