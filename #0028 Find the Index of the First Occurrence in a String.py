class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Implement strStr() function. Given two strings, return the index of the first occurrence 
        of 'needle' in 'haystack', or -1 if 'needle' is not part of 'haystack'.

        Parameters:
        haystack (str): The main string to search within.
        needle (str): The substring to search for.

        Returns:
        int: The index of the first occurrence of 'needle' in 'haystack', or -1 if not found.
        """
        
        if len(haystack) < len(needle):
            return -1  # If haystack is shorter than needle, needle cannot be found

        i = 0  # Pointer for haystack
        j = 0  # Pointer for needle
        needle_length = len(needle)  # Length of the needle

        while i < len(haystack):
            if haystack[i] == needle[j]:
                j += 1  # Move to the next character in needle
                if j == needle_length:
                    return i - j + 1  # Found the needle, return the start index
                i += 1  # Move to the next character in haystack
            else:
                i = i - j + 1  # Reset haystack pointer to the next position after the last match
                j = 0  # Reset needle pointer
                
        return -1  # Needle not found in haystack
