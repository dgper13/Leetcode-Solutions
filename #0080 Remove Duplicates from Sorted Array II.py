from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates from a sorted list in-place such that duplicates appeared at most twice 
        and return the new length of the list.

        Args:
        nums (List[int]): The input list of integers, sorted in non-decreasing order.

        Returns:
        int: The new length of the list after removing duplicates.
        """
        i = 0  # Pointer to place the next valid element

        for n in nums:
            # Place element at index i if it's the first or second element,
            # or if it's different from the element at i-2 position
            if i == 0 or i == 1 or nums[i-2] != n:
                nums[i] = n
                i += 1
        
        return i
