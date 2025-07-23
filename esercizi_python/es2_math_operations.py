import math

class MathOperations:

    def power(self, base: int, exponent: int) -> int:
        return pow(base, exponent)
    
    def factorial(self, number: int) -> int:
        '''
        n = number
        fact = 1
        for i in range(1, n+1):
            fact = fact * i
        '''
        return math.factorial(number)

    def is_prime(self, number: int) -> bool:
        if number <= 1:
            return False
        else:
            for i in range(2, int(math.sqrt(number)) + 1):
                if number % i == 0:
                    return False
            return True
