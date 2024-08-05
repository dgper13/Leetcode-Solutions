from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        """
        Find the k-th distinct string in the array that appears exactly once.

        Args:
        arr (List[str]): A list of strings.
        k (int): The index (1-based) of the distinct string to return.

        Returns:
        str: The k-th distinct string that appears exactly once, or an empty string if not found.
        """
        # Dictionary to keep track of the frequency of each string
        seen = {}

        # Count the frequency of each string in the array
        for s in arr:
            seen[s] = seen.get(s, 0) + 1

        # Adjust k to be zero-based
        k -= 1

        # Iterate through the dictionary to find the k-th distinct string
        for s in seen:
            if seen[s] == 1:  # Check if the string appears exactly once
                if k == 0:
                    return s  # Return the k-th distinct string
                else:
                    k -= 1  # Decrement k to find the next distinct string
        
        return ""  # Return an empty string if the k-th distinct string is not found
