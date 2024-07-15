from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Remove all instances of a specific value from a list in place and return the new length.

        Parameters:
        nums (List[int]): The input list of integers.
        val (int): The value to remove from the list.

        Returns:
        int: The new length of the list after removing the specified value.
        """
        k = 0  # Pointer for the next position to place a non-val element
        for n in nums:
            if n != val:
                nums[k] = n  # Place the non-val element at the next position
                k += 1  # Increment the position pointer
        return k  # Return the new length of the list
