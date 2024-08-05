from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        """
        Calculate the minimum number of swaps required to group all 1's together in the list.

        Args:
        nums (List[int]): A list of integers containing 0's and 1's.

        Returns:
        int: The minimum number of swaps required.
        """
        N = sum(nums)  # Total number of 1's in the list
        L = len(nums)  # Length of the data list

        # Count the number of 0's in the first window of size N
        curr = nums[:N].count(0)
        min_swaps = curr  # Initialize the minimum swaps with the count of 0's in the first window

        # Slide the window across the list using a circular approach
        for i in range(1, L):
            # Update the count of 0's in the current window
            if nums[i - 1] == 0:
                curr -= 1  # Subtract the 0 that is leaving the window
            if nums[(i + N - 1) % L] == 0:
                curr += 1  # Add the 0 that is entering the window
            # Update the minimum swaps if the current count of 0's is less than the previous minimum
            min_swaps = min(min_swaps, curr)

        return min_swaps  # Return the minimum number of swaps required
