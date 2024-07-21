class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Given a string s consisting of some words separated by spaces, return the length 
        of the last word in the string. A word is a maximal substring consisting of non-space characters only.

        Args:
        s (str): The input string.

        Returns:
        int: The length of the last word in the string.
        """
        words = s.split(" ")  # Split the string into words based on spaces
        i = len(words) - 1  # Initialize index to the last word

        # Traverse backwards to find the last non-empty word
        while not words[i]:
            i -= 1
        
        return len(words[i])  # Return the length of the last non-empty word
