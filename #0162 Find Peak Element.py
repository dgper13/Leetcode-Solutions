from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        This function finds a peak element in the input list and returns its index.
        A peak element is defined as an element that is greater than its neighbors.
        
        Args:
        nums (List[int]): A list of integers.
        
        Returns:
        int: The index of a peak element.
        """
        left = 0
        right = len(nums) - 1

        # Binary search loop to find a peak element
        while left < right:
            mid = left + (right - left) // 2  # Calculate the middle index

            # Compare mid element with the next element
            if nums[mid] < nums[mid + 1]:
                # If mid element is less than the next element,
                # then a peak must be in the right half, excluding mid
                left = mid + 1
            else:
                # If mid element is greater than or equal to the next element,
                # then a peak is in the left half including mid
                right = mid
        
        # When the loop finishes, left == right and points to a peak element
        return left
