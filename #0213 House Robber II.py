from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Solves the 'House Robber' problem where houses are arranged in a circle.

        Args:
        nums (List[int]): A list of integers representing the amount of money at each house.

        Returns:
        int: The maximum amount of money that can be robbed without triggering alarms.
        """
        # If there's only one house, return the money in that house
        if len(nums) == 1:
            return nums[0]

        # Since houses are in a circle, either rob from the 2nd house to the last house
        # or rob from the 1st house to the second-to-last house
        return max(
            self.helper(nums[1:]),  # Case 1: Exclude the first house
            self.helper(nums[:-1])  # Case 2: Exclude the last house
        )
        
    def helper(self, nums: List[int]) -> int:
        """
        Helper function to solve the 'House Robber' problem for a linear list of houses.

        Args:
        nums (List[int]): A list of integers representing the amount of money at each house.

        Returns:
        int: The maximum amount of money that can be robbed.
        """
        if not nums:
            return 0

        # Initialize variables to store the maximum money that can be robbed
        rob1, rob2 = 0, 0

        # Iterate through each house
        for n in nums:
            # Calculate the new maximum if we rob the current house
            temp = max(n + rob1, rob2)
            rob1 = rob2  # Move the previous max to rob1
            rob2 = temp  # Update rob2 to the new max

        return rob2  # Return the maximum money that can be robbed
