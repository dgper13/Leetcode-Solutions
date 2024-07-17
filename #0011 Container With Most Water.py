from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Calculate the maximum area of water that can be contained by the lines.

        Args:
        height (List[int]): List of non-negative integers representing the height of each line.

        Returns:
        int: The maximum area of water that can be contained.
        """
        i = 0  # Initialize left pointer
        j = len(height) - 1  # Initialize right pointer
        max_area = 0  # Initialize max_area to 0

        while i < j:
            # Calculate the current area with the current pointers
            current_area = (j - i) * min(height[i], height[j])
            # Update max_area if the current area is greater
            max_area = max(max_area, current_area)

            # Move the pointer that points to the shorter line inward
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return max_area
