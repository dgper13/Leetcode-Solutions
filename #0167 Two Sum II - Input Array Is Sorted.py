from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Find two numbers in a sorted array that add up to a specific target.

        Parameters:
        numbers (List[int]): The sorted array of numbers.
        target (int): The target sum to find.

        Returns:
        Returns:
        - List[int]: Indices of the two numbers in the array that add up to the target.
          If no such pair is found, an empty list is returned.
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        # If no valid pair is found
        return []
    