from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Perform binary search to find the index of a target value in a sorted list.

        This method uses binary search to efficiently locate the target value in a 
        sorted list of integers. If the target is found, it returns its index. 
        If the target is not present in the list, it returns -1.

        Args:
        nums (List[int]): A list of integers sorted in ascending order.
        target (int): The integer value to search for in the list.

        Returns:
        int: The index of the target if found, otherwise -1.
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            # Check if the middle element is the target
            if nums[middle] == target:
                return middle
            
            # If target is greater, ignore left half
            elif nums[middle] < target:
                left = middle + 1
            
            # If target is smaller, ignore right half
            else:
                right = middle - 1
        
        # Target was not found
        return -1
