from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate the array to the right by k steps in-place.

        Args:
        nums (List[int]): The list of integers to be rotated.
        k (int): The number of steps to rotate the list.

        Returns:
        None: The function modifies the list in-place.
        """
        k = k % len(nums)  # Calculate effective rotations needed

        # Reverse the entire list
        nums.reverse()

        # Reverse the first part (from start to k-1)
        part1 = nums[:k]
        part1.reverse()
        nums[:k] = part1

        # Reverse the second part (from k to end)
        part2 = nums[k:]
        part2.reverse()
        nums[k:] = part2
