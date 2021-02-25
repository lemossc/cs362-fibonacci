import unittest
import fibonacci


# Pytest
def test_fibonacci():
    result = fibonacci.fibonacci(13)
    assert result == 233


# Unittest Fibonacci
class TestFibonacci(unittest.TestCase):
    def test_invalid_input(self):
        # String
        result = fibonacci.fibonacci("length")
        self.assertEqual(result, None)
        # Complex
        result = fibonacci.fibonacci(complex(5, 3))
        self.assertEqual(result, None)
        # Negative
        result = fibonacci.fibonacci(-1)
        self.assertEqual(result, None)

    def test_float(self):
        result = fibonacci.fibonacci(2.5)
        self.assertEqual(result, None)

    def test_int(self):
        result = fibonacci.fibonacci(0)
        self.assertEqual(result, 0)

        result = fibonacci.fibonacci(7)
        self.assertEqual(result, 13)

        result = fibonacci.fibonacci(12)
        self.assertEqual(result, 144)

        result = fibonacci.fibonacci(3)
        self.assertEqual(result, 2)

        result = fibonacci.fibonacci(20)
        self.assertEqual(result, 6765)


# Unittest Factorial
class TestFactorial(unittest.TestCase):
    def test_invalid_input(self):
        # String
        result = fibonacci.factorial("length")
        self.assertEqual(result, None)
        # Complex
        result = fibonacci.factorial(complex(5, 3))
        self.assertEqual(result, None)
        # Negative
        result = fibonacci.factorial(-1)
        self.assertEqual(result, None)
        # Float
        result = fibonacci.factorial(2.5)
        self.assertEqual(result, None)

    def test_int(self):
        result = fibonacci.factorial(0)
        self.assertEqual(result, 1)

        result = fibonacci.factorial(1)
        self.assertEqual(result, 1)

        result = fibonacci.factorial(2)
        self.assertEqual(result, 2)

        result = fibonacci.factorial(3)
        self.assertEqual(result, 6)

        result = fibonacci.factorial(7)
        self.assertEqual(result, 5040)

        result = fibonacci.factorial(12)
        self.assertEqual(result, 479001600)


if __name__ == "__main__":
    unittest.main()

