## Print out if a number is a prime number.

import unittest ## Inport the pytest for testing.

def get_user_input ():
    user_input = input('Enter a number')
    return type (user_input)

## User input cannot be a string.
def string_test ():
    assert get_user_input() == 'int'

## User input cannot be a negative. 
def negative_test ():
    assert get_user_input() < 0

## User input cannot be one.

def one_test ():
    assert get_user_input () == 1


if __name__ == '__main__':
    unittest.main()