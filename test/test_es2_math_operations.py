import unittest
from esercizi_python import MathOperations

class TestMathOperations(unittest.TestCase):

    def setUp(self):
        self.mathoperations = MathOperations()

    def test_power(self):
        self.assertEqual(self.mathoperations.power(2, 0), 1)
        self.assertEqual(self.mathoperations.power(3, 3), 27)

    def test_factorial(self):
        self.assertEqual(self.mathoperations.factorial(1), 1)
        self.assertEqual(self.mathoperations.factorial(3), 6)
        self.assertEqual(self.mathoperations.factorial(6), 720)

    def test_is_prime(self):
        self.assertFalse(self.mathoperations.is_prime(1))
        self.assertTrue(self.mathoperations.is_prime(2))  # Si
        self.assertTrue(self.mathoperations.is_prime(3))  # Si
        self.assertFalse(self.mathoperations.is_prime(4))
        self.assertTrue(self.mathoperations.is_prime(5))  # Si
        self.assertFalse(self.mathoperations.is_prime(6))
        self.assertTrue(self.mathoperations.is_prime(7))  # Si
