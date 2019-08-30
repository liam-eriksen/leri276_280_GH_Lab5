import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        #act
        result = maths.add(5,5)
        #assert
        self.assertEqual(result,10,"The add function returned an incorrect value!")
        

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        #act
        result = maths.fibonacci(5)
        #assert
        self.assertEqual(result, 5, "The fibonacci function returned the incorrect value!")
    
    def test_convert_base_low(self):
        '''Test the convert base function for a base less than 10'''
        #act
        result = maths.convert_base(15,5)
        #assert
        self.assertEqual(result, '30', "The convert_base function returned the incorrect value!")
    
    def test_convert_base_high(self):
        '''Test the convert base function for a base over 10'''
        #act
        result = maths.convert_base(15,12)
        #assert
        self.assertEqual(result, '13', "The convert_base function returned the incorrect value!")
        
    def test_add_convert_low(self):
        '''tests the add with the added conversion for a base less than 10 '''
        #act
        result = maths.add(5,5,5)
        #assert
        self.assertEqual(result, 20, "The add function returned an incorrect value!")
    
    def test_add_convert_high(self):
        '''tests the add with the added conversion for a base over 10 '''
        #act
        result = maths.add(5,10,12)
        #assert
        self.assertEqual(result, 13, "The add function returned an incorrect value!")
        

# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
