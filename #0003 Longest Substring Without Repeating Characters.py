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
        j = 1  # Right pointer of the window
        
        max_len = 1  # Initialize the maximum length of the substring
        window = set(s[0])  # Initialize the set with the first character

        while j < s_len:
            if s[j] in window:
                # If character at j is already in the set, remove character at i and move i forward
                window.remove(s[i])
                i += 1
            else:
                # If character at j is not in the set, add it and move j forward
                window.add(s[j])
                j += 1
                # Update the maximum length found so far
                max_len = max(max_len, j - i)
        
        return max_len
