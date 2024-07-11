class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Determine if a number is happy.

        A number is happy if repeatedly replacing it with the sum of the squares of its digits
        eventually leads to 1.

        Parameters:
        n (int): The number to check for happiness.

        Returns:
        bool: True if the number is happy, False otherwise.
        """
        seen = set()  # Set to store numbers seen during the process

        while n not in seen:
            if n == 1:
                return True  # If n becomes 1, it's a happy number
            else:
                seen.add(n)  # Add current number to the set of seen numbers
                n = calculate_happy(n)  # Calculate the next number in the sequence
        
        return False  # If we encounter a number already seen, it's not a happy number


def calculate_happy(n):
    """
    Calculate the sum of the squares of digits of a number.

    Parameters:
    num (int): The number for which the sum of squares of digits is to be calculated.

    Returns:
    int: The calculated sum of squares of digits.
    """
    result = 0
    while n > 0:
        digit = n % 10
        result += digit * digit
        n //= 10
    return result
