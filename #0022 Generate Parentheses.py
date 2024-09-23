from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate all combinations of well-formed parentheses.

        Parameters:
        n (int): The number of pairs of parentheses.

        Returns:
        List[str]: A list of all valid combinations of parentheses.
        """
        # Base case: if n is 1, the only combination is "()"
        if n == 1:
            return ["()"]

        res = []

        def calc(curr: str, i: int, left: int, right: int):
            """
            Helper function to generate parentheses combinations.

            Parameters:
            curr (str): The current combination of parentheses being built.
            i (int): The current index for tracking the length of the combination.
            left (int): The number of '(' used.
            right (int): The number of ')' used.
            """
            # When the current combination reaches the maximum length
            if len(curr) == 2 * n:
                res.append(curr)
                return

            # If there are more ')' than '(', it's invalid
            if right > left:
                return

            # If we can still add '(', add it and recurse
            if left < n:
                calc(curr + "(", i + 1, left + 1, right)

            # If we can add ')', add it and recurse
            if right < left:
                calc(curr + ")", i + 1, left, right + 1)

        # Start the recursive generation of parentheses
        calc("", 0, 0, 0)

        return res
