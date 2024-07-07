from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        """
        Check if there are three consecutive odd numbers in the array.

        Args:
            arr (List[int]): The list of integers to check.

        Returns:
            bool: True if there are three consecutive odd numbers, False otherwise.
        """
        n_odds = 0  # Counter for consecutive odd numbers
        for n in arr:
            if n % 2 != 0:  # Check if the number is odd
                n_odds += 1
                if n_odds == 3:  # Found three consecutive odd numbers
                    return True
            else:
                n_odds = 0  # Reset counter if the number is even
        return False
    