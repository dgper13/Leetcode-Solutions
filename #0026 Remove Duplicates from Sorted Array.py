from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates from a sorted list in place and return the new length.

        Parameters:
        nums (List[int]): The input list of integers (sorted in non-decreasing order).

        Returns:
        int: The new length of the list after removing duplicates.
        """
        if not nums:
            return 0  # Return 0 if the list is empty

        k = 1  # Pointer for the next position to place a unique element
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]  # Place the unique element at the next position
                k += 1  # Increment the position pointer
        return k  # Return the new length of the list
    