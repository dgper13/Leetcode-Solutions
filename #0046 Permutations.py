from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible permutations of a list of numbers.

        Args:
        nums (List[int]): The list of integers to permute.

        Returns:
        List[List[int]]: A list of all possible permutations.
        """
        res = []  # To store the resulting permutations
        entry_len = len(nums)  # Length of the input list

        def backtracking(i, curr, remaining):
            """
            Recursive helper function to generate permutations.

            Args:
            i (int): The current depth in the recursion.
            curr (List[int]): The current permutation being formed.
            remaining (List[int]): The list of numbers left to use in the permutation.
            """
            # Base case: If the current permutation has the desired length
            if len(curr) == entry_len:
                res.append(curr)  # Add the current permutation to the result list
                return

            # Iterate over the remaining numbers to generate permutations
            for j, n in enumerate(remaining):
                local = remaining.copy()  # Copy the remaining numbers
                local.pop(j)  # Remove the current number from the remaining list
                # Recurse with the next number added to the permutation
                backtracking(i + 1, curr + [n], local)

        # Start the backtracking process with the initial empty permutation
        backtracking(0, [], nums)
        return res
