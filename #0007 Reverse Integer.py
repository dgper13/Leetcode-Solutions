class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverses the digits of an integer, returning 0 if the result overflows a 32-bit signed integer.
        
        Args:
        x (int): The integer to reverse.
        
        Returns:
        int: The reversed integer or 0 if it overflows.
        """
        # Define the 32-bit signed integer bounds
        upper_limit = 2**31
        lower_limit = - upper_limit
        
        result = 0
        # Determine the sign of the number and work with its absolute value
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check if the result will overflow if we add the new digit
            if result > (upper_limit - digit) // 10:
                return 0
            
            # Update result with the new digit
            result = result * 10 + digit
        
        # Restore the original sign
        result *= sign
        
        # Check if the reversed result is within the 32-bit signed integer range
        if result > upper_limit or result < lower_limit:
            return 0
        
        return result
