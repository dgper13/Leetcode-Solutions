from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Generate all possible letter combinations that the number could represent.

        Args:
        digits (str): A string containing digits from 2 to 9.

        Returns:
        List[str]: A list containing all possible letter combinations.
        """
        # Mapping of digits to corresponding letters
        phone_digits = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"], 
            "9": ["w", "x", "y", "z"]
        }

        res = []  # To store the resulting letter combinations

        def backtracking(index, current_combination):
            """
            Recursive helper function to generate combinations.

            Args:
            index (int): Current index in the digits string.
            current_combination (str): The current letter combination being formed.
            """
            # Base case: If the current combination has the same length as the digits
            if index == len(digits):
                res.append(current_combination)  # Add the current combination to the result list
                return
            
            # Get the letters corresponding to the current digit
            for letter in phone_digits[digits[index]]:
                # Append the letter to the current combination and move to the next digit
                backtracking(index + 1, current_combination + letter)

        # If the digits string is not empty, start the backtracking process
        if digits:
            backtracking(0, "")
        
        return res
