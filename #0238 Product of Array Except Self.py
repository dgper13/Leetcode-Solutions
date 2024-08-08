from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Returns an array such that each element at index 'i' is the product of all
        elements in the original array except for the element at index 'i'.

        Args:
        nums (List[int]): A list of integers.

        Returns:
        List[int]: A list where each element is the product of all other elements in 'nums'.
        """
        results = [1] * len(nums)  # Initialize the results array with 1s

        # Calculate the prefix products and store them in results
        prefix = 1
        for i in range(len(nums)):
            results[i] = prefix   # Store the current prefix product
            prefix *= nums[i]     # Update prefix with the current element
        
        # Calculate the postfix products and multiply them with the current value in results
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            results[i] *= postfix  # Multiply the current result with the postfix product
            postfix *= nums[i]     # Update postfix with the current element
        
        return results
