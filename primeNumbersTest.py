## Print out if a number is a prime number.

import unittest ## Inport the pytest for testing.

## Get the user input
def get_user_input ():
    user_input = input('Enter a number')
    return user_input

## Print out the prime numbers.
def primeNumbers() :
    start_num = 0;
    end_num = input("Please provide a number");
    if end_num > 1 :
        for num in range(start_num, end_num + 1) :
            for i in range(2, num) :
                if num % i == 0: 
                    break
            else :
                print(num)

class Tests (unittest.TestCase) :       
    ## User input cannot be a string.
   ##def test_string_test (self):
        ##self.assertEqual(type(get_user_input()),  'str')

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
    ##def test_float_num (self) :
       ## self.assert_(float(get_user_input()), 'float')

if __name__ == '__main__':
    ##unittest.main()
    primeNumbers()