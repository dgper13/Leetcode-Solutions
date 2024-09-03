from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """
        Generate all possible permutations of a string by changing the case of the letters.

        Args:
        s (str): The input string containing letters and/or digits.

        Returns:
        List[str]: A list containing all possible case permutations of the string.
        """
        res = []  # To store the resulting permutations

        def backtracking(i, current):
            """
            Recursive helper function to generate permutations.

            Args:
            index (int): Current index in the string `s`.
            current (str): The current permutation being formed.
            """
            # Base case: If we have processed all characters in the string
            if i == len(s):
                res.append(current)  # Add the current permutation to the result list
                return
            
            # If the current character is a digit, keep it as is
            if s[i].isdigit():
                backtracking(i + 1, current + s[i])
            else:
                # Recursively explore the case where the current character is lowercase
                backtracking(i + 1, current + s[i].lower())
                # Recursively explore the case where the current character is uppercase
                backtracking(i + 1, current + s[i].upper())
        
        # Start the backtracking process from the first character with an empty current permutation
        backtracking(0, "")
        return res
