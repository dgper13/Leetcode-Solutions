class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if a given string is a palindrome, considering only alphanumeric characters
        and ignoring cases.

        Args:
        s (str): The input string.

        Returns:
        bool: True if the string is a palindrome, False otherwise.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            # Move the left pointer to the next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            # Move the right pointer to the previous alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare the characters after converting to lowercase
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True