class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Reverse the order of words in a given string.

        A word is defined as a maximal substring consisting of non-space characters only.

        Args:
        s (str): The input string containing words separated by spaces.

        Returns:
        str: The string with words in reversed order.
        """
        # Split the string into a list of words
        words = s.split()
        
        # Initialize two pointers
        i = 0
        j = len(words) - 1

        # Reverse the list of words in-place
        while i < j:
            words[i], words[j] = words[j], words[i]
            i += 1
            j -= 1

        # Join the reversed list of words back into a single string
        return " ".join(words)
