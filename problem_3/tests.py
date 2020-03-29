import unittest

from solution import *

class MyTestCase(unittest.TestCase):
    def test_object(self):
        product = Solution("4","5")
        return self.assertIsNotNone(product) #tests if num_hash works

    def test_product(self):
        product = Solution("4","5")
        return self.assertEqual(product.multiply(),"20") #tests if multiplication works with only hash one digit numbers

    def test_largeproduct(self):
        product = Solution("12","56")
        return self.assertIsNotNone(product.multiply()) #tests for large numbers(output currently only returns a integer)

    def test_tostring(self):
        string = tostring(9)
        return self.assertIsNotNone(string,"9") #tests if string_hash works

    def test_tostring1(self):
        string = tostring(9)
        return self.assertEqual(string,"9") #tests single-digit in the string_hash

    def test_tostring2(self):
        string = tostring(15)
        return self.assertEqual(string,"15") #tests double-digit

    def test_tolargestring(self):
        string = tostring(320921)
        return self.assertEqual(string,"320921") #tests large number

    def test_largeproduct1(self):
        product = Solution("12","56")
        return self.assertEqual(product.multiply(),"672") #tests for large numbers(should output a string now)

    def test_largeproduct2(self):
        product = Solution("1234","5678")
        return self.assertEqual(product.multiply(),"7006652") #tests for large numbers(should output a string now)
    


if __name__ == '__main__':
    unittest.main()

