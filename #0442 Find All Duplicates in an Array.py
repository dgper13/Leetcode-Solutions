from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Finds all the elements that appear twice in an array where the numbers are between 1 and n (inclusive).

        Args:
        nums (List[int]): The list of integers.

        Returns:
        List[int]: A list of integers that appear twice in the array.
        """
        
        res = []  # List to store the result

        # Iterate through each number in the list
        for n in nums:
            # Take the absolute value of the current number
            n = abs(n)
            
            # Check the value at the index (n-1)
            if nums[n-1] < 0:
                # If the value is negative, it means the number n has been seen before
                res.append(n)
            else:
                # Otherwise, negate the value at the index (n-1) to mark it as seen
                nums[n-1] *= -1

        return res
