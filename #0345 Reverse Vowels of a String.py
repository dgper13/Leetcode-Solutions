class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Reverse the vowels in a given string while keeping non-vowel characters in their original positions.

        Args:
        s (str): Input string.

        Returns:
        str: String with vowels reversed.
        """
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        stack = []

        # Push vowels into a stack in their original order
        for char in s:
            if char in vowels:
                stack.append(char)

        new_s = ""

        # Build the new string with reversed vowels
        for char in s:
            if char in vowels:
                new_s += stack.pop()  # Pop vowel from stack if current character is a vowel
            else:
                new_s += char  # Append non-vowel character as it is

        return new_s
