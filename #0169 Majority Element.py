from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Find the majority element in an array. A majority element appears more than ⌊ n/2 ⌋ times.

        Parameters:
        nums (List[int]): The input list of integers.

        Returns:
        int: The majority element in the array.
        """
        count = 0  # Initialize count of majority element
        major = 0  # Initialize majority element candidate
        
        for i in range(len(nums)):
            if count == 0:
                major = nums[i]  # Update major to current element if count is 0
            if major == nums[i]:
                count += 1  # Increment count if current element is equal to major
            else:
                count -= 1  # Decrement count if current element is not equal to major
        
        return major  # Return the majority element
