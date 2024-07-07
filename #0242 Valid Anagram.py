class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if two strings are anagrams of each other.

        Args:
            s (str): First string.
            t (str): Second string.

        Returns:
            bool: True if s and t are anagrams, False otherwise.
        """
        if len(s) != len(t):
            return False

        char_count = {}

        # Count occurrences of each character in s
        for l in s:
            char_count[l] = char_count.get(l, 0) + 1
        
        # Compare with t
        for l in t:
            if l not in char_count or char_count[l] == 0:
                return False
            char_count[l] -= 1
        
        return True
