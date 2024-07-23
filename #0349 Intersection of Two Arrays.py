from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Find the intersection of two integer arrays. Each element in the result should appear
        in the intersection of the two arrays. Duplicate elements should be listed only once.

        Args:
        nums1 (List[int]): The first list of integers.
        nums2 (List[int]): The second list of integers.

        Returns:
        List[int]: A list containing the intersection of the two input lists.
        """
        # Ensure nums1 is the smaller or equal-sized array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # Convert nums1 to a set for O(1) average time complexity lookups
        set1 = set(nums1)
        
        # Set to store the intersection result
        results = set()
        
        # Iterate through nums2 and add common elements to results
        for n in nums2:
            if n in set1:
                results.add(n)
        
        # Convert the set to a list before returning
        return list(results)
