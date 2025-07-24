import math

class MathOperations:
    """
    A collection of basic mathematical operations.

    This class provides utility methods for performing common mathematical tasks
    such as exponentiation, factorial calculation, and prime number checking.
    """

    def power(self, base: int, exponent: int) -> int:
        """
        Calculates the power of a number.

        Args:
            base (int): The base of the exponentiation.
            exponent (int): The exponent to raise the base to.

        Returns:
            int: The result of raising the base to the given exponent.
        """
        return pow(base, exponent)
    
    def factorial(self, number: int) -> int:
        """
        Calculates the factorial of a given non-negative integer.

        Args:
            number (int): A non-negative integer whose factorial is to be computed.

        Returns:
            int: The factorial of the given number.

        Raises:
            ValueError: If the input is a negative integer.
        """
        '''
        n = number
        fact = 1
        for i in range(1, n+1):
            fact = fact * i
        '''
        return math.factorial(number)

    def is_prime(self, number: int) -> bool:
        """
        Determines whether a given number is a prime number.

        Args:
            number (int): The number to check for primality.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if number <= 1:
            return False
        else:
            for i in range(2, int(math.sqrt(number)) + 1):
                if number % i == 0:
                    return False
            return True
