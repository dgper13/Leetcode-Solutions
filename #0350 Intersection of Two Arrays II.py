from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Find the intersection of two integer arrays. Each element in the result should appear as many times
        as it shows in both arrays.

        Args:
        nums1 (List[int]): The first list of integers.
        nums2 (List[int]): The second list of integers.

        Returns:
        List[int]: A list containing the intersection of the two input lists.
        """
        # Ensure nums1 is the smaller or equal-sized array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # Dictionary to count occurrences of elements in nums1
        seen1 = {}

        # Count the frequency of each number in nums1
        for n in nums1:
            seen1[n] = seen1.get(n, 0) + 1
        
        # List to store the intersection result
        results = []

        # Find common elements with their frequency in nums2
        for n in nums2:
            if n in seen1 and seen1[n] > 0:
                results.append(n)
                seen1[n] -= 1
        
        return results
