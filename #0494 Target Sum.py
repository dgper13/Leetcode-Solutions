from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Calculate the number of ways to assign '+' or '-' signs to elements in `nums`
        to achieve a target sum.

        Args:
        nums (List[int]): List of integers to which '+' or '-' will be assigned.
        target (int): The target sum we want to achieve.

        Returns:
        int: The number of ways to achieve the target sum.
        """
        dp = {}  # Memoization dictionary to store previously computed results

        def backtracking(index, current_sum):
            """
            Recursive function to explore all possible ways of assigning '+' or '-' signs
            to achieve the target sum.

            Args:
            index (int): Current index in the nums list.
            current_sum (int): Current sum achieved with the assigned signs.

            Returns:
            int: Number of ways to achieve the target sum from the current index.
            """
            # Base case: If all elements are processed
            if index == len(nums):
                return 1 if current_sum == target else 0
            
            # Check if the result is already computed for the current state
            if (index, current_sum) in dp:
                return dp[(index, current_sum)]
            
            # Recursive calls: Include the current number with '+' and '-' signs
            dp[(index, current_sum)] = (backtracking(index + 1, current_sum + nums[index]) +
                                        backtracking(index + 1, current_sum - nums[index]))
            return dp[(index, current_sum)]
        
        return backtracking(0, 0)
