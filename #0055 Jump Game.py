from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Determines if you can reach the last index of the array.
        
        Args:
        nums (List[int]): A list of non-negative integers where each element represents the maximum jump length from that position.
        
        Returns:
        bool: True if you can reach the last index, False otherwise.
        """
        target = len(nums) - 1  # The target is the last index of the array

        # Iterate backward through the array starting from the second-to-last index
        for i in range(len(nums) - 2, -1, -1):
            # If the current index + its jump length can reach or exceed the target
            if i + nums[i] >= target:
                # Update the target to be the current index
                target = i
            
        # If after the loop the target is the first index, return True
        return target == 0
