class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Check if string s is a subsequence of string t.

        Args:
        s (str): The subsequence to check.
        t (str): The main sequence in which to check for the subsequence.

        Returns:
        bool: True if s is a subsequence of t, False otherwise.
        """
        len_s = len(s)
        len_t = len(t)
        
        # If s is longer than t, s cannot be a subsequence of t
        if len_s > len_t:
            return False
        
        i = 0
        j = 0
        
        # Iterate through both strings
        while i < len_s and j < len_t:
            # If characters match, move to the next character in s
            if s[i] == t[j]:
                i += 1
            # Always move to the next character in t
            j += 1
        
        # If we have iterated through all characters of s, it is a subsequence
        return i == len_s
