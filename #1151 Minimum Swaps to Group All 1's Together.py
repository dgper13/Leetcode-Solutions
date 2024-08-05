from typing import List

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        """
        Calculate the minimum number of swaps required to group all 1's together in the list.

        Args:
        data (List[int]): A list of integers containing 0's and 1's.

        Returns:
        int: The minimum number of swaps required.
        """
        L = len(data)  # Length of the data list
        N = sum(data)  # Total number of 1s in the data list
        
        # Count the number of 0s in the first window of size N
        curr = data[:N].count(0)
        min_swaps = curr  # Initialize the minimum swaps with the count of 0s in the first window

        # Slide the window across the list from index N to L-1
        for i in range(N, L):
            # Update the count of 0s in the current window
            curr += data[i] - data[i-N]
            # Update the minimum swaps if the current count of 0s is less than the previous minimum
            min_swaps = min(min_swaps, curr)

        return min_swaps  # Return the minimum number of swaps required
