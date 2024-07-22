class Solution:
    def fib(self, n: int) -> int:
        """
        Calculate the nth Fibonacci number.

        Args:
        n (int): The position of the Fibonacci number to calculate.

        Returns:
        int: The nth Fibonacci number.
        """
        # Base cases for Fibonacci sequence
        if n == 0 or n == 1:
            return n
        
        # Initialize the first two Fibonacci numbers
        a = 0
        b = 1
        
        # Calculate the Fibonacci number iteratively
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        
        return c
