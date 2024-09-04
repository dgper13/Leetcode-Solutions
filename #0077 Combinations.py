from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Generate all combinations of `k` numbers out of the range `1` to `n`.

        Args:
        n (int): The upper limit of the range of numbers.
        k (int): The number of elements in each combination.

        Returns:
        List[List[int]]: A list of all possible combinations.
        """
        res = []  # To store the resulting combinations
        
        def backtracking(start, curr):
            """
            Recursive helper function to generate combinations.

            Args:
            start (int): The starting number for this stage of the combination.
            curr (List[int]): The current combination being formed.
            """
            # Base case: If the current combination has the desired length
            if len(curr) == k:
                res.append(curr)  # Add the current combination to the result list
                return
            
            # Iterate over the range starting from `start` to `n`
            for i in range(start, n + 1):
                # Recurse with the next number and the updated combination
                backtracking(i + 1, curr + [i])
        
        # Start the backtracking process with `start` as 1 and an empty combination
        backtracking(1, [])
        return res
