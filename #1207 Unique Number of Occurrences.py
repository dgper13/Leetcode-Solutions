from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        Check if the number of occurrences of each value in the array is unique.

        Args:
        arr (List[int]): A list of integers.

        Returns:
        bool: True if the occurrences of each integer are unique, False otherwise.
        """
        
        seen = {}  # Dictionary to count occurrences of each element in the array

        # Count occurrences of each element
        for n in arr:
            seen[n] = seen.get(n, 0) + 1

        unique = set()  # Set to track unique occurrence counts

        # Check if each occurrence count is unique
        for count in seen.values():
            if count in unique:
                return False  # If the count is already in the set, return False
            unique.add(count)  # Add the count to the set

        return True  # If all counts are unique, return True
