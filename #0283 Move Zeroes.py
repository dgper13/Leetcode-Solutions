from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Initialize the position for the next non-zero element
        non_zero_index = 0
        
        # Traverse through the list
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap elements if the current element is non-zero and not in the correct position
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                non_zero_index += 1
