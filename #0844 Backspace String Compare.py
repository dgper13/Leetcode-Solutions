class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

        Args:
        s (str): The first input string containing letters and '#' characters.
        t (str): The second input string containing letters and '#' characters.

        Returns:
        bool: True if both strings are equal after processing backspaces, False otherwise.
        """
        i = len(s) - 1  # Initialize pointer for the end of string s
        j = len(t) - 1  # Initialize pointer for the end of string t

        def get_next_valid_char_index(index: int, input_string: str) -> int:
            """
            This helper function returns the next valid character index in the input string,
            skipping the characters that should be removed due to backspaces ('#').

            Args:
            index (int): The current index in the string.
            input_string (str): The input string to process.

            Returns:
            int: The index of the next valid character or -1 if no valid character exists.
            """
            skips = 0  # Count of backspaces
            while index >= 0:
                if input_string[index] == '#':
                    skips += 1
                    index -= 1
                elif skips > 0:
                    skips -= 1
                    index -= 1
                else:
                    break
            return index

        # Compare characters from the end of both strings
        while i >= 0 or j >= 0:
            i = get_next_valid_char_index(i, s)
            j = get_next_valid_char_index(j, t)

            # If both pointers are valid, compare characters
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False

            # If one pointer is valid and the other is not, strings are not equal
            if (i >= 0) != (j >= 0):
                return False

            i -= 1  # Move to the next character in s
            j -= 1  # Move to the next character in t

        return True  # If all characters matched, return True
