class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.

        Args:
        s (str): The input string.

        Returns:
        int: The length of the longest substring without repeating characters.
        """
        
        s_len = len(s)
        
        # Handle edge cases where the string is empty or has only one character
        if s_len == 0 or s_len == 1:
            return s_len

        i = 0  # Left pointer of the window
        max_len = 1  # Initialize the maximum length of the substring
        window = set(s[0])  # Initialize the set with the first character

        # Iterate through the string with the right pointer `j`
        for j in range(1, s_len):
            next_letter = s[j]
            
            # If the character at `j` is not in the set, expand the window
            if next_letter not in window:
                window.add(next_letter)
                max_len = max(max_len, j - i + 1)  # Update the max length
            else:
                # If the character is a duplicate, shrink the window from the left
                while s[i] != next_letter:
                    window.remove(s[i])  # Remove characters until the duplicate is removed
                    i += 1
                i += 1  # Move past the duplicate character
        
        return max_len
