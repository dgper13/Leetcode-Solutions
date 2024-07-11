from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers in an array that add up to a specific target.

        Parameters:
        nums (List[int]): The input list of integers.
        target (int): The target sum to find.

        Returns:
        List[int]: Indices of the two numbers in the array that add up to target.
        """
        seen = {}  # Dictionary to store seen elements and their indices

        for i, n in enumerate(nums):
            complementary = target - n  # Calculate the complementary number needed to reach the target
            if complementary in seen:
                return [seen[complementary], i]  # Return indices of the pair that sums to target
            seen[n] = i  # Store current number and its index in the dictionary

        return []  # Return an empty list if no such pair is found
