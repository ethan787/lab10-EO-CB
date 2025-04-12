import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(-5,-4),-9)
        self.assertNotEqual(add(3,111),9)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(9,5),4)
        self.assertEqual(sub(-9,5),-14)
        self.assertNotEqual(sub(9,5),3)

    ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ####### Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0,5)

    # call division function inside, example:
    # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(3,2),math.log(3,2))
        self.assertEqual(log(2,10),math.log(2,10))
        self.assertEqual(log(0,3),math.log(0,3))
    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(2,-2)
# use same technique from test_divide_by_zero
    ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()