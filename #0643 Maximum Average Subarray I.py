from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Find the maximum average subarray of length k.

        Args:
        nums (List[int]): A list of integers.
        k (int): The length of the subarray.

        Returns:
        float: The maximum average value of a subarray of length k.
        """
        # Calculate the sum of the first k elements
        current_sum = sum(nums[:k])
        # Initialize max_sum with the sum of the first k elements
        max_sum = current_sum

        # Iterate from the k-th element to the end of the list
        for i in range(k, len(nums)):
            # Update the current_sum by adding the next element and subtracting the element that is out of the window
            current_sum += nums[i] - nums[i - k]
            # Update max_sum if the current_sum is greater
            max_sum = max(max_sum, current_sum)

        # Return the maximum average value
        return max_sum / k
