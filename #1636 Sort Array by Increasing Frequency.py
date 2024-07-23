from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        """
        Sort the numbers in the list based on their frequency. Numbers that appear more frequently come first.
        If two numbers have the same frequency, the larger number comes first.

        Args:
        nums (List[int]): The list of integers to be sorted.

        Returns:
        List[int]: The list of integers sorted by frequency and then by value.
        """
        # Dictionary to store the frequency of each number
        seen = {}

        # Count the frequency of each number in the list
        for n in nums:
            seen[n] = seen.get(n, 0) + 1
        
        # Sort the items by frequency (ascending) and by number (descending) for tie-breaking
        seen_sorted = sorted(list(seen.items()), key=lambda x: (x[1], -x[0]))

        # Construct the result list based on sorted frequencies
        results = []
        for n, f in seen_sorted:
            results.extend([n] * f)
        
        return results
