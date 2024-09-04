from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets in the list that sum to zero.

        Args:
        nums (List[int]): The list of integers.

        Returns:
        List[List[int]]: A list of unique triplets [a, b, c] such that a + b + c = 0.
        """
        res = []  # To store the resulting triplets
        nums.sort()  # Sort the input list to facilitate the two-pointer approach

        # Iterate through the list, considering each number as the first element of the triplet
        for i, a in enumerate(nums):
            # Skip duplicate values to avoid duplicate triplets in the result
            if i > 0 and a == nums[i - 1]:
                continue
            
            l = i + 1  # Left pointer starts just after the current element
            r = len(nums) - 1  # Right pointer starts at the end of the list

            # Use the two-pointer technique to find valid triplets
            while l < r:
                three_sum = a + nums[l] + nums[r]  # Calculate the sum of the triplet

                if three_sum > 0:
                    r -= 1  # If the sum is too large, move the right pointer left
                elif three_sum < 0:
                    l += 1  # If the sum is too small, move the left pointer right
                else:
                    # Found a triplet that sums to zero, add it to the result list
                    res.append([a, nums[l], nums[r]])
                    l += 1  # Move the left pointer to avoid duplicates
                    # Skip over duplicates in the left pointer
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                
        return res
