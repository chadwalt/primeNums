## Print out if a number is a prime number.

import unittest ## Inport the pytest for testing.

def get_user_input ():
    user_input = input('Enter a number')
    return user_input

class Tests (unittest.TestCase) :       
    ## User input cannot be a string.
    def test_string_test (self):
        self.assertEqual(type(get_user_input()),  'int')

    ## User input cannot be a negative. 
    def test_negative_test (self):
        self.assert_(int(get_user_input()) < 0)

    ## User input cannot be an empty string.
    def test_empty_string (self):
        self.assertEqual(get_user_input(), '')

    ## User input cannot be one.
    def test_one_test (self):
        self.assertEqual(int(get_user_input ()) ,1)

    ## User input is not a floating point number.
    def test_float_num (self) :
        self.assertEqual(type(get_user_input()), 'float')

if __name__ == '__main__':
    unittest.main()