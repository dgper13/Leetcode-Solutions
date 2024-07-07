class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Determines if two strings s and t are isomorphic.

        Two strings s and t are isomorphic if the characters in s can be replaced to get t.
        No two characters may map to the same character, but a character may map to itself.

        Args:
        s (str): The first string.
        t (str): The second string.

        Returns:
        bool: True if the strings are isomorphic, False otherwise.
        """
        if len(s) != len(t):
            return False

        char_map = {}
        mapped_chars = set()

        for char_s, char_t in zip(s, t):
            if char_s in char_map:
                if char_map[char_s] != char_t:
                    return False
            else:
                if char_t in mapped_chars:
                    return False
                char_map[char_s] = char_t
                mapped_chars.add(char_t)

        return True
