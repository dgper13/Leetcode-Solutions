from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Check if there are any duplicate elements within k indices in the given list.

        Args:
        nums (List[int]): List of integers to check for duplicates.
        k (int): Maximum distance between indices to consider duplicates.

        Returns:
        bool: True if there are duplicates within k indices, False otherwise.
        """
        seen = {}
        
        for i, n in enumerate(nums):
            if n in seen:
                # Check if the difference between current index and previous index of n is <= k
                if abs(i - seen[n]) <= k:
                    return True
            # Update the last seen index of n
            seen[n] = i
            
        return False
