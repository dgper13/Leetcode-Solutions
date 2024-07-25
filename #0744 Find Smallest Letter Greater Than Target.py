from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        Find the smallest letter in the list that is larger than the target.

        This method uses binary search to efficiently find the smallest letter 
        in the sorted list `letters` that is larger than the `target`. If such a letter 
        is not found, it returns the first letter in the list.

        Args:
        letters (List[str]): A list of characters sorted in non-decreasing order.
        target (str): The target character to find the next greatest letter for.

        Returns:
        str: The next greatest letter after the target.
        """
        # Edge case: If target is greater than or equal to the last letter, return the first letter
        if letters[0] > target or letters[-1] <= target:
            return letters[0]
        
        left = 0
        right = len(letters) - 1
        res = letters[0]  # Default result if no greater letter is found
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # If the middle letter is greater than the target, update result and search left half
            if letters[mid] > target:
                res = letters[mid]
                right = mid - 1
            # If the middle letter is less than or equal to the target, search right half
            else:
                left = mid + 1
            
        return res
