from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums sorted in non-decreasing order,
        return an array of the squares of each number sorted in non-decreasing order.

        Args:
        nums (List[int]): A list of integers sorted in non-decreasing order.

        Returns:
        List[int]: A list of the squares of each number in nums sorted in non-decreasing order.
        """
        results = []  # List to store the squared values in sorted order
        left = 0  # Pointer to the start of the list
        right = len(nums) - 1  # Pointer to the end of the list

        # Iterate until the two pointers meet
        while left <= right:
            left_square = nums[left] * nums[left]  # Square of the left pointer value
            right_square = nums[right] * nums[right]  # Square of the right pointer value

            if right_square > left_square:
                # If right_square is greater, add it to the results list and move the right pointer leftwards
                results.append(right_square)
                right -= 1
            else:
                # If left_square is greater or equal, add it to the results list and move the left pointer rightwards
                results.append(left_square)
                left += 1

        results.reverse()  # Reverse the results list to get the squares in non-decreasing order

        return results
