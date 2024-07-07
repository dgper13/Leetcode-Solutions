class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Determines if a given pattern matches the words in a string.

        A pattern matches a string if there is a bijection between a letter in the pattern 
        and a word in the string such that the same letter always maps to the same word.

        Args:
        pattern (str): The pattern string consisting of letters.
        s (str): The string of words separated by spaces.

        Returns:
        bool: True if the pattern matches the string, False otherwise.
        """
        pattern_list = list(pattern)
        words = s.split()

        if len(pattern_list) != len(words):
            return False

        char_to_word = {}
        word_set = set()

        for char, word in zip(pattern_list, words):
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                if word in word_set:
                    return False
                char_to_word[char] = word
                word_set.add(word)

        return True
