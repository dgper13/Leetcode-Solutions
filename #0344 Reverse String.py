from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverse the input list of characters in place.

        This method reverses the order of elements in the given list of characters
        without using extra space for another list. 

        Args:
        s (List[str]): A list of characters to be reversed. The list is modified in place.

        Returns:
        None: This method does not return any value. It modifies the input list directly.
        """
        left = 0
        right = len(s) - 1

        # Reverse the list by swapping characters from both ends
        while left < right:
            # Swap characters at the current left and right indices
            s[left], s[right] = s[right], s[left]
            # Move the left pointer to the right and the right pointer to the left
            left += 1
            right -= 1
