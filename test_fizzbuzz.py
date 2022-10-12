import unittest 

from program import fizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def test_0_fizzbuzz(self):
        self.assertEqual(fizzBuzz(3), "Fizz")
        self.assertEqual(fizzBuzz(6), "Fizz")
        self.assertEqual(fizzBuzz(5), "Buzz")
        self.assertEqual(fizzBuzz(10), "Buzz")
        self.assertEqual(fizzBuzz(15), "FizzBuzz")
        self.assertEqual(fizzBuzz(45), "FizzBuzz")
        self.assertEqual(fizzBuzz(1), 1)
        self.assertEqual(fizzBuzz(7), 7)

if __name__ == '__main__':
    unittest.main()
    