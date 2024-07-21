from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Given a sorted array and a target value, return the index if the target is found. 
        If not, return the index where it would be if it were inserted in order.

        Args:
        nums (List[int]): A sorted list of integers.
        target (int): The target integer to find or insert.

        Returns:
        int: The index of the target if found, or the index where the target should be inserted.
        """
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2  # Calculate the mid index
            current = nums[mid]  # Get the value at mid index

            if current == target:
                return mid  # Target found, return its index
            elif current < target:
                low = mid + 1  # Adjust the lower bound
            else:
                high = mid - 1  # Adjust the upper bound
        
        return low  # Return the insertion point if target is not found
