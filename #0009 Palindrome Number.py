class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Check if the given integer is a palindrome.

        A palindrome is a number that reads the same backward as forward.

        Args:
            x (int): The integer to check.

        Returns:
            bool: True if the integer is a palindrome, False otherwise.
        """
        # Handle negative numbers and numbers ending in zero
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        s = str(x)
        length = len(s)
        middle_index = length // 2
        
        # Check palindrome by comparing characters
        for i in range(middle_index):
            if s[i] != s[length - 1 - i]:
                return False
        
        return True
    