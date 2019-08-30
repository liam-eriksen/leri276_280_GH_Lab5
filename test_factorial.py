import unittest     # Import the Python unit testing framework
import maths        # Our code to test

class FactorialTest(unittest.TestCase):
    def test_factorial(self):
        result = maths.factorial(5)
        self.assertEqual(result, 120)
        
if __name__ == '__main__':
    unittest.main()
