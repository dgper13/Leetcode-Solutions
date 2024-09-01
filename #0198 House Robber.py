from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Determines the maximum amount of money that can be robbed without robbing two adjacent houses.
        
        Args:
        nums (List[int]): List of non-negative integers representing the amount of money in each house.
        
        Returns:
        int: The maximum amount of money that can be robbed.
        """
        return self.helper(nums)

    def helper(self, nums: List[int]) -> int:
        """
        Helper function to calculate the maximum amount of money that can be robbed.
        
        Args:
        nums (List[int]): List of non-negative integers representing the amount of money in each house.
        
        Returns:
        int: The maximum amount of money that can be robbed.
        """
        if not nums:
            return 0

        rob1 = 0  # Max profit from previous to the previous house
        rob2 = 0  # Max profit from the previous house

        # Iterate through each house
        for n in nums:
            # Calculate the maximum profit if robbing the current house
            temp = max(n + rob1, rob2)
            # Update rob1 to be the previous rob2
            rob1 = rob2
            # Update rob2 to be the current maximum profit
            rob2 = temp

        return rob2
