import unittest
import calculatons

class TestCalculations(unittest.TestCase):
    
    def test_add(self):
        result = calculatons.add(20,5)
        self.assertEqual(result,25)
    
    def test_multiply(self):
        result = calculatons.multiply(20,5)
        self.assertEqual(result,100)
    
    def test_subtract(self):
        result = calculatons.subtract(20,5)
        self.assertEqual(result,15)
        
    def test_divide(self):
        result = calculatons.divide(20,5)
        self.assertEqual(result,4)
        
if __name__ == '__main__':
    unittest.main()