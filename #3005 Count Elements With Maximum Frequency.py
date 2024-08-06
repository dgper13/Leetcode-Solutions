from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        """
        Count how many elements have the maximum frequency in the given list.

        Args:
        nums (List[int]): The list of integers.

        Returns:
        int: The number of elements with the maximum frequency.
        """
        
        # Dictionary to keep track of the frequency of each element
        seen = {}
        # Variable to keep track of the maximum frequency encountered
        max_frequency = 0

        # Count the frequency of each element in nums
        for n in nums:
            seen[n] = seen.get(n, 0) + 1  # Increment the frequency of the current element
            max_frequency = max(max_frequency, seen[n])  # Update the maximum frequency if needed

        # Count how many elements have the maximum frequency
        count = sum(freq for freq in seen.values() if freq == max_frequency)

        return count
