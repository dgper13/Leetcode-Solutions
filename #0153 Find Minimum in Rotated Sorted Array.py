from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        This function finds the minimum element in a rotated sorted array.
        
        Args:
        nums (List[int]): A list of integers that represents a rotated sorted array.
        
        Returns:
        int: The minimum element in the array.
        """
        left = 0
        right = len(nums) - 1

        # Binary search loop to find the minimum element
        while left < right:
            mid = left + (right - left) // 2  # Find the middle index

            # If the middle element is less than the rightmost element, 
            # then the minimum must be in the left half including mid
            if nums[mid] < nums[right]:
                right = mid  # Move the right pointer to mid
            
            # If the middle element is greater than or equal to the rightmost element, 
            # then the minimum must be in the right half excluding mid
            else:
                left = mid + 1  # Move the left pointer to mid + 1
            
        # After the loop, left == right and points to the minimum element
        return nums[left]
